# Scala syntax, Option, collections, ordering, and allocation

375 source-specific cases. Statements retain their historical scope and source stance. Read related PR cases for corrections or alternatives.

## Cases

- A1-0028 — RecurringInvestmentProcessor methods may not require List
- A1-0032 — Accumulate recurring planCount separately
- A1-0051 — Use collectFirst consistently in recurring validation processing
- A1-0055 — Use redistributeByCapacity for both optimizer cases
- A1-0056 — Use deltasById.keySet instead of minsById.keySet where applicable
- A1-0057 — Use deltasById instead of minsById in optimizer
- A1-0058 — Use positiveDeltasById.keySet for undecided IDs
- A1-0059 — Select minViolationToClamp via invalidMinIds.minBy(minViolationScores)
- A1-0062 — Optimizer callee already calls iterator
- A1-0063 — Replace another optimizer minsById reference with deltasById
- A1-0067 — Collect idsWithInvalidPositiveRange when max exists below min
- A1-0079 — Move nonFundingValidationSubscriptionCombinations calculation to scheduler base
- A1-0083 — grouped Iterator consumed by size before export scheduler logging
- A1-0084 — Match ExcludeAllInstrumentCombinations symmetrically in either optional tuple position
- A1-0101 — validateRequestForEtf accepts instrumentsMap.values already resolved from TAA
- A1-0116 — Compact restriction-group filtering with collect and flatten
- A1-0122 — Do not split TradingRestrictionGroups cases when both are true
- A1-0127 — Use Set.empty instead of empty string in goal acknowledgement handling
- A1-0144 — Keep targetWeights and targetAmounts derivation and fallback consistent
- A1-0148 — ThresholdBreachHelper may require weights.toList
- A1-0149 — ThresholdBreachHelper inner logic sorts by weight
- A1-0160 — Sort same-placement FRS by future maturity then orderId with Ordering
- A1-0168 — Define TradingAccountType Ordering with SGD or HKD first
- A1-0172 — Extract CashBalancePageGenerator Ordering
- A1-0177 — Sort and createPage in one Future.map and companion Ordering for transaction rows
- A1-0180 — Use sum for processing transaction total
- A1-0188 — Check account before statement and late-transaction Option lookup
- A1-0205 — Create Ordering for processing transaction pages
- A1-0212 — Optimizer full decision map includes zero orders; constructOrders filters them
- A1-0240 — Avoid refiltering goal plans
- A1-0265 — Cache effective minimums map in RebalanceSellAmountCalculator
- A1-0266 — Use List prepend when append order not needed
- A1-0302 — Zip optional metrics with inputs before flattening and collect
- A1-0315 — Use Option.map in both places
- A1-0335 — find returns only one plan
- A1-0425 — Collect all currencies missing FX before throwing
- A1-0439 — Second minOption appears redundant
- A1-0456 — CustomerId PK prevents duplicate fee profile; change collection type to Set
- A1-0496 — Parse all MStar benchmarks then accept only one with weight 100
- A1-0503 — Use deduped dailyMvMap in fee calculation
- A1-0528 — Fetch MStar basic info with mapAsync(2), id tuple, Sink.seq and toMap
- A1-0536 — Resolve translator once and map repository results; None locale uses identity
- A1-0583 — Use tail recursion for projection
- A1-0592 — Flatten positive charge fees then fold by FeeRateType and TradingAccountType
- A1-0595 — Traverse large readSideTransactions once while accumulating merged transactions and IDs
- A1-0596 — Map readside transactions and reuse upstreamById lookup
- A1-0604 — Avoid traversing readSideTransactions twice because collection may be large
- A1-0607 — Two nonoverlapping transaction lists only need concatenation
- A1-0608 — Do not reverse query-only list lacking order contract
- A1-0609 — Fold upstreamById.keySet with Set subtraction then map remaining IDs
- A1-0632 — Future group-by-customer optimization with canActionForCustomerGoals
- A1-0652 — Extract retrievedPrimaryBenchmarks with Option.when nonempty source list
- A1-0657 — Fold maybeBm so inceptionDate availability explicit
- A1-0716 — Use instrumentIds.size
- A1-0757 — Do not combine redundant Option.when and getOrElse
- A1-0775 — Map investmentRequests by ID before diff and membership checks
- A1-0788 — Use contains instead of exists equality
- A1-0789 — Resolve goal RRT plans before entityIds filter to avoid overfetch
- A1-0791 — Combine collect filter and following map to avoid rematch
- A1-0795 — Use Option.when
- A1-0797 — Fold optional goalId into successful planId list or filtered plan IDs
- A1-0810 — Map optional getByPortfolioId directly into optional response
- A1-0814 — strs already Seq; no toSeq needed
- A1-0890 — Convert toList after flatMap
- A1-0947 — Explain drop(1) in monthly update
- A1-0951 — Avoid sorting twice when generateMonthlyChangesFromCombinedMonthlyReturns sorts
- A1-0953 — Require currentIndex strictly above startIndex for overflow pagination
- A1-1011 — Use request.targetWeights.keySet
- A1-1049 — Return Option invalid only and flatMap; discard valid reconciliation results
- A1-1051 — Pattern-match tuple instead of _2
- A1-1059 — Collect only displayTags
- A1-1067 — Count errors rather than collect
- A1-1073 — Merge by explicit keyExtractor with distinctBy or supplied merge logic
- A1-1082 — distinctBy documentation does not promise order preservation
- A1-1102 — Materialize toSeq or toList before returning mutable-map-derived view
- A1-1118 — Use map values without filter or toList
- A1-1131 — Use groupMap then collect
- A1-1134 — Keep compliance collection as List or Set
- A1-1135 — Use Option.when
- A1-1139 — Use collect instead of filter then map
- A1-1145 — Reuse fetched source goals for customer entrypoint and key names by goalId
- A1-1147 — After contains check getOrElse unnecessary
- A1-1157 — Group acknowledgement plans by customerId first
- A1-1159 — Validate one grouped customer rather than traverse every plan again
- A1-1253 — Use groupMapReduce for variant grouping
- A1-1278 — Use exists
- A1-1343 — Search RPC tasks by tenantId and later goalId/planId
- A1-1348 — Use Set for RPC identifiers
- A1-1384 — Unapply totalFee totalBufferedFeeAmount unchargedFees directly
- A1-1412 — FilterNot hasCpfSaAccount then map investor type and empty fallback
- A1-1426 — Only top25Holdings switched to takeTopKBy
- A1-1478 — Optional broker rebate lookups require flatMap and minOption
- A1-1483 — flatMap optional broker ratios then minOption and fallback
- A1-1484 — Inline runFold merges instruments distinctBy id, goal-type unions, investor-type union
- A1-1485 — Apply same funding-source merge improvement here
- A1-1500 — Convert toList at intended point
- A1-1547 — Use optionA.orElse(optionB) rather than wrapping getOrElse in Some
- A1-1568 — Sort offerings by displayOrder
- A1-1572 — span daily NAV by not-after start; retain last prior plus later entries
- A1-1574 — No maxByOption because ordering already assumed
- A1-1576 — Resolve optional inception using filter/map/getOrElse or fold, not get
- A1-1583 — Use anonymous parameter for addDerivedTagsV2 mapping
- A1-1630 — Use mapValues or groupMap
- A1-1662 — Use Option.when
- A1-1667 — Pass merged instead of already evaluated accumulator
- A1-1684 — Prefer checking accumulator first for early stitch termination
- A1-1712 — Use Option.when for CPF/SRS detail
- A1-1816 — Portfolio cache unnecessary toList
- A1-1840 — Use forall rather than validated Option.get
- A1-1860 — Filter sorted return index then head; empty range returns empty
- A1-1876 — Filter before DTO except investorType
- A1-1879 — Take head before converting all
- A1-1898 — Filter then maxByOption
- A1-1907 — Deduplicate MStar documents by documentId
- A1-1921 — Use forall
- A1-1933 — Unapply recurring frequency/amount tuple instead of _1 _2
- A1-1954 — Expression now simple if/else
- A1-2010 — Do not collect large planId list without need
- A1-2011 — Keep count only instead of full UUID list
- A1-2018 — Avoid Option.get; filter fold/getOrElse
- A1-2019 — Mapping withFilter produces List[WithFilter] rather than instrument list
- A1-2054 — Group RPC by plan and maxBy createdAt status directly into map
- A1-2129 — Prepend if ordering irrelevant; append slower
- A1-2296 — Pattern-match only context when rest same
- A1-2308 — Set tags collapse duplicated sector/asset labels before display List
- A1-2316 — FE-added two filters should sort last
- A1-2317 — Static FilterOrder lookup; dummy-section helper may unnecessary
- A1-2320 — Regional filterOrder alone controls allowed sections then extra skips
- A1-2348 — Use collect
- A1-2356 — Use exists account type instead of map-toSet
- A1-2362 — Use collect instead of filter/map
- A1-2365 — Only project nonempty goal when requested; filter empty monthlyResults
- A1-2405 — Map optional fee config and Option.when positive applied fee instead of get
- A1-2421 — Build optional AI-only mismatch error then flatten blocked-error list
- A1-2434 — Use statuses.forall(isTerminal) rather than confusing transfer helper
- A1-2435 — No distinct needed before forall
- A1-2446 — Avoid eager return via Nil/head pattern then optional counterparty match
- A1-2453 — Use map.get(key).contains
- A2-0002 — PortfolioUnderlyingManager: This is existing code, but let’s double check if we should filter only active here
- A2-0003 — PortfolioUnderlyingManager: Let’s use sort \+ reverse instead
- A2-0007 — HkPortfolioMetricsManager: AnnualYield is fetched and calculated based on instrument data, regardless of goalType. I think we don’t need to this extra filter
- A2-0026 — BackfillPlanProfileTenantIdCmdHandler: Let’s also return without events if same tenantId already exists. Then we won’t have duplicated events, as the subscriber might process a ...
- A2-0061 — TagTransactionAdvisoryClassification: L32 returns tuple of `(transactionId, customerId)`
- A2-0066 — HkTradingSimulationHelper: Actually Set.map will return a new set…. so it’s better to use `errors.exists(_.category == SuitabilityBreach)` instead
- A2-0078 — FixV3DividendsTransactions: Why don’t we add more filter here, to reduce the payload size? Also maybe groupBy customerId so that we don’t repeat the query again?
- A2-0080 — ExportFeeEstimation: Are we using only 1st customerId and 1st broker that matches tradingAccount? Need to groupBy customer first right?
- A2-0093 — InstrumentTransferHelper: Existing code would match by specified brokerAccountId too.
- A2-0111 — B2BProductHelpers: Do we need Option here? Maybe just use `task.payload.exists` above and return boolean here
- A2-0140 — InvestOnceCmdHandler: Nit: `maybeInvestmentRequestCreationApprovedEvt.toList` is sufficient
- A2-0143 — StopRecurringInvestmentScheduleCmdHandler: Same here and the cmd handler below. Can use Option#toList
- A2-0275 — FeeInstructionHelper: Since it’s a little bit tricky, maybe put a comment here explaining that we want `inclusive maxBefore` which is not available. Author of scala TreeMap seem...
- A2-0282 — PlanFeeInstructionEntity: The entity state is default with empty fee instructions, it means the plan always exists, just without any data. Modelling it this way means you can’t ...
- A2-0300 — BackfillPlanInvestmentCmdHandler: I think this could be confusing to read, e.g. what if existing but doesn’t match the resolve? Well it cannot be, due to how we resolve. So mayb...
- A2-0314 — BaseServiceLogicImpl: No need this filter
- A2-0365 — GoalSupportingDataJdbcDbHandler: I suppose this would return 0, if row already exists? Do we log error or something cuz we don’t expect that to happen?
- A2-0385 — BaseAdvisoryServiceE4s: If In is not tuple, then we don’t need to define `handle` or `toTupled`
- A2-0400 — SgFundDetailsManager: Let’s structure these as
- A2-0418 — CorporateProductRuleService: [person] pointed out to me that we already checked this below
- A2-0438 — DocumentServiceE4s: We only need to create these `handle` methods if In is tuple
- A2-0440 — InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs: This won’t work cuz we already filter out invalid data on the way out from domain model to DTO. I think we just need to use what...
- A2-0514 — BaseBffRouteDefinitionsE4s: Should be `lines.headOption.map(_ => lines.flatten.mkString("\n"))`
- A2-0544 — HkChargeCommunicationProjection: This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.
- A2-0549 — MarketDataUploader: Blind me didn’t realize this method `retrievePrices` already exists. The `getPricesToUpdate` sorts again anyway
- A2-0593 — MstarDailyPerformance: This should be the only logic change. If ccy mismatched, we shouldn’t really fallback to headOption
- A2-0602 — HkFundSmartManagerV3: So we block returning AI-only collections, but do not filter out AI data for instrument? What’s the expectation from Product?
- A2-0640 — BaseAdvisoryServiceE4s: Actually, would it be easier if we just change `Endpoint` to `EndpointDef`, without touching the jsonRequest and jsonResponse? Anyway, we won’t be able t...
- A2-0673 — GoalModifyBehaviourHelpers: throw if using map \(`_ = ...`\), or `Future.failed` if using flatmap \(`_ <- ...`\)
- A2-0675 — ServiceLogicImpl: Use collect
- A2-0677 — ServiceLogicImpl: This method doesnt need to know about TAA, it should just load given set of instrumentIds \(and at most additionally marketdataCcy\)
- A2-0710 — PortfolioMonthlyChangesHelper: Use collect
- A2-0730 — InstrumentMonthlyChangesJdbcRepository: Move filter up, and select specific columns
- A2-0732 — ServiceLogicImpl: Maybe drop all these filter out of BENCHMARK
- A2-0746 — BaseAdvisoryServiceE4s: Oh it doesn’t work if you don’t make this inner tuple? Or you do it for clarity?
- A2-0781 — SgRecommendedInvestmentManager: After the month filter, we don’t need to worry about it anymore
- A2-0782 — SgRecommendedInvestmentManager: Let’s return Set in `getLastThreeMonths` so it’s a bit faster to filter here
- A2-0784 — SgRecommendedInvestmentManager: Can we change to this style instead
- A2-0794 — ServiceLogicImpl: Just extract this filter and map as well? Also use collect instead
- A2-0821 — ProductPortfolioRepository: Maybe we can keep this method generic, but only handle for CoreEnhanced for now…
- A2-0858 — InstrumentMarketDataEntity: If it’s None, `exists` will return false and we won’t fail
- A2-0869 — PerformanceCalculator: Same same only, but I think structuring the logic this way makes it easier for me to visualize
- A2-0883 — StatementDataGenerator: Let’s filter for dpmGoals outside, regardless of `ignoreTimeForDebug`
- A2-0952 — BaseRedemptionCommunicationV2Projection: Can import `TraversableOnceUtils` and use it like this
- A2-0956 — portfolio: I would think if a benchmark portfolio has missing performance, we should just filter it out, instead of sending with None portfolioStats. So let’s make this required
- A2-0957 — package: Either that or we keep it Set\[UUID\] here, and sort \(say by stockRatio and then by name\) in offerings response
- A2-1030 — CorporateProfile: Let’s just filter for exclusive, then check
- A2-1040 — MonthlyChangeGenerator: [person] maybe just a bit cleaner to change this condition
- A2-1041 — MonthlyChangeGenerator: Yea we can just find instruments with empty monthly changes, if exists then log them and return empty for whole TAA. If one is empty, we wont be able to ...
- A2-1059 — PageDataGenerator: Actually we have too many region pattern matching in this method. Maybe consolidate it a bit
- A2-1116 — RecurringInvestmentProcessor: You can import OptionUtils and use onNone and make this a bit nicer… also better to extract schedule here, so that we don’t have to blindly call ge...
- A2-1182 — FlagshipDpmSchemaV1: Can use `exists`
- A2-1197 — InstrumentExportScheduler: You can just batch it here
- A2-1272 — AdvisedPortfolioHelper: Maybe `exists` instead? We dont need to log if not provided?
- A2-1297 — ValidationHelpers: Maybe just make this `maybeAmount`
- A2-1360 — MarketDataUploader: I suppose it’s also good to log for prices we have in our DB but not in MStar.
- A2-1366 — MarketDataUploader: Nit: no need to start a Source from beginning I think
- A2-1375 — MarketDataUploader: I think this cassandra table already have priceDate in its clustering key. We should be able to add a method in repository to filter in database itself
- A2-1378 — MarketDataUploader: We can return `InstrumentPriceReconResult` from here right? In general, avoid using tuple to avoid confusion/mistake unless it’s very isolated and simple
- A2-1421 — PortfolioSuitabilityAnalysisLogic: Yeah I think we can pass the isDpm flag there and we can reduce a lot of tuple returning here…
- A2-1439 — BaseServiceLogicImpl: Yes all the usage of this API mostly just check if plan exists.. and in general, if you query by not entity-id, you should expect EC regardless
- A2-1455 — BaseServiceLogicImpl: Nits: maybe filter out inactive before we append plans
- A2-1493 — FlowUtils: ```
- A2-1517 — HkFundSmartManager: Maybe reuse `InstrumentInfoDto.canBePartOfMultiFundPortfolio` for this instrument count check.. And we simply use `instruments.exists(_.isIlliquidAlts)` for ...
- A2-1531 — FundSmartHelper: This reads a bit weird, cuz it’s all logic within this trait. It’s the one deciding which fee to fetch per `request.isSingleFund`, then it validates against its...
- A2-1547 — HkFundSmartInstrumentBuilder: We’re adding funding source tag for HK too? Today we only have HKD Cash or USD Cash, which the ccy filter should be sufficient?
- A2-1644 — UpdateTemplateDisplayName: Filter for empty displayName instead?
- A2-1654 — HkAdvisoryLevelClassificationLogic: exists instead? Today we don’t allow mixing illiquid alts with other funds, but I suppose just one would make it execution-only mode?
- A2-1659 — HkAdvisoryLevelClassificationLogic: So exists is correct behaviour, not forall right?
- A2-1661 — HkAdvisoryLevelClassificationLogic: Check advisory logic we built for Alts for reference. I think we have been using exists so far \(and sometimes, additionally check single ins...
- A2-1701 — BaseRedemptionCommunicationV2Projection: Ah we already filter for this in the main handle method
- A2-1721 — models: Maybe sort in here so we don’t need to care if groupBy changes ordering or not
- A2-1725 — InvestmentRequestJdbcRepository: Hmm status filter is behaving same as before. I just move the createdAt check to logic layer, cuz we need to check cutOffDate first.
- A2-1729 — InstrumentPerformanceCache: Maybe we can use collect here… sth like this
- A2-1790 — NewWealthDataFetcher: Nit: `Some(fundDetails.FundManager).filter(_.nonEmpty)`
- A3-0010 — ServiceLogicImpl.scala: Does this look better? ``` instrumentId .map(marketDataUploader.syncInstrumentMstarData) .getOrElse { // run in background marketDataUploader.safeSync
- A3-0019 — ServiceLogicImplV2.scala: can extract for both ``` .map(it => it.map(InstrumentV1.toDto)) ```
- A3-0022 — ServiceLogicImplV2.scala: Or maybe just pass the Option\[Boolean\] to the other methods so we don’t need to resolve these booleans
- A3-0032 — DailyMvAuditEntry array_agg/customerId optimization deferred over Slick GROUP BY issues
- A3-0037 — No daily fee for a plan means remove: retain every planId and relevant MVs
- A3-0040 — BaseServiceLogicImpl.scala: Good catch. Let me just handle empty MV inside batchUpsert then
- A3-0072 — InstrumentDataUpdateManagerV2.scala: no need for comprehend if just single future
- A3-0076 — InstrumentRetrievalManagerV2.scala: This should check for contain instead? Tmr we might add some other restrictions that applicable on top of offline rule right?
- A3-0077 — InstrumentV2EntityTest.scala: add a test case to cover that we merge/override existing map correctly with data from request for these update idMap/urlMap
- A3-0081 — InstrumentCommandsHandler.scala: Looks like we can use `i` here?
- A3-0083 — TransactionV2AccountSerializerRegistry.scala: Don’t var if you can
- A3-0084 — TransactionV2AccountSerializerRegistry.scala: you have to update the field using \+\+ but still you don’t need to reassign to existing val?
- A3-0097 — TransactionTypes.scala: Can we not use this style.. it’s very easy to make mistake. Just do: ``` case Some(settledOrder) => (Some(settledOrder.settledUnits), Some(settledUnit
- A3-0099 — Settled orders without isAssumed: collect/max date, zone start-of-day and confirmedAt fallback
- A3-0104 — Scala2.13 maxByOption unavailable here: import TraversableOnceUtils
- A3-0124 — ServiceLogicImpl.scala: We have utils in OptionUtils so this can be written as ``` rpcCmsWebflowIdJdbcRepository .find(portfolioId, effectiveDate) .map(_.map { entry => RpcCm
- A3-0125 — ServiceLogicImpl.scala: Same here, you don’t need to match. Can extract to reuse same toDto method as well ``` rpcCmsWebflowIdJdbcRepository .findByItemId(itemId) .map(_.map(
- A3-0162 — models.scala: You can use the util in MapJsonFormat ``` implicit private val brokerRatioMapFormat: Format[Map[Broker, BigDecimal]] = new MapJsonFormat.EnumMap(Broke
- A3-0172 — InstrumentV2-to-V1 mapping: Either instead of exception-based conditional flow
- A3-0174 — models.scala: Should this be a List?
- A3-0202 — RedemptionTransactionV2Transformer.scala: You can write it as ``` transaction.settledAt.orElse(redemptionData.timestamps.completedAt).getOrElse(throw ...) ``` Is same same but I think it looks
- A3-0203 — TransactionServiceImpl.scala: `accountType.map(TradingAccountType.withName)` should work?
- A3-0225 — UUID+CustomerStatus cache estimate32MB/1mio versus larger plan-market-value map
- A3-0239 — BasePlanRecurringInvestmentScheduleManager.scala: Can just use `schedule` cuz we already validate here?
- A3-0245 — PlanCommunicationV2EventProcessor.scala: Why we need to `.map(_ => Done)` again?
- A3-0255 — RecurringInvestmentScheduleJdbcEventProcessor.scala: You’ll need for-comprehend block
- A3-0266 — PlanRecurringInvestmentScheduleDbItem.scala: Isn’t it clearer if we don’t pair these in a single patten match ``` config.flatMap { case SpecificEndDate(userEndDate) => Some(userEndDate) case _: O
- A3-0272 — scheduledInvestmentId flatMap, matching startingFrom/interval, max sequence+1
- A3-0338 — TransactionTypes.scala: t.taxDetails is already Option no?
- A3-0341 — RedemptionRequestTopicSubscriberV2.scala: pattern match on `request.feeChargeDetails`, extract the mapping methods so it’s easier to follow
- A3-0343 — RedemptionRequestTopicSubscriberV2.scala: Do we need this filter? Just default to 0? ``` r.confirmedAmount.getOrElse(r.assumedAmount.getOrElse(r.orderAmount.getOrElse(BigDecimal(0)))) ```
- A3-0352 — RedemptionRequestTopicSubscriberV2.scala: Can we pattern match outside and break this into 2 methods
- A3-0353 — RedemptionRequestTopicSubscriberV2.scala: Can just return, no need to assign here. In fact, assigning here create chance for the bug last time, cuz the underlying type is lost via type erasure
- A3-0354 — RedemptionRequestTopicSubscriberV2.scala: Does this look better? ``` val amountChargedBySell = request.orders .map(o => o.confirmedAmount.getOrElse(o.assumedAmount.getOrElse(o.orderAmount.getO
- A3-0355 — RedemptionRequestTopicSubscriberV2.scala: Better to maintain parity ``` val amountChargedBySell = ... val amountChargedByCash = ... (Some(amountChargedBySell), Some(amountChargedByCash)) ```
- A3-0356 — RedemptionRequestTopicSubscriberV2.scala: ``` request.cashReservations.map(_.reservedAmount).sum ```
- A3-0360 — RedemptionRequestTopicSubscriberV2.scala: Actually there’s a better method for this: ``` settledAmount.orElse(assumedAmount).getOrElse(request.requestedAmount) ```
- A3-0361 — RedemptionRequestTopicSubscriberV2.scala: Same can use orElse here
- A3-0370 — DistributionPreferenceDecider.scala: `.exists(_.isPrimary)` should be enough
- A3-0379 — SgInvestmentServiceImpl.scala: can be written as below so that we call derive once ``` .map { schedule => (schedule, schedule.derive(...)) } .collect { case (schedule, missingDates)
- A3-0380 — SgInvestmentServiceImpl.scala: Haha should have used `missingDates` here, but it’s alright
- A3-0384 — InvestmentScheduleActivePeriod.scala: You can use the common method ``` Iterator.iterate(startingDate)(_.plus(CashflowInterval.toTemporalAmount(recurringInterval))) ```
- A3-0401 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: the better syntax would be ``` _ <- investmentPlan.recurringInvestmentSchedule match { case Some(schedule) => repository.upsert(...) case None => Futu
- A3-0408 — SgServiceLogicImpl.scala: Clearer to use `planMarketValues.values.map(_.totalMarketValue)` I think
- A3-0409 — SgServiceLogicImpl.scala: Should we calculate MV grouped by planId, then use it for the total in step 1? So we don’t need to repeat that logic here
- A3-0410 — SgServiceLogicImpl.scala: So this step is basically split the planMV by TAA for each plan right? See if you can reuse `Calculator#distributeAmountByWeight` in silver-commons
- A3-0411 — SgServiceLogicImpl.scala: And this step is to split MV per instrument back into weight. See if you can see `Calculator#weightedRatios`
- A3-0412 — SgServiceLogicImpl.scala: Should we just use `ModelPortfolioRiskTarget.values`?
- A3-0420 — Risk-target performance example uses mapAsync2 over risks and mapAsync1 over plans
- A3-0421 — AdHocTaaHelpers.scala: Seems not used… but otherwise, `planMarketValues.size` is good
- A3-0422 — AdHocTaaHelpers.scala: Use Calculator.weightedRatio here too
- A3-0423 — Combined TAA weights use assumedMV+pending investment; equal weights when all zero
- A3-0430 — BaseServiceLogicImpl.scala: A bit redundant to check this as `resolveNewTaasFromProvidedParam` requires the planIds set to match
- A3-0435 — RebalanceRequestJdbcRepositoryImpl.scala: ``` filterOpt(planId)(_.planId === _) ``` Does this work?
- A3-0455 — WithdrawalTopicSubscriber.scala: Also, query by planId if exists would give fewer results, so let’s match that first
- A3-0490 — RebalanceMsgLogicImpl.scala: just add another method similar to `calculateRequestedAmount` ``` def calculateSettledAmount(orders: List[OrderV2]): BigDecimal = { val orderAmounts =
- A3-0492 — RebalanceMsgLogicImpl.scala: change for all the places that cast `SettledOrder` ?
- A3-0494 — RebalanceMsgLogicImpl.scala: collect = filter \+ map… here we don’t care about PendingOrder, so we can simply drop it
- A3-0556 — CustomerPIMatcher.scala: change this method a bit: ``` def getPIInstrumentsForNonPI(customerId: UUID, instruments: Seq[InstrumentProfile]): Future[Set[String]] ``` Makes the c
- A3-0557 — PortfolioSuitabilityAnalysisLogic.scala: How about we create a local scaffiene cache for instrument performance in this method \(i.e. invalidate all after we are done with all the `instrument
- A3-0569 — CustomerAltsFeesCalculator.scala: change these 2 methods to accept `PlanProfile` / `PlanChargeContext` ``` isRelevantPlan(planProfile: PlanProfile): Boolean isRelevantPlan(planChargeCo
- A3-0601 — ServiceLogicImpl.scala: Can we extract some var here, and also reformat this code block… idk what’s going with all these wonky indentation \+ brackets here…
- A3-0611 — CustomerFeeEstimator.scala: we can pattern match to avoid calling Option.get ``` (maybeYear, maybeQuarter) match { case (Some(year), Some(quarter)) => Some(...) case _ => None } 
- A3-0687 — TransactionFxConverter.scala: Not good hide var like this \(e.g `maybeConvertedSettlementDetail` was a fut, and then reassigned as an Option How about just ``` maybeConvertedSettle
- A3-0697 — package.scala: Both are already Option, so no we don’t need
- A3-0702 — PortfolioVersionUpgradeRebalanceRequestsGenerator.scala: Good point. Added the runFold back
- A3-0705 — PreRpcValidation.scala: Ah yeah I just need to sort based on something so that the ordering is same when I run multiple times
- A3-0712 — PlanTimeseriesTopicSubscriber.scala: How about ``` _ <- maybeLatestStoredMV match { case Some(latestStoredMV) if latestStoredMV.updatedAt.isAfter(msg.updatedAt) => logger.info("Skipping..
- A3-0720 — PlanTimeseriesTopicSubscriber.scala: just keep the old check in the patten matching above. Then the method isValid below doesn’t need that check anymore, and purely checking the MV data
- A3-0723 — AssumeTransactionSettlementCmdHandler.scala: that amount vs unit check might be specific to rebalance sell order. Based on new logic, this condition `areAllOrdersUnAssumedRebalanceSell` should re
- A3-0758 — Transaction FX conversion Futures: bounded Source.mapAsync2 proposed
- A3-0772 — TransactionFxConverter.scala: distinct the pairs before loading?
- A3-0774 — FxRateHelper.scala: ``` fxRateCache .getIfPresent(fxId) .map(Future.successful) .getOrElse(loadCacheAndFind(fxId)) ``` Try to use Option more idiomatically
- A3-0776 — FxRateHelper.scala: create a TreeMap keyed by priceDate first, then just lookup here? Otherwise we traverse the Seq everytime
- A3-0787 — SgServiceLogicImpl.scala: If you want to log when we generate for all, then should check both `includeCustomers` and `excludeCustomers` to be empty
- A3-0795 — SftpRunner.scala: This can be `val` now
- A3-0796 — SftpRunner.scala: No need to assign to var `channelSftp` anymore. Can just return
- A3-0809 — AdvisedPortfolioOfferingsManager.scala: Hmm I don’t want this logic to be aware that flagship portfolios are available in Cash/CPF/SRS. Can we find allowed trading accounts by using superset
- A3-0810 — MaaPageLoaderV2.scala: We handled the performance fetch error in advisory, so it’s possible to have empty performance here. `offering.performance.get` is not safe. We don’t 
- A3-0813 — InvestmentCommunicationV2EventProcessor.scala: No need to extract `instruments` here right? We can just traverse and map from sorted allocationTargets directly in L155?
- A3-0814 — InvestmentCommunicationV2EventProcessor.scala: Why find again here? Isn’t it exactly `allocationTargetDto` now?
- A3-0824 — InvestmentPlanEventProcessor.scala: also `.map(_.isValid)` here?
- A3-0844 — HkNotificationManager.scala: Does it work with just `case Some(tuple) => tuple`?
- A3-0850 — NotificationManager.scala: Looks like you don’t need for-comprehend block here
- A3-0853 — NotificationManager.scala: Can we just return `Some(customerData)` ?
- A3-0854 — NotificationManager.scala: Then you can `.collect { case Some(customerData) => customerData }` to flatten the flow
- A3-0903 — CraManager.scala: Can we extract filters like this to a named method so that it’s easier to follow?
- A3-0914 — CraManager.scala: forall returns true if Option is empty… so if somehow, profile is missing, we will always trigger? Should we use exists instead?
- A3-0915 — Missing profile readside: warn and force inclusion, while expired stays until retake
- A3-0947 — PassportValidatorHelper.scala: Wanna extract this `customer.officialIdentificationDto.fold`?
- A3-0968 — ServiceLogicImpl.scala: the scala idiomatic way would be ```scala configDetails.exists(cd => cd.fundSmartCma || cd.fundSmartGwa) ```
- A3-0970 — NewWealthDataFetcher.scala: How about this? ```scala fundList.map(fundDetail => fundDetail.ISIN -> fundDetail).toMap ```
- A3-0972 — ServiceLogicImpl.scala: we don’t actually need this for comprehend block here if it’s just one future
- A3-0987 — InvestmentCommunicationV2EventProcessor.scala: at this point, we already know assumedAt is defined… so this fallback logic is redundant and potentially confusing? same for the below confirmed metho
- A3-0990 — StatementDataGenerator.scala: What if `settledOrders` is now empty? Should we follow the logic in else clause which uses `transaction.settledDate`?
- A3-1011 — NewWealthDataUploader.scala: Not sure if we still need to group here
- A3-1027 — RedeemOnceEdgeLogic.scala: We can remove this match now
- A3-1044 — ServiceLogicImpl.scala: can write this as below? ``` _.tags .flatMap(allPossibleTagsMap.get) .flatMap(tag => getDisplaySectionOrdering(tag.section).map((tag.label, _))) .toLi
- A3-1052 — TransactionEntity.scala: maybe easier to read if we match this first? ``` case t: InvestmentTransaction if transaction.statusDetails.transactionStatus == TransactionStatus.CRE
- A3-1059 — CustomerAdvisoryProfileTopicSubscriber.scala: You can use Option#fold or Option#getOrElse. But yeah, most of methods in Option are following that pattern `if isEmpty foo else bar`
- A3-1060 — CustomerAdvisoryProfileTopicSubscriber.scala: `persistedAcks.craCat2Ack.exists(_.isBefore())`
- A3-1061 — CraCategoryMatcher.scala: It’s better to match using type if we don’t care about underlying fields ``` case _: VulnerableCustomerProfileDto ``` Here the Dto has only 1 field, s
- A3-1062 — CraCategoryMatcher.scala: You can match using ``` case NonVulnerableCustomerProfileDto(_, RiskProfileStatus.Expired, _, _) ```
- A3-1063 — StatementDataGenerator.scala: Should we sort the pending transactions here too, to avoid unnecessary reprinting
- A3-1096 — BaseServiceLogicImpl.scala: You can just use `=` if not returning a future.. It’s equivalent to `Future#map`
- A3-1097 — BaseServiceLogicImpl.scala: There’s `mapValues` too
- A3-1098 — BaseServiceLogicImpl.scala: We can fold on map too
- A3-1110 — ModifyPlanAcknowledgementsLogic.scala: Don’t need for-comprehension block if you have only one future
- A3-1111 — ModifyPlanAcknowledgementsLogic.scala: Hmm why need to pair these? Maybe use the usual trick with List\[Option\].flatten?
- A3-1124 — PI-only predicate is contains(PI) AND not contains(Retail)
- A3-1125 — InstrumentHelper.scala: Also can we move assign that as a field in the for block?
- A3-1127 — InstrumentHelper.scala: This flag should be isPiOnlyInstrument I think. And let’s check using contains PI and not contains Retail, so that if instrument has more investor typ
- A3-1136 — EdgeQueryTradingRestrictionLogic.scala: we want non-inactive. There is `LiveGoalStatusSet`
- A3-1140 — EdgeQueryTradingRestrictionLogic.scala: This is a function so no need lazy?
- A3-1144 — EdgeQueryTradingRestrictionLogic.scala: There’s a `OptionUtils` , so we can write `Option.when(condition)(value)`
- A3-1148 — EdgeQueryTradingRestrictionLogic.scala: It’s internal impl of this class to provide the goal map. Can just use `goalIdMap(plan.goalId)` directly I think
- A3-1151 — EdgeQueryTradingRestrictionLogic.scala: Or don’t need to check and just call `goalIdMap(plan.goalId)` directly :stuck_out_tongue:
- A3-1171 — BaseServiceLogicImpl.scala: Hmmm the fields are Option but in the logic below, we filter for isDefined only..
- A3-1172 — BaseServiceLogicImpl.scala: Something like this? Not sure how to handle 2 options… ``` ipDto => { ipDto.commonPeriodPerformanceMetrics .flatMap( metric => if (metric.annualisedPe
- A3-1173 — SgServiceLogicImpl.scala: Need `toList` meh?
- A3-1209 — TradingRestrictionLogic.scala: Minor: maybe we can write this as ``` s.craCat2Ack.map(_ => CraCat2Ack) s.recurringInvestmentAck.map(_ => RecurringTransactionAck).filter(_ => request
- A3-1221 — MarketDataUploader.scala: Yeah, I can’t see the benefit of this being in separate for-comprehension block
- A3-1223 — InstrumentManager.scala: Wanna take this chance to refactor this into for-comprehension instead of async await?
- A3-1232 — CraManagerTest.scala: Use `None`
- A3-1240 — HkServiceLogicMockUtils.scala: Ok for test code, but a NIT still: it’s easier to follow if we assign val for `craResponse` based on the logic. I inline it previously because there w
- A3-1255 — HkInvestmentTopicSubscriber.scala: not worry about these for now. But you will need to provide a case for them, otherwise we would get a `MatchError`
- A3-1260 — HkInvestmentTopicSubscriber.scala: Maybe use `Option#fold`?
- A3-1263 — HkInvestmentTopicSubscriber.scala: Return Option here instead of null..
- A3-1265 — HkInvestmentTopicSubscriber.scala: Just notice this :rofl: It’s `Some` vs `None`, but yeah `Option.apply` vs `Option.empty` works too, just looks weird
- A3-1289 — InvestmentValueCalculator.scala: Oh you’re talking about the `#map` honouring the characteristic of the original collection.. well once I know it, it becomes normal to me :rofl: But y
- A3-1303 — CustomerTradingEarmarkManagerEntity.scala: How about we refactor this a bit? Using pattern match on the find? ```scala state.buyEarmarks.find(_.id == cmd.buyEarmark.id) match { case Some(existi
- A3-1313 — CustomerTradingEarmarkManagerEntity.scala: Sorry I just notice this. We don’t actually care about ordering, so maybe let’s prepend instead of append, to some some peanut cost
- A3-1315 — CustomerTradingEarmarkManagerEntity.scala: In scala, we can use ==
- A3-1327 — HkServiceLogicImpl.scala: Hmm `Map[InstrumentProfile, BigDecimal]` already can be mapped to instrumentWeights?
- A3-1339 — package.scala: This needs to be a collection, cuz we will need multiple fxRates \(per date, per ccypair\)
- A3-1377 — PortfolioMarketDataEntity.scala: Use `updatedPriceMap` below and check forAll\(contain\) ?
- A3-1381 — distributeAmountByWeight used to distribute weights with TotalWeights1
- A3-1389 — PlanUpsertSummaryBehaviour.scala: let’s do that. At least we can see the decision to calculate projection and to call maybeProjection.get in one place
- A3-1390 — PlanUpsertSummaryBehaviour.scala: Ah I mean, both of these at same one method scope \(aka product specific method\) * `calculateProjection = true` * `portfolioProjection = baseSummary.
- A3-1404 — package.scala: use `Either`?
- A3-1410 — MasApiService.scala: use `(Ordering[Long].reverse)` would be clearer to me. This `* -1` is not always very visible
- A3-1413 — Cross-FX old intersection behavior versus new all-base-rates-from-minDate calculation
- R-3316 — It doesn’t matter much, but I don’t want to change the ordering of submitted answers…
- R-3324 — Maybe just `Option.map().getOrElse()` is sufficient here?
- R-3325 — Same for `employmentDetails` below
- R-3398 — We can use exists\(predicate\) again with configDetails right?
- R-3406 — Unit is like void, hence everything it mappable to Unit. And by extension, every Future\[Blah\] to mappable to Future\[Unit\]. We normally return Future\[a
- R-3447 — Looks like this customerSource can be just customerId instead of full DTO?
- R-3448 — So we have unlisted SIP and listed SIP \(or just SIP\)? Should we name this method and its filter `isUnlistedSip`?
- R-3449 — This already returns `Future[Done]` so we don’t need this for comprehend at all? Also for timing, would you like to give `TimeUtils.TimedLogger` a try? You
- R-3489 — Would `filter().result.headOption` be enough?
- R-3490 — take(1) translates to LIMIT 1, correcting the earlier result.headOption suggestion
- R-3505 — We have 2 somewhat generic helper functions for now ``` def findProductPortfolio(advisoryTag: AdvisoryTag, targetStockRatio: BigDecimal, tradingAccountType
- R-3508 — I prefer scaladoc over comments. But one could argue you can name things better to explain yourself. For example, ```scala private def getDividendTransacti
- R-3558 — Portfolio stats exact-ID lookup and filter lookup both produce a List response
- R-3569 — Existing monthly-change sort is found; originalMonthlyChanges input still questioned
- R-3571 — Can we rely on fxRate to take care of inverting the rate already? e.g. it’s EURUSD but USDJPY
- R-3572 — Nit: Can we rename these two as `prevMonthConvertedNav` and `currMonthConvertedNav`?
- R-3574 — Maybe we should sort here, instead of trusting the caller
- R-3583 — I think we should make this method returns the instrumentIds only - and let its caller invoke instrumentService. It will make it simpler to write test too.
- R-3595 — I think I like iterator better :stuck_out_tongue:
- R-3610 — FX daily-price conversion separates missing prior rate from mapping outcome and uses HALF_EVEN scale 2

## Full source cases

## A1-0028 — RecurringInvestmentProcessor methods may not require List

**Source stance:** open-question

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; operation: [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need List in these methods?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:30 · comment 822095144 · PR 14066 · 2026-07-06

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (pr_title):**

> [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification

**Evidence:** anon-1.jsonl:30 · comment 822095144 · PR 14066 · 2026-07-06

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (hunk):**

> -        Future.successful(RecurringInvestmentScheduleResult(1, 0, 0, 0, 0, 1, 0, 0))
> +        Future.successful(Some(TradabilityApiFailed))
>      }
>    }
>  
>    private def validateComplianceRestriction(
>      investmentPlan: InvestmentPlanDto,
>      planCcyAdjustedRecurringAmount: PlanCcyAdjustedAmount,
> -    dateToUse: LocalDate,

## A1-0032 — Accumulate recurring planCount separately

**Source stance:** suggestion

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; operation: [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This looks hacky. Maybe just accumulate the `planCount` separately

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:34 · comment 822091771 · PR 14066 · 2026-07-06

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (pr_title):**

> [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification

**Evidence:** anon-1.jsonl:34 · comment 822091771 · PR 14066 · 2026-07-06

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (hunk):**

> +                s"Plans which are not tradable: [${result.notTradablePlanCount}]. " +
> +                s"Plans which have bank account issues: [${result.bankAccountInvalidPlanCount}]."
>              logger.warn(summaryMsg + warningMsg)
>              sendSlackNotification(summaryMsg + warningMsg + " :warning:", WARNING)
>            } else {

## A1-0051 — Use collectFirst consistently in recurring validation processing

**Source stance:** suggestion

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; operation: [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> maybe more consistent to use `collectFirst` as well?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:53 · comment 822673189 · PR 14066 · 2026-07-07

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (pr_title):**

> [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification

**Evidence:** anon-1.jsonl:53 · comment 822673189 · PR 14066 · 2026-07-07

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (hunk):**

> schedule = schedule,
> -        bankAccountError = bankAccountError
> +        bankAccountError = validationErrors.collectFirst { case BankAccountInvalid(error)              => error },
> +        complianceValidationResult = validationErrors.collectFirst { case ComplianceRestricted(result) => result },
> +        minTradingAmountNotMet = validationErrors.collectFirst { case NotTradable(breach) => breach }.getOrElse(false),
>        )
>        .recoverWith {
>          case ex =>
> -          logger.warn(

## A1-0055 — Use redistributeByCapacity for both optimizer cases

**Source stance:** suggestion

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala; operation: [INV-5732] feat(commons): Optimizer to support max per instrument and clamping; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Previous single-decrement logic need not remain

**Source-preserving request, proposal, or question:**

> I think we can just use `redistributeByCapacity` for both cases here, no need to retain previous logic of decreasing only one

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:57 · comment 822450910 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (pr_title):**

> [INV-5732] feat(commons): Optimizer to support max per instrument and clamping

## A1-0056 — Use deltasById.keySet instead of minsById.keySet where applicable

**Source stance:** suggestion

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala; operation: [INV-5732] feat(commons): Optimizer to support max per instrument and clamping; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Validation ensures the two match; deltas is clearer

**Source-preserving request, proposal, or question:**

> I think let’s change all the usage of `minsById.keySet` to `deltasById.keySet` where applicable. The two should match by the validation, but I think it would be clearer

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:58 · comment 822464826 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (pr_title):**

> [INV-5732] feat(commons): Optimizer to support max per instrument and clamping

## A1-0057 — Use deltasById instead of minsById in optimizer

**Source stance:** requested-change

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala; operation: [INV-5732] feat(commons): Optimizer to support max per instrument and clamping; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Change `minsById` to `deltasById`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:59 · comment 822465355 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (pr_title):**

> [INV-5732] feat(commons): Optimizer to support max per instrument and clamping

**Evidence:** anon-1.jsonl:59 · comment 822465355 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (hunk):**

> -    // Recursively solve for relaxed solution that only enforces the decided zeroed & positive ids
> -    // ignoring those variables that are not decided yet
> -    Some(innerSolveRelax(nodeInfo, Set.empty))
> +    val idsThatCanStillBePositive = deltasById.keySet -- nodeInfo.zeroedIds
> +    val maxReachableSum = idsThatCanStillBePositive.iterator.map(id => optionalMaxesById.getOrElse(id, targetSum)).sum
> +    if (maxReachableSum < targetSum) {
> +      // No solution if all values that can still be selected cannot reach targetSum even at their maximums.
> +      return None

## A1-0058 — Use positiveDeltasById.keySet for undecided IDs

**Source stance:** requested-change

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala; operation: [INV-5732] feat(commons): Optimizer to support max per instrument and clamping; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Change undecided to `positiveDeltasById.keySet`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:60 · comment 822465487 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (pr_title):**

> [INV-5732] feat(commons): Optimizer to support max per instrument and clamping

**Evidence:** anon-1.jsonl:60 · comment 822465487 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (hunk):**

> }
>        val naiveUnboundedValues = adjustToRequiredSum(rawNaiveUnboundedValues, targetSum)
>  
> -      constructFeasibleSolution(naiveUnboundedValues, zeroedIds = zeroedIds, undecided = minsById.keySet -- zeroedIds)
> +      constructFeasibleSolution(naiveUnboundedValues, zeroedIds = zeroedIds, undecided = positiveDeltasById.keySet)
>      } else {
>        None
>      }

## A1-0059 — Select minViolationToClamp via invalidMinIds.minBy(minViolationScores)

**Source stance:** suggestion

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala; operation: [INV-5732] feat(commons): Optimizer to support max per instrument and clamping; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ```scala
> val minViolationToClamp = invalidMinIds.minBy(minViolationScores)
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:61 · comment 822468116 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (pr_title):**

> [INV-5732] feat(commons): Optimizer to support max per instrument and clamping

**Evidence:** anon-1.jsonl:61 · comment 822468116 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (hunk):**

> +          // Limit mixed violations to two branches: the cheapest minimum clamp and the cheapest maximum clamp.
> +          // This keeps both possible clamp directions while avoiding a separate branch for every violating id.
> +          val minViolationScores = invalidMinIds.map(id => id -> squaredViolationGap(solution.values, id)).toMap
> +          val maxViolationScores = invalidMaxIds.map(id => id -> squaredViolationGap(solution.values, id)).toMap
> +          val minViolationToClamp = invalidMinIds.minBy(minViolationScores)
> +          val maxViolationToClamp = invalidMaxIds.minBy(maxViolationScores)
> +
> +          logger.info(
> +            s"""EuclideanDistanceWithSumConstraintOptimizer found mixed min/max bound violations.

## A1-0062 — Optimizer callee already calls iterator

**Source stance:** explanation

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala; operation: [INV-5732] feat(commons): Optimizer to support max per instrument and clamping; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> inside we already call call iterator

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:64 · comment 822451181 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (pr_title):**

> [INV-5732] feat(commons): Optimizer to support max per instrument and clamping

**Evidence:** anon-1.jsonl:64 · comment 822451181 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (hunk):**

> +    redistributeByCapacity(
> +      values = values,
> +      amount = amount,
> +      capacity = (id, value) => optionalMaxesById.get(id).map(_ - value).getOrElse(amount),
> +      adjust = _ + _
> +    )
> +  }
> +
> +  private def decreaseWithinLowerBounds(values: Map[Id, BigDecimal], amount: BigDecimal): Option[Map[Id, BigDecimal]] = {

## A1-0063 — Replace another optimizer minsById reference with deltasById

**Source stance:** requested-change

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala; operation: [INV-5732] feat(commons): Optimizer to support max per instrument and clamping; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Change `minsById` to `deltasById`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:65 · comment 822465220 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (pr_title):**

> [INV-5732] feat(commons): Optimizer to support max per instrument and clamping

**Evidence:** anon-1.jsonl:65 · comment 822465220 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (hunk):**

> * worse (higher) objective value
>      */
>    private def solveRelaxed(nodeInfo: NodeInfo[Id]): Option[Solution[Id]] = {
> -    val allIdsAreZeroed = nodeInfo.zeroedIds == minsById.keySet
> +    val allIdsAreZeroed = nodeInfo.zeroedIds == deltasById.keySet
>      if (allIdsAreZeroed) {
>        // Can't satisfy positive target sum constraint if all variables are zeroed
>        return None

## A1-0067 — Collect idsWithInvalidPositiveRange when max exists below min

**Source stance:** suggestion

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala; operation: [INV-5732] feat(commons): Optimizer to support max per instrument and clamping; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ```scala
> private val idsWithInvalidPositiveRange = minsById.collect {
>   case (id, min) if maxesById.get(id).exists(_ < min) => id
> }.toSet
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:69 · comment 822434986 · PR 14214 · 2026-07-07

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/EuclideanDistanceWithSumConstraintOptimizer.scala`

**Explicit source context (pr_title):**

> [INV-5732] feat(commons): Optimizer to support max per instrument and clamping

## A1-0079 — Move nonFundingValidationSubscriptionCombinations calculation to scheduler base

**Source stance:** suggestion

**Context:**

> component: broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala; operation: TT-8234 Instrument export process should account for CPF/SRS funding validation; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** SG and HK logic differ only in region and funding-validation combinations

**Source-preserving request, proposal, or question:**

> I think it’s better to move this to base. Logic is same between sg and hk - each of those defines the region & fundingValidationSubscriptionCombinations
> 
> ```
> protected[exportscheduler] lazy val nonFundingValidationSubscriptionCombinations: Set[(BrokerTransactionType, TradingAccountType)] =
>   BrokerTransactionType.SUBSCRIPTION_FILE_TRANSACTION_TYPES_BY_REGION(silverRegion).flatMap { transactionType =>
>     TradingAccountType.accountSetByRegion(silverRegion).map { tradingAccountType =>
>       (transactionType, tradingAccountType)
>     }
>   } -- fundingValidationSubscriptionCombinations
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:81 · comment 817497013 · PR 14154 · 2026-06-25

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala`

**Explicit source context (pr_title):**

> TT-8234 Instrument export process should account for CPF/SRS funding validation

## A1-0083 — grouped Iterator consumed by size before export scheduler logging

**Source stance:** observed-defect

**Context:**

> component: broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala; operation: TT-8234 Instrument export process should account for CPF/SRS funding validation; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Iterator traverses once; later logging emits nothing

**Source-preserving request, proposal, or question:**

> `grouped` returns Iterator \(can only traverse one time\), and calling size here will consume that already. The below won’t log anything

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:85 · comment 817504976 · PR 14154 · 2026-06-25

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala`

**Explicit source context (pr_title):**

> TT-8234 Instrument export process should account for CPF/SRS funding validation

## A1-0084 — Match ExcludeAllInstrumentCombinations symmetrically in either optional tuple position

**Source stance:** suggestion

**Context:**

> component: broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala; operation: TT-8234 Instrument export process should account for CPF/SRS funding validation; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> These 2 can be
> 
> ```scala
> case (Some(ExcludeAllInstrumentCombinations), _) =>
>   ExcludeAllInstrumentCombinations
> case (_, Some(ExcludeAllInstrumentCombinations)) =>
>   ExcludeAllInstrumentCombinations
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:86 · comment 817925722 · PR 14154 · 2026-06-25

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala`

**Explicit source context (pr_title):**

> TT-8234 Instrument export process should account for CPF/SRS funding validation

## A1-0101 — validateRequestForEtf accepts instrumentsMap.values already resolved from TAA

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala; operation: [INV-5597] feat(advisory): add validation for etf in advisory flow; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Also `instrumentsMap` is looked up from `taa` already, so this `validateRequestForEtf` just need to accept `instrumentsMap.values` for its validation logic

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:104 · comment 812150647 · PR 13764 · 2026-06-16

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Explicit source context (pr_title):**

> [INV-5597] feat(advisory): add validation for etf in advisory flow

## A1-0116 — Compact restriction-group filtering with collect and flatten

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala; operation: [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Good refactor :thumbsup:  I think can keep it a bit more compact
> 
> ```scala
> checkCustomerDetailsForSubscriptions(request) :: List(
>   CpfSrsRestriction(checkCpfSrsRestrictions),
>   FinancialSituationRestriction(checkCustomerFinancialSituationAckRestrictions),
>   SipRestriction(checkCustomerUnsuitableForSipAckRestrictions),
>   EtfRestriction(checkCustomerEtfAckRestrictions),
>   CarRestriction(checkCustomerCarAckRestrictions),
>   AiOnlyFundRestriction(checkAiOnlyFundRestrictions),
> ).collect {
>   case restrictionGroup if restrictionGroup.appliesTo(request) => restrictionGroup.buildChecks(request, accreditedInvestorStatus)
> }.flatten
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:119 · comment 814811367 · PR 13979 · 2026-06-19

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack

## A1-0122 — Do not split TradingRestrictionGroups cases when both are true

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/TradingRestrictionGroups.scala; operation: [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No need to split since both are true

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:125 · comment 814822571 · PR 13979 · 2026-06-19

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/TradingRestrictionGroups.scala`

**Explicit source context (pr_title):**

> [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack

**Evidence:** anon-1.jsonl:125 · comment 814822571 · PR 13979 · 2026-06-19

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/TradingRestrictionGroups.scala`

**Explicit source context (hunk):**

> +    case x: GoalCreationRestrictionRequest if x.isSaveEmptyGoal                 => false
> +    case _: GoalCreationRestrictionRequest                                      => true
> +    case _: PlanCreationRestrictionRequest                                      => true
> +    case _: PlanRecurringInvestmentUpsertRestrictionRequest                     => true
> +    case x: OneTimeInvestmentRestrictionRequest if x.transferRequestId.nonEmpty => true
> +    case _: OneTimeInvestmentRestrictionRequest                                 => true
> +    case _: ManualInvestmentRestrictionRequest                                  => true
> +    case _: RecurringInvestmentRestrictionRequest                               => true
> +    case _: GoalModificationRestrictionRequest                                  => true

## A1-0127 — Use Set.empty instead of empty string in goal acknowledgement handling

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; operation: [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Should be `Set.empty` instead of `””`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:130 · comment 816250309 · PR 13979 · 2026-06-23

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack

**Evidence:** anon-1.jsonl:130 · comment 816250309 · PR 13979 · 2026-06-23

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +                  (goalAvailableMvInGoalCcy, maybeGoalAvailableMvInDisplayCcy, _) <- if (isRedeemable) {
>                      calculateAvailableMarketValueAtPlanLevel(planIds, goalCcy, Some(ccy))
>                    } else {
> -                    Future.successful((BigDecimal(0), Some(BigDecimal(0))))
> +                    Future.successful((BigDecimal(0), Some(BigDecimal(0)), Set.empty))
>                    }
>                  } yield {
>                    Some(

## A1-0144 — Keep targetWeights and targetAmounts derivation and fallback consistent

**Source stance:** suggestion

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/utils/ThresholdBreachHelper.scala; operation: Fix/INV-5927 correctly distribute reminders; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can keep it consistent between targetWeights and targetAmounts
> 
> ```scala
> val targetAmounts = targetWeights.map {
>   tw => Calculator.distributeAmountByWeight(....)
> }
> ```
> 
> ‌
> 
> Then inside
> 
> ```scala
> val iTargetWeight = targetWeights.map(getOrZero(_, instrumentId)).getOrElse(iActualWeight)
> val iTargetAmount = targetAmounts.map(getOrZero(_, instrumentId)).getOrElse(iActualAmount)
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:148 · comment 819597599 · PR 14191 · 2026-06-30

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/ThresholdBreachHelper.scala`

**Explicit source context (pr_title):**

> Fix/INV-5927 correctly distribute reminders

## A1-0148 — ThresholdBreachHelper may require weights.toList

**Source stance:** open-question

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/utils/ThresholdBreachHelper.scala; operation: Fix/INV-5927 correctly distribute reminders; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This should be `weights.toList`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:152 · comment 819604013 · PR 14191 · 2026-06-30

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/ThresholdBreachHelper.scala`

**Explicit source context (pr_title):**

> Fix/INV-5927 correctly distribute reminders

**Evidence:** anon-1.jsonl:152 · comment 819604013 · PR 14191 · 2026-06-30

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/ThresholdBreachHelper.scala`

**Explicit source context (hunk):**

> +      val targetAmounts: Option[Map[String, BigDecimal]] = targetWeights.map { weights =>
> +        Calculator
> +          .distributeAmountByWeight(amountScale = CurrencyToMaxDecimalsMap(ccy), ratioScale = weightScale, rounding = roundingMode)(
> +            totalAmount = totalActualAmount,
> +            weightedElements = weights.toList
> +          )
> +          .toMap
> +      }
> +

## A1-0149 — ThresholdBreachHelper inner logic sorts by weight

**Source stance:** explanation

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/utils/ThresholdBreachHelper.scala; operation: Fix/INV-5927 correctly distribute reminders; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Inside logic will sort by weight…

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:153 · comment 819610546 · PR 14191 · 2026-06-30

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/ThresholdBreachHelper.scala`

**Explicit source context (pr_title):**

> Fix/INV-5927 correctly distribute reminders

**Evidence:** anon-1.jsonl:153 · comment 819610546 · PR 14191 · 2026-06-30

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/ThresholdBreachHelper.scala`

**Explicit source context (hunk):**

> +      val targetAmounts: Option[Map[String, BigDecimal]] = targetWeights.map { weights =>
> +        Calculator
> +          .distributeAmountByWeight(amountScale = CurrencyToMaxDecimalsMap(ccy), ratioScale = weightScale, rounding = roundingMode)(
> +            totalAmount = totalActualAmount,
> +            weightedElements = weights.toList
> +          )
> +          .toMap
> +      }
> +

## A1-0160 — Sort same-placement FRS by future maturity then orderId with Ordering

**Source stance:** requested-change

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/FixedRateSavingsPageGenerator.scala; operation: [INV-5214] adds frs; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> If same placement date, let’s still sort by \(future\) maturity date before falling back to orderId?
> 
> Also add Ordering instead of tuple

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:165 · comment 819044389 · PR 14080 · 2026-06-29

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/FixedRateSavingsPageGenerator.scala`

**Explicit source context (pr_title):**

> [INV-5214] adds frs

## A1-0168 — Define TradingAccountType Ordering with SGD or HKD first

**Source stance:** open-question

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/CashBalancePageGenerator.scala; operation: [INV-5212] adds cash balance section; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** No implicit Ordering exists

**Source-preserving request, proposal, or question:**

> There’s no implicit Ordering for TradingAccountType, but I suppose we want certain ordering right? Say at least SGD / HKD will always be on top?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:173 · comment 818401094 · PR 14045 · 2026-06-26

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/CashBalancePageGenerator.scala`

**Explicit source context (pr_title):**

> [INV-5212] adds cash balance section

## A1-0172 — Extract CashBalancePageGenerator Ordering

**Source stance:** requested-change

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/CashBalancePageGenerator.scala; operation: [INV-5212] adds cash balance section; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> extract Ordering

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:178 · comment 818399439 · PR 14045 · 2026-06-26

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/CashBalancePageGenerator.scala`

**Explicit source context (pr_title):**

> [INV-5212] adds cash balance section

**Evidence:** anon-1.jsonl:178 · comment 818399439 · PR 14045 · 2026-06-26

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/CashBalancePageGenerator.scala`

**Explicit source context (hunk):**

> +            lineItems = items,
> +            footnoteTexts = texts
> +          )
> +        }
> +      }
> +  }
> +
> +  private def sortRows(rows: List[CashBalanceRow]): List[CashBalanceRow] =
> +    rows.sorted(CashBalanceRowOrdering)

## A1-0177 — Sort and createPage in one Future.map and companion Ordering for transaction rows

**Source stance:** suggestion

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/CompletedTransactionsPageGenerator.scala; operation: [INV-5210, INV-5211, INV-5916] Feat/presentation completed processing transaction; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Avoid tuple allocation for each entry

**Source-preserving request, proposal, or question:**

> nit: can sort and createPage in single Future.map
> 
> Better to create Ordering in companion object of `CompletedTransactionRow` and `ProcessingTransactionRow` so we don’t have to create the tuple for all entries

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:183 · comment 815848529 · PR 14029 · 2026-06-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/CompletedTransactionsPageGenerator.scala`

**Explicit source context (pr_title):**

> [INV-5210, INV-5211, INV-5916] Feat/presentation completed processing transaction

## A1-0180 — Use sum for processing transaction total

**Source stance:** suggestion

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/ProcessingTransactionsPageGenerator.scala; operation: [INV-5210, INV-5211, INV-5916] Feat/presentation completed processing transaction; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> just use `sum`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:186 · comment 815857417 · PR 14029 · 2026-06-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/ProcessingTransactionsPageGenerator.scala`

**Explicit source context (pr_title):**

> [INV-5210, INV-5211, INV-5916] Feat/presentation completed processing transaction

**Evidence:** anon-1.jsonl:186 · comment 815857417 · PR 14029 · 2026-06-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/ProcessingTransactionsPageGenerator.scala`

**Explicit source context (hunk):**

> +    }
> +    val fxDisclaimer = Option.when(rows.nonEmpty)(FxDisclaimer)
> +    // The "Estimated trade date" disclaimer is a page-level footnote on the column header â always shown at index 1
> +    // when the section has any rows. Row-level footnotes (currently only synthetic-leg) start from index 2.
> +    val leadingFootnote = Option.when(rows.nonEmpty)(EstimatedTradeDateFootnote)
> +    FootnoteUtils.createPageWithLeadingFootnote(leadingFootnote, rows) { (items, texts) =>
> +      ProcessingTransactionsPage(
> +        lineItems = items,
> +        footnoteTexts = texts,

## A1-0188 — Check account before statement and late-transaction Option lookup

**Source stance:** requested-change

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/CompletedTransactionPresentationBehaviour.scala; operation: [INV-5210, INV-5211, INV-5916] Feat/presentation completed processing transaction; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Inside it’s Option only but still, we can check account first before looking at statement & late txns

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:194 · comment 816038318 · PR 14029 · 2026-06-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/CompletedTransactionPresentationBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-5210, INV-5211, INV-5916] Feat/presentation completed processing transaction

## A1-0205 — Create Ordering for processing transaction pages

**Source stance:** open-question

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/ProcessingTransactionsPageGenerator.scala; operation: [INV-5210, INV-5211, INV-5916] Feat/presentation completed processing transaction; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Create Ordering for this as well?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:211 · comment 817568354 · PR 14029 · 2026-06-25

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/ProcessingTransactionsPageGenerator.scala`

**Explicit source context (pr_title):**

> [INV-5210, INV-5211, INV-5916] Feat/presentation completed processing transaction

**Evidence:** anon-1.jsonl:211 · comment 817568354 · PR 14029 · 2026-06-25

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/ProcessingTransactionsPageGenerator.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  private def sortRows(rows: List[ProcessingTransactionRow]): List[ProcessingTransactionRow] =
> +    rows.sorted(ProcessingTransactionRowOrdering)
> +
> +  private def buildPage(statementData: StatementDataV1, rows: List[ProcessingTransactionRow]): ProcessingTransactionsPage = {
> +    val asOfDate = formatAsOf(statementData)
> +    val movements = statementData.statementBalanceData.processingInvestmentValueData.movements
> +    // Every movement in the spine must be consumed by a rendered row; an unconsumed movement means its

## A1-0212 — Optimizer full decision map includes zero orders; constructOrders filters them

**Source stance:** explanation

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/utils/orderGenerators/BuyOrderGeneratorV2.scala; operation: feat(trading): BuyOrderGeneratorV2 fixes; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This is also expected. Optimizer return full Map of decision hence it will contain 0-amount orders. `constructOrders` will correctly filter them out \(as it also handles manual instruction orders\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:218 · comment 815803975 · PR 14138 · 2026-06-22

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/utils/orderGenerators/BuyOrderGeneratorV2.scala`

**Explicit source context (pr_title):**

> feat(trading): BuyOrderGeneratorV2 fixes

## A1-0240 — Avoid refiltering goal plans

**Source stance:** open-question

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; operation: [INV-5700] feat(goal, rebalance): NVM goal details page changes; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> why do we need to filter plans again

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:247 · comment 809617927 · PR 13856 · 2026-06-11

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5700] feat(goal, rebalance): NVM goal details page changes

## A1-0265 — Cache effective minimums map in RebalanceSellAmountCalculator

**Source stance:** suggestion

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/utils/RebalanceSellAmountCalculator.scala; operation: Feat/INV-5616 calculate rebalancing sell amount feasibility logic; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Maybe assign the effective mins to some Map, so that we don’t keep recalculating

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:272 · comment 803296361 · PR 13934 · 2026-05-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/utils/RebalanceSellAmountCalculator.scala`

**Explicit source context (pr_title):**

> Feat/INV-5616 calculate rebalancing sell amount feasibility logic

**Evidence:** anon-1.jsonl:272 · comment 803296361 · PR 13934 · 2026-05-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/utils/RebalanceSellAmountCalculator.scala`

**Explicit source context (hunk):**

> +      .orElseBy(_.result.instrumentId)
> +  }
> +
> +  private case class CandidateSelection(
> +    remainingOverweightAmount: BigDecimal,
> +    candidates: List[UnderweightCandidate]
> +  )
> +
> +  private def effectiveMinimumAmount(instrumentInput: RebalanceSellAmountInstrumentInput): BigDecimal = {

## A1-0266 — Use List prepend when append order not needed

**Source stance:** suggestion

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/utils/RebalanceSellAmountCalculator.scala; operation: Feat/INV-5616 calculate rebalancing sell amount feasibility logic; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We don’t really care to append here? Might as well just List & prepend?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:273 · comment 803308230 · PR 13934 · 2026-05-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/utils/RebalanceSellAmountCalculator.scala`

**Explicit source context (pr_title):**

> Feat/INV-5616 calculate rebalancing sell amount feasibility logic

**Evidence:** anon-1.jsonl:273 · comment 803308230 · PR 13934 · 2026-05-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/utils/RebalanceSellAmountCalculator.scala`

**Explicit source context (hunk):**

> +    * We cannot naively use total overweight amount in full, as not all currently underweight instruments can be bought,
> +    * especially if they have non-waivable minimum buy amount (NWM). Since these NWMs are strict constraint, and the
> +    * rebalance sell orders are unit-based, we also need to be conservative with the buffer, as settled NAV of sell orders
> +    * might drop as compared to calculation time.
> +    *
> +    * OTOH, we also can't solve for the "best" sell vs buy order splits to rebalance the plan AAA optimally, as there
> +    * are external factors, especially since rebalance sell leg and buy leg are days apart.
> +    *
> +    * This implements a greedy approach that traverses a sorted list of underweight instruments, and decides whether

## A1-0302 — Zip optional metrics with inputs before flattening and collect

**Source stance:** observed-defect

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceMetricsCache.scala; operation: [INV-5558] feat(advisory): add performance based on daily market data; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Flatten first breaks positional correspondence

**Source-preserving request, proposal, or question:**

> Here we flatten the optional metrics, so it’s not safe to zip directly with the inputs anymore.
> 
> Need to zip first, then only filter out empty one in the collect

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:309 · comment 794518250 · PR 13698 · 2026-05-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceMetricsCache.scala`

**Explicit source context (pr_title):**

> [INV-5558] feat(advisory): add performance based on daily market data

## A1-0315 — Use Option.map in both places

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala; operation: [INV-5558] feat(advisory): add performance based on daily market data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> looks like we can just use Option.map? Same for below

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:322 · comment 797309037 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> [INV-5558] feat(advisory): add performance based on daily market data

**Evidence:** anon-1.jsonl:322 · comment 797309037 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (hunk):**

> -      val return1year = maybeAnnualisedPerformanceMetrics.flatMap(_.oneYearAnnualisedReturn)
> -      val return3year = maybeAnnualisedPerformanceMetrics.flatMap(_.threeYearAnnualisedReturn)
> +
> +      val returnWithMonthlyMarketData: Option[ReturnStatsHighlight] =
> +        maybePerformance.map { perf =>
> +          getReturns(
> +            perf.performanceMetrics.cumulativePerformanceMetrics,
> +            perf.performanceMetrics.annualisedPerformanceMetrics,
> +            perf.performanceMetrics.monthlyReturnEnd.atEndOfMonth()

## A1-0335 — find returns only one plan

**Source stance:** open-question

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; operation: [INV-5703] feat(bff, goal): NVM preference page changes; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> `find` will return only one plan right?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:342 · comment 798354684 · PR 13907 · 2026-05-19

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5703] feat(bff, goal): NVM preference page changes

**Evidence:** anon-1.jsonl:342 · comment 798354684 · PR 13907 · 2026-05-19

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      .runWith(Sink.seq)
> +      .map { instruments =>
> +        val instrumentMap = instruments.map(i => i.id -> i).toMap
> +        goals.map { goal =>
> +          val isMultiFundGoalWithNwmFunds = goal.plans.filter(PlanDto.isActive).exists { plan =>
> +                val instrumentIds = plan.targetAssetAllocation.targetInstrumentWeights.keySet
> +                val isMultiFund = instrumentIds.size > 1
> +                val hasNwmFund = instrumentIds.flatMap(instrumentMap.get).exists { instrument =>
> +                      instrument.subscriptionDetails.flatMap(_.regulation).flatMap(_.minTradingAmount).isDefined

## A1-0425 — Collect all currencies missing FX before throwing

**Source stance:** suggestion

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/data/FxRatesDataGenerator.scala; operation: [INV-5206] feat(report, marketdata): fx rates for statements v3 and market data fx api; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** foreach throw reports only first

**Source-preserving request, proposal, or question:**

> Is it better to collect all the ccys with missing rate, and throw together?
> 
> foreach and throw here will fail fast, and we get only the 1st exception

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:432 · comment 797283087 · PR 13816 · 2026-05-15

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/data/FxRatesDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-5206] feat(report, marketdata): fx rates for statements v3 and market data fx api

## A1-0439 — Second minOption appears redundant

**Source stance:** open-question

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala; operation: Resolve INV-5291: Eam profile validation integrations, fix up table name; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Looks like redundant 2nd minOption?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:446 · comment 793434196 · PR 13798 · 2026-05-06

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-5291: Eam profile validation integrations, fix up table name

**Evidence:** anon-1.jsonl:446 · comment 793434196 · PR 13798 · 2026-05-06

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Explicit source context (hunk):**

> state.feeInstructions.keys
>                    .filter(_.isAfter(cmd.effectiveStartDate))
>                    .minOption
> -                  .minOption
>                    .map(_.minusDays(1)),
>              )
>              Effect.persist[Event, State](event).thenAck(cmd.replyTo)
>            }
>          })

## A1-0456 — CustomerId PK prevents duplicate fee profile; change collection type to Set

**Source stance:** explanation

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/jdbc/feetiering/mapping/FeeTieringProfileMappingJdbcRepository.scala; operation: [INV-5238] feat(charge): Charge service changes to construct EAM contexts on quarterly charge flow; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> pk is customerId so yea not possible. Just changing the type to Set

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:463 · comment 793864229 · PR 13599 · 2026-05-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/jdbc/feetiering/mapping/FeeTieringProfileMappingJdbcRepository.scala`

**Explicit source context (pr_title):**

> [INV-5238] feat(charge): Charge service changes to construct EAM contexts on quarterly charge flow

**Evidence:** anon-1.jsonl:463 · comment 793864229 · PR 13599 · 2026-05-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/jdbc/feetiering/mapping/FeeTieringProfileMappingJdbcRepository.scala`

**Explicit source context (hunk):**

> +        .filter(_.profileId === profileId)
> +        .map(_.customerId)
>          .result
> -    }
> +    }.map(_.toSet)
>    }
>  }
> -

## A1-0496 — Parse all MStar benchmarks then accept only one with weight 100

**Source stance:** suggestion

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/morningstar/xmls/MStarFundBenchmarkDetails.scala; operation: Resolve INV-5219: Changes for benchmark retrieval logic; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** headOption ignores weighted benchmark collection

**Source-preserving request, proposal, or question:**

> Looking at MStar response, I don’t think it’s 100% safe to take headOption
> 
> ```scala
>             <PrimaryProspectusBenchmarks>
>                 <PrimaryProspectusBenchmark>
>                     <IndexId>F00000W0L1</IndexId>
>                     <IndexName>JP Morgan Asia Crdt(JACI)Non-InvGrd TR</IndexName>
>                     <Weighting>100</Weighting>
>                 </PrimaryProspectusBenchmark>
>             </PrimaryProspectusBenchmarks>
> ```
> 
> ‌
> 
> In this example, it seems to suggest that `PrimaryProspectusBenchmarks` is a list of benchmarks, each having their target weight. I think to be safe, the parsing from MStar should return collection, then it’s up to the caller to decide what to do with the data. And for starter, we can always check if single benchmark with 100% weight then return, else log and return no benchmark \(as it doesn’t fit current data model\). I guess we can start with error log first, and see what’s next?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Log error and return no benchmark for unsupported multi-benchmark model initially.

**Evidence:** anon-1.jsonl:503 · comment 740494850 · PR 13204 · 2026-01-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/morningstar/xmls/MStarFundBenchmarkDetails.scala`

**Explicit source context (pr_title):**

> Resolve INV-5219: Changes for benchmark retrieval logic

## A1-0503 — Use deduped dailyMvMap in fee calculation

**Source stance:** open-question

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerAltsFeesCalculator.scala; operation: Resolve INV-5237: Changes to calculate tier charge rates; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Why don’t we use the deduped `dailyMvMap`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:510 · comment 773305409 · PR 13424 · 2026-03-25

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerAltsFeesCalculator.scala`

**Explicit source context (pr_title):**

> Resolve INV-5237: Changes to calculate tier charge rates

**Evidence:** anon-1.jsonl:510 · comment 773305409 · PR 13424 · 2026-03-25

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerAltsFeesCalculator.scala`

**Explicit source context (hunk):**

> -            case AltsPlanChargeContext(_, _, altsRebateRatio) =>
> -              altsRebateRatio
> -            case _ =>
> -              throw new Exception(s"Found unexpected plan charge context for planId: $planId.")
> +    maybeCustomerProfileChargeContext match {
> +      case Some(customerProfileChargeContext) =>
> +        CustomerProfileChargeContextEvaluator.getFeeRateCalculator(planChargeContexts, dailyMvMap, customerProfileChargeContext)
> +
> +      case None =>

## A1-0528 — Fetch MStar basic info with mapAsync(2), id tuple, Sink.seq and toMap

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala; operation: Feat/INV-4792 update stitch details minimal request payload; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Why are we creating a map like this? Should just be
> 
> ```scala
> .mapAsync(2)(id => mstarApiService.getFundShareClassBasicInfo(id).map(id -> _))
> .runWith(Sink.seq)
> .map(_.toMap)
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:535 · comment 778127381 · PR 13640 · 2026-04-06

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (pr_title):**

> Feat/INV-4792 update stitch details minimal request payload

## A1-0536 — Resolve translator once and map repository results; None locale uses identity

**Source stance:** suggestion

**Context:**

> component: composition-impl/src/main/scala/com/endowus/silver/composition/impl/db/jdbc/instrumentData/InstrumentDataManager.scala; operation: [INV-4917] feat(advisory)(charge)(composition)(gateway)(portfolio)(rebalance): composition holding data translation for portoflio; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This whole block can use some refactor I guess
> 
> Maybe sth like this
> 
> ```
>   def findByInstrumentId(instrumentId: String, maybeLocale: Option[Locale]): Future[Option[InstrumentDataDbRecord]] = {
>     val translator = getTranslator(maybeLocale)
>     repository
>       .findByInstrumentId(instrumentId)
>       .map(_.map(translator))
>   }
> 
>   def findByInstrumentIds(instrumentIds: Set[String], maybeLocale: Option[Locale]): Future[Seq[InstrumentDataDbRecord]] = {
>     val translator = getTranslator(maybeLocale)
>     repository
>       .findByInstrumentIds(instrumentIds)
>       .map(_.map(translator))
>   }
> 
>   private def getTranslator(maybeLocale: Option[Locale]): InstrumentDataDbRecord => InstrumentDataDbRecord = {
>     maybeLocale match {
>       case Some(locale) => translateInstrument(locale, _)
>       case None => identity
>     }
>   }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:543 · comment 718785188 · PR 12978 · 2025-11-27

Source path: `composition-impl/src/main/scala/com/endowus/silver/composition/impl/db/jdbc/instrumentData/InstrumentDataManager.scala`

**Explicit source context (pr_title):**

> [INV-4917] feat(advisory)(charge)(composition)(gateway)(portfolio)(rebalance): composition holding data translation for portoflio

## A1-0583 — Use tail recursion for projection

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/CashSmartComparisonCalculator.scala; operation: [PG-1948] feat(advisory) Income projection; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Current two-year range is okay, tail recursion faster and safer memory-wise

**Source-preserving request, proposal, or question:**

> We only projection for 2 years here so it should be ok, but this one can be easily written as tail recursion which should be faster and safer \(memory wise\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:590 · comment 775484961 · PR 13581 · 2026-03-30

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/CashSmartComparisonCalculator.scala`

**Explicit source context (pr_title):**

> [PG-1948] feat(advisory) Income projection

## A1-0592 — Flatten positive charge fees then fold by FeeRateType and TradingAccountType

**Source stance:** suggestion

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeEstimateNotificationManager.scala; operation: [INV-5456] feat(charge, communication): Fee charge estimate email to include EAM fee; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Large interim nested map only regrouped later; zero ignored and negative not expected

**Source-preserving request, proposal, or question:**

> So this `groupedEstimatesWithFeeRateType` is not used anywhere, other than to be grouped again… i.e. there’s no value to create this interim map
> 
> And it’s quite big map in fact, `Map[FeeRateType, Map[TradingAccountType, List[PlanFeeQueryResult]]`
> 
> ‌
> 
> Can you consider sth like this?
> 
> * flatten the fee breakdown, and filter for positive value upfront - we don’t entertain zero, and we don’t expect negative entries
> * then we fold into expected shape `Map[FeeRateType, Map[TradingAccountType, BigDecimal]]`
> 
> ```scala
> estimatedFeesByFeeRateType = estimateResponse.planFees
>   .flatMap(
>     pf =>
>       pf.feeBreakdown
>         .getOrElse(List.empty)
>         .filter(_.accumulatedChargeableFee > 0)
>         .map(c => (c.feeRateType, pf.tradingAccountType) -> c.accumulatedChargeableFee)
>   )
>   .foldLeft(Map.empty[FeeRateType, Map[TradingAccountType, BigDecimal]]) {
>     case (accByFeeRateType, ((feeRateType, tradingAccountType), fee)) =>
>       accByFeeRateType.updatedWith(feeRateType) {
>         case Some(innerAccByTradingAccountType) =>
>           Some(innerAccByTradingAccountType.updatedWith(tradingAccountType) {
>             case Some(accumulatedFee) => Some(accumulatedFee + fee)
>             case None                 => Some(fee)
>           })
>         case None =>
>           Some(Map(tradingAccountType -> fee))
>       }
>   }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:599 · comment 775415744 · PR 13548 · 2026-03-30

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeEstimateNotificationManager.scala`

**Explicit source context (pr_title):**

> [INV-5456] feat(charge, communication): Fee charge estimate email to include EAM fee

## A1-0595 — Traverse large readSideTransactions once while accumulating merged transactions and IDs

**Source stance:** suggestion

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala; operation: Feat/INV-5336 enable rrt redemption; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Hmm in theory, upstream should have very few entries, while readside can have a lot more. So it would be better if we only traverse `readSideTransactions` once and accumulate both the merged txn and the ids. But yea this is small one

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:602 · comment 764523961 · PR 13472 · 2026-03-09

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-5336 enable rrt redemption

## A1-0596 — Map readside transactions and reuse upstreamById lookup

**Source stance:** requested-change

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala; operation: Feat/INV-5336 enable rrt redemption; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Replace readside row only if upstream status differs

**Source-preserving request, proposal, or question:**

> This is a map, not a collect.
> 
> Can avoid lookup `upstreamById` again
> 
> ```scala
> readSideTransactions.map { readSideTxn =>
>   upstreamById.get(readSideTxn.id) match {
>     case Some(upstreamTxn) if upstreamTxn.statusDetails.transactionStatus != readSideTxn.statusDetails.transactionStatus =>
>       upstreamTxn
>     case _ =>
>       readSideTxn
>   }
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:603 · comment 764522850 · PR 13472 · 2026-03-09

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-5336 enable rrt redemption

## A1-0604 — Avoid traversing readSideTransactions twice because collection may be large

**Source stance:** requested-change

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala; operation: Feat/INV-5336 enable rrt redemption; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I mean `readSideTransactions` might have many records so we want to avoid traversing it 2 times

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:611 · comment 767130119 · PR 13472 · 2026-03-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-5336 enable rrt redemption

**Evidence:** anon-1.jsonl:611 · comment 767130119 · PR 13472 · 2026-03-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (hunk):**

> +              upstream.get(readSideTxn.id) match {
> +                case Some(upstreamTxn) =>
> +                  val txn = if (upstreamTxn.statusDetails.transactionStatus != readSideTxn.statusDetails.transactionStatus) upstreamTxn else readSideTxn
> +                  (txn :: acc, upstream - readSideTxn.id)
> +                case None =>
> +                  (readSideTxn :: acc, upstream)
> +              }
> +          }
> +

## A1-0607 — Two nonoverlapping transaction lists only need concatenation

**Source stance:** open-question

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala; operation: Feat/INV-5336 enable rrt redemption; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I don’t get this comment. At this point, the 2 lists have no overlapping entries right? We simply concat them

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:614 · comment 773349790 · PR 13472 · 2026-03-25

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-5336 enable rrt redemption

## A1-0608 — Do not reverse query-only list lacking order contract

**Source stance:** open-question

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala; operation: Feat/INV-5336 enable rrt redemption; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Final TransactionOrderingForActivityAndBalances sorts results

**Source-preserving request, proposal, or question:**

> Do we care to reverse here? This step is only to query, even tho we return List, we have no ordering obligation.
> 
> The final result is sorted below using `TransactionOrderingForActivityAndBalances`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:615 · comment 773350397 · PR 13472 · 2026-03-25

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-5336 enable rrt redemption

## A1-0609 — Fold upstreamById.keySet with Set subtraction then map remaining IDs

**Source stance:** suggestion

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala; operation: Feat/INV-5336 enable rrt redemption; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We can start with `upstreamById.keySet` instead of full `upstreamTransactions`, so that we can just use `-` on Set, instead if `filterNot` on a List.
> 
> After fold completes, we would have `val (merged, remainingUpstreamIds)` which we can find upstreamOnly easily via map lookup from `upstreamById`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:616 · comment 773352431 · PR 13472 · 2026-03-25

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-5336 enable rrt redemption

## A1-0632 — Future group-by-customer optimization with canActionForCustomerGoals

**Source stance:** explanation

**Context:**

> component: bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/GuardsHandlerLogic.scala; operation: Feat/sg warnings blocks acks api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Known room for improvement to group by customer first before checking. We will tackle together with `canActionForCustomerGoals`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:640 · comment 721631977 · PR 13021 · 2025-12-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/GuardsHandlerLogic.scala`

**Explicit source context (pr_title):**

> Feat/sg warnings blocks acks api

## A1-0652 — Extract retrievedPrimaryBenchmarks with Option.when nonempty source list

**Source stance:** suggestion

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala; operation: Feat/INV-5338 v2 benchmark model; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can extract
> 
> ```scala
> retrievedPrimaryBenchmarks = Option.when(mstarRetrievalResult.fundBasicInfoAndWeightList.nonEmpty) {
>   upsertPrimaryBm(mstarRetrievalResult, existingInstrument.ccy, existingInstrument.fundDetails.isCurrencyHedged)
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:659 · comment 762142242 · PR 13358 · 2026-03-03

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (pr_title):**

> Feat/INV-5338 v2 benchmark model

## A1-0657 — Fold maybeBm so inceptionDate availability explicit

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/morningstar/MStarDataEnricher.scala; operation: Feat/INV-5338 v2 benchmark model; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We fold on maybeBm. Then here, it will be clear that inceptionDate is available

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:664 · comment 762166204 · PR 13358 · 2026-03-03

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/morningstar/MStarDataEnricher.scala`

**Explicit source context (pr_title):**

> Feat/INV-5338 v2 benchmark model

**Evidence:** anon-1.jsonl:664 · comment 762166204 · PR 13358 · 2026-03-03

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/morningstar/MStarDataEnricher.scala`

**Explicit source context (hunk):**

> +            )
> +            Option.empty[BenchmarkConstituentDto]
> +          } { bm =>
> +            val ccy = CurrencyUtils.safeCurrencyConversion(bm.fundCcy)
> +            val conversionNeeded = InstrumentConfigValidator.computeIsConversionNeeded(
> +              thisCurrency = ccy,
> +              instrumentCurrency = instrumentCcy,
> +              instrumentIsHedged = instrumentCurrencyHedged
> +            )

## A1-0716 — Use instrumentIds.size

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goaldetail/hk/HkExistingGoalDetailBehaviour.scala; operation: feat(bff, advisory): Add hasStandaloneOnlyFund flag to fundsmart goal detail behaviour and make funding source optional for fundsmart instrument list; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can use `instrumentIds.size` instead

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:727 · comment 750017066 · PR 13347 · 2026-02-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goaldetail/hk/HkExistingGoalDetailBehaviour.scala`

**Explicit source context (pr_title):**

> feat(bff, advisory): Add hasStandaloneOnlyFund flag to fundsmart goal detail behaviour and make funding source optional for fundsmart instrument list

**Evidence:** anon-1.jsonl:727 · comment 750017066 · PR 13347 · 2026-02-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goaldetail/hk/HkExistingGoalDetailBehaviour.scala`

**Explicit source context (hunk):**

> +    } yield {
> +      if (instrumentIds.size > 1 && hasStandaloneOnlyFund) {
> +        logger.error(s"Goal ${goal.goalId} is on multi-fund portfolio but contains standalone-only instrument")
> +      }
>        HkFundSmartGoalDetail(
>          goal = goal,
>          isViewOnlyGoal = isViewOnlyGoal,
> +        hasStandaloneOnlyFund = hasStandaloneOnlyFund,
>          planPerformanceMetrics = metrics

## A1-0757 — Do not combine redundant Option.when and getOrElse

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/InterGoalTransferManager.scala; operation: [INV-5296] feat(bff advisory): min investment amount v2; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We don’t need both `Option.when` and `getOrElse`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:769 · comment 746301045 · PR 13287 · 2026-01-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/InterGoalTransferManager.scala`

**Explicit source context (pr_title):**

> [INV-5296] feat(bff advisory): min investment amount v2

**Evidence:** anon-1.jsonl:769 · comment 746301045 · PR 13287 · 2026-01-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/InterGoalTransferManager.scala`

**Explicit source context (hunk):**

> -        val lowestMinTransferAmount = lowestMinInvestmentAmount + redemptionBufferAmount
> -        planRedeemableAmount >= lowestMinTransferAmount
> -      }
> +      hasSufficientRedeemableAmount = transferTargetsForPlan.map { target =>
> +        helper.calculateMinTransferAmount(
> +          maybeMinInvestmentAmount = target.targetRestrictions.minInvestmentAmountV2,
> +          redemptionBufferMultiplier = redemptionBufferMultiplier
> +        )
> +      }.minOption // lowest min transfer amount > highest redeemable amount possible (taking into account pending amount based redemption)

## A1-0775 — Map investmentRequests by ID before diff and membership checks

**Source stance:** suggestion

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/InvestmentPlanEntity.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** List diff/contains expensive

**Source-preserving request, proposal, or question:**

> Note that both `investmentRequestIds` / `investmentRequests` are all List, so these diff / contains ops are quite expensive
> 
> How about using Map instead?
> 
> ```scala
> val requestsById = state.investmentRequests.map(r => r.investmentRequestId -> r)
> val diff = investmentRequestIds.filterNot(requestsById.contains)
> if (diff.isEmpty) {
>   //... investmentRequestIds.map(requestsById)...
> } else {
>   //... error...
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:787 · comment 738475850 · PR 13145 · 2026-01-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/InvestmentPlanEntity.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0788 — Use contains instead of exists equality

**Source stance:** requested-change

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionRRTQueryLogic.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Just use `contains` instead of `exists(_ == ...)`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:800 · comment 743575196 · PR 13145 · 2026-01-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionRRTQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0789 — Resolve goal RRT plans before entityIds filter to avoid overfetch

**Source stance:** suggestion

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Current small-RRT volume accepted as okay

**Source-preserving request, proposal, or question:**

> Seeing the goalId filter here still feels a bit off. I guess since this RRT only, we don’t expect much data so it should be ok. Otherwise, I think if goalId is specified, calling get-goal-with-rrt to check its planIds, merge with input planId, and use for entityIds filter is better \(cuz we won’t over fetch\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:801 · comment 744756784 · PR 13145 · 2026-01-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0791 — Combine collect filter and following map to avoid rematch

**Source stance:** requested-change

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> The below `map` can be done here too right? Otherwise we are using `collect` as a `filter` without `map` here, and then have to match again below

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:803 · comment 744758249 · PR 13145 · 2026-01-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0795 — Use Option.when

**Source stance:** requested-change

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/PlanTopicSubscriber.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Option.when

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:807 · comment 744910214 · PR 13145 · 2026-01-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/PlanTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

**Evidence:** anon-1.jsonl:807 · comment 744910214 · PR 13145 · 2026-01-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/PlanTopicSubscriber.scala`

**Explicit source context (hunk):**

> -              _ <- refProvider.getPlanInvestmentManagerEntityRef(plan.planId).ask(cmd)
> +              _ <- refProvider.getPlanInvestmentManagerEntityRef(plan.planId).encapsulatedAsk(cmd, InvestmentRrtCommandContext(
> +                customerId = plan.customerId,
> +                rrtContext = Option.when(plan.initialInvestmentRequest.fundingInstructions.amount > 0)(InitialInvestmentRequestContext)
> +              ))
>              } yield Done
>            }

## A1-0797 — Fold optional goalId into successful planId list or filtered plan IDs

**Source stance:** suggestion

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ```scala
> goalId.fold(Future.successful(planId.map(List(_)))) {... Some(filteredPlanIds)... }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:809 · comment 744912891 · PR 13145 · 2026-01-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

**Evidence:** anon-1.jsonl:809 · comment 744912891 · PR 13145 · 2026-01-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala`

**Explicit source context (hunk):**

> +    goalId: Option[UUID],
> +    planId: Option[UUID],
> +    tradingAccountType: Option[TradingAccountType]
> +  ): Future[Seq[InvestmentRequestListAndInvestmentPlan]] = {
> +    for {
> +      maybePlanIdList <- goalId.fold(
> +        Future.successful(planId.map(s => Set(s.toString)))
> +      ) { goalId =>
> +        goalSvc.findGoalById(customerId = customerId, goalId = goalId, includePlans = true)

## A1-0810 — Map optional getByPortfolioId directly into optional response

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; operation: Feat/BB-3003 portfolio tenant api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ```scala
> getByPortfolioId(...).map {
>   _.map { pa =>
>     PortfolioAssignmentResponse(...)
>   }
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:822 · comment 746442738 · PR 12919 · 2026-01-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/BB-3003 portfolio tenant api

## A1-0814 — strs already Seq; no toSeq needed

**Source stance:** open-question

**Context:**

> component: silver-commons-jdbc/src/main/scala/com/endowus/silver/commons/jdbc/Filters.scala; operation: Feat/BB-2959 portfolio filters enhancement; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need `toSeq`? `strs` should already be a seq right?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:826 · comment 743470599 · PR 12884 · 2026-01-23

Source path: `silver-commons-jdbc/src/main/scala/com/endowus/silver/commons/jdbc/Filters.scala`

**Explicit source context (pr_title):**

> Feat/BB-2959 portfolio filters enhancement

**Evidence:** anon-1.jsonl:826 · comment 743470599 · PR 12884 · 2026-01-23

Source path: `silver-commons-jdbc/src/main/scala/com/endowus/silver/commons/jdbc/Filters.scala`

**Explicit source context (hunk):**

> +      Try(UUID.fromString(value)).fold(_ => CoerceFalse, uuid => column === uuid)
> +    case Op.In =>
> +      valuesFromJsonArray(value)
> +        .flatMap { strs =>
> +          Try(strs.map(UUID.fromString))
> +        }
> +        .fold(
> +          _ => CoerceFalse,
> +          uuids => column inSetBind uuids

## A1-0890 — Convert toList after flatMap

**Source stance:** suggestion

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/RRTHelper.scala; operation: Feat/INV INV-4671 redemption endpoint leverage rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can toList after flatMap instead

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:903 · comment 732346552 · PR 13061 · 2025-12-30

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/RRTHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV INV-4671 redemption endpoint leverage rrt

**Evidence:** anon-1.jsonl:903 · comment 732346552 · PR 13061 · 2025-12-30

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/RRTHelper.scala`

**Explicit source context (hunk):**

> +      rrtBasedResult = ByKeyMergeStrategy[PlanDto, UUID](keyExtractor = _.planId, postPatchFilter = goal => planIds.contains(goal.planId))
> +        .iterable(
> +          baseEntriesFut = readSideLoader,
> +          unfilteredPatchEntriesFut = entityLoader(customerId = customerId, maybeGoalId = None)
> +            .map(_.values.flatten.flatMap(_.plans).toList)
> +        )
> +        .map(_.map(_.patched))
> +        .map(_.toList)
> +        .withTimeout(readRoutingTableHelper.defaultTimeout) {

## A1-0947 — Explain drop(1) in monthly update

**Source stance:** open-question

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala; operation: [INV-4722] feat(marketdata): support single monthly change update; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Why drop\(1\)?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:962 · comment 680632297 · PR 12533 · 2025-09-09

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala`

**Explicit source context (pr_title):**

> [INV-4722] feat(marketdata): support single monthly change update

**Evidence:** anon-1.jsonl:962 · comment 680632297 · PR 12533 · 2025-09-09

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala`

**Explicit source context (hunk):**

> +      case Nil                                               => Nil
> +      case head :: tail if head.nav == 1 && head.change == 0 => tail
> +      case head :: _                                         => throw new Exception(s"Expected NAV 1 and monthly change 0 for instrument [$instrumentId] for existing data, however found $head")
> +    }
> +
> +    val updatedManualChanges = trimmedExistingMonthlyChanges
> +      .map(mc => ManualMonthlyChangeDto(mc.yearMonth, mc.change))
> +      .filterNot(_.yearMonth == givenYm)
> +      .appended(singleMonthlyChange)

## A1-0951 — Avoid sorting twice when generateMonthlyChangesFromCombinedMonthlyReturns sorts

**Source stance:** open-question

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala; operation: [INV-4722] feat(marketdata): support single monthly change update; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No need to sort right? Cuz `generateMonthlyChangesFromCombinedMonthlyReturns` will have to sort again anyway?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:966 · comment 687135142 · PR 12533 · 2025-09-22

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala`

**Explicit source context (pr_title):**

> [INV-4722] feat(marketdata): support single monthly change update

## A1-0953 — Require currentIndex strictly above startIndex for overflow pagination

**Source stance:** requested-change

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala; operation: Fix/INV-4826 statement cash balance page overflow; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Failed page-content assumption otherwise causes endless tail recursion

**Source-preserving request, proposal, or question:**

> I think let’s put an assertion here that `currentIndex` would be strictly greater than `startIndex`, based on our assumption of the page content.
> 
> Otherwise if such assumption fails in prod, we will get stuck in this tailrec.
> 
> ‌
> 
> Same for the cash balance page

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Applies to transaction and cash-balance pages.

**Evidence:** anon-1.jsonl:968 · comment 695046002 · PR 12709 · 2025-10-06

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala`

**Explicit source context (pr_title):**

> Fix/INV-4826 statement cash balance page overflow

## A1-1011 — Use request.targetWeights.keySet

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateConfirmationBehaviour.scala; operation: [INV-5015] feat(compliance, goal, investment, trading): Integrate acknowledgements with compliance; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> maybe use `request.targetWeights.keySet`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1027 · comment 725864841 · PR 12963 · 2025-12-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateConfirmationBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-5015] feat(compliance, goal, investment, trading): Integrate acknowledgements with compliance

**Evidence:** anon-1.jsonl:1027 · comment 725864841 · PR 12963 · 2025-12-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateConfirmationBehaviour.scala`

**Explicit source context (hunk):**

> baseGoalCreateRequest = generateBaseGoalCreateRequest(request, createdPortfolio, acknowledgements, riskTolerance, dividendDistributionPref)
>          //add region specific acknowledgements here
> -        requireUnemployedSubstantialInvestmentAck <- isFinancialSituationAckRequired(request.customerId)
> -        requireUnsuitableForSipAck <- isUnsuitableForSipAckRequired(request.customerId)
> +        financialSuitabilityCheckResponse <- checkFinancialSituationSuitability(request.customerId, request.targetWeights.keySet)
>          additionalAcks = customerGoalAcknowledgement(
>            maybeCkaExemptionAcknowledged = request.maybeCkaExemptionAcknowledged,
>            maybeFinancialSituationAcknowledged = request.maybeFinancialSituationAcknowledged,
> -          requireUnemployedSubstantialInvestmentAck = requireUnemployedSubstantialInvestmentAck,

## A1-1049 — Return Option invalid only and flatMap; discard valid reconciliation results

**Source stance:** requested-change

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/models/Translation.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We don’t really care about Valid ones. Let’s change the inner methods to return Option and only yield if invalid, then we flatmap here

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1066 · comment 675906812 · PR 12485 · 2025-08-28

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/Translation.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

## A1-1051 — Pattern-match tuple instead of _2

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> case instead of \_2

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1068 · comment 680163745 · PR 12485 · 2025-09-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

**Evidence:** anon-1.jsonl:1068 · comment 680163745 · PR 12485 · 2025-09-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala`

**Explicit source context (hunk):**

> +                templateTagErrors <- validateAdvisoryTags(t.displayTags.toSet, locale)
> +              } yield (locale, templateErrors ++ templateTagErrors)
> +            }
> +            .wireTap(ValidationError.logErrors(logger, _))
> +            .runFold(ValidationError.ErrorCount.empty)(ValidationError.mergeErrorCount)
> +        }
> +        .runFold(ValidationError.ErrorCount.empty)({ case (errorCount, errorCountPerLocale) => errorCount + errorCountPerLocale })
> +    } yield {
> +      if (templateErrorCount.total > 0) {

## A1-1059 — Collect only displayTags

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Maybe we collect just the displayTags?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1076 · comment 680163597 · PR 12485 · 2025-09-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

**Evidence:** anon-1.jsonl:1076 · comment 680163597 · PR 12485 · 2025-09-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala`

**Explicit source context (hunk):**

> +            }
> +            .wireTap(ValidationError.logErrors(logger, _))
> +            .runFold(ValidationError.ErrorCount.empty)(ValidationError.mergeErrorCount)
> +        }
> +        .runFold(ValidationError.ErrorCount.empty)({ case (errorCount, errorCountPerLocale) => errorCount + errorCountPerLocale })
> +    } yield {
> +      if (templateErrorCount.total > 0) {
> +        logger.error(
> +          s"Reconcile translations completed with ${templateErrorCount.missingTranslationCount} missing translations and ${templateErrorCount.missingDataCount} missing data. Check logs for details."

## A1-1067 — Count errors rather than collect

**Source stance:** requested-change

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/models/Translation.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Just count, not need to collect errors

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1084 · comment 681458103 · PR 12485 · 2025-09-10

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/Translation.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

**Evidence:** anon-1.jsonl:1084 · comment 681458103 · PR 12485 · 2025-09-10

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/Translation.scala`

**Explicit source context (hunk):**

> +        def +(other: ErrorCount): ErrorCount = ErrorCount(
> +          missingTranslationCount + other.missingTranslationCount,
> +          missingDataCount + other.missingDataCount
> +        )
> +      }
> +
> +      object ErrorCount {
> +
> +        def empty: ErrorCount = ErrorCount(0L, 0L)

## A1-1073 — Merge by explicit keyExtractor with distinctBy or supplied merge logic

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableUtils.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** distinct alone insufficient; avoid optional strategy

**Source-preserving request, proposal, or question:**

> distinct alone is not enough
> 
> ```scala
> def mergeDataViaPlanId[M](planId: UUID)(readSideLoader, entityLoader, keyExtractor)
> def mergeDataViaPlanId[M](planId: UUID)(readSideLoader, entityLoader, mergeLogic)
> ```
> 
> ‌
> 
> Given `keyExtractor`, we construct `mergeLogic` using `distinctBy(keyExtractor)`. Then we dont need any optional

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1090 · comment 700091356 · PR 12767 · 2025-10-15

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableUtils.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1082 — distinctBy documentation does not promise order preservation

**Source stance:** explanation

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableUtils.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> `distinctBy` doesn’t state about order preserving in its docs

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1099 · comment 705788465 · PR 12767 · 2025-10-28

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableUtils.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1102 — Materialize toSeq or toList before returning mutable-map-derived view

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Ensure fully immutable structure rather than mutable reference

**Source-preserving request, proposal, or question:**

> It should be ok but let’s stay on the safe side and call toSeq or toList here to ensure we return completely immutable structure, instead of still referencing the mutable Map

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1119 · comment 713906463 · PR 12767 · 2025-11-14

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1118 — Use map values without filter or toList

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> no need filter
> 
> use values \+ no need toList

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1135 · comment 716209441 · PR 12767 · 2025-11-20

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1131 — Use groupMap then collect

**Source stance:** requested-change

**Context:**

> component: bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/AkkaHttpAuthRecipes.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> `groupMap` then collect

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1148 · comment 717270816 · PR 12767 · 2025-11-24

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/AkkaHttpAuthRecipes.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

**Evidence:** anon-1.jsonl:1148 · comment 717270816 · PR 12767 · 2025-11-24

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/AkkaHttpAuthRecipes.scala`

**Explicit source context (hunk):**

> +  private[impl] def validateAdditionalContextFromOwnershipGuards(
> +    authorized: Authorized,
> +    tracingContexts: List[TracingContext.Tag[_]]
> +  ): List[TracingContext.Tag[_]] = {
> +    val hasDifferentValuesMap = tracingContexts
> +      .groupMapReduce(_.key)(tag => Set(tag.value))(_ ++ _)
> +      .collect { case (key, value) if value.size > 1 => (key, value.size) }
> +
> +    if (hasDifferentValuesMap.nonEmpty) {

## A1-1134 — Keep compliance collection as List or Set

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/util/SipHelper.scala; operation: [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Better to keep this as List/Set instead

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1151 · comment 724002265 · PR 13025 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/util/SipHelper.scala`

**Explicit source context (pr_title):**

> [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis

**Evidence:** anon-1.jsonl:1151 · comment 724002265 · PR 13025 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/util/SipHelper.scala`

**Explicit source context (hunk):**

> +  implicit def executionContext: ExecutionContext
> +  implicit def materializer: Materializer
> +  def instrumentService: SgInstrumentService
> +
> +  def hasSipInstruments(instrumentIds: Set[String]): Future[Boolean] = {
> +    instrumentService.getInstrumentByIds(instrumentIds.mkString(",")).map { instruments =>
> +      instruments.exists { i =>
> +        InstrumentInfoDto
> +          .getMasDetails(i)

## A1-1135 — Use Option.when

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/util/SipHelper.scala; operation: [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> nit: Option.when

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1152 · comment 724002399 · PR 13025 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/util/SipHelper.scala`

**Explicit source context (pr_title):**

> [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis

**Evidence:** anon-1.jsonl:1152 · comment 724002399 · PR 13025 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/util/SipHelper.scala`

**Explicit source context (hunk):**

> +    Source(plans)
> +      .mapAsync(3) { plan =>
> +        val instrumentIds = plan.targetAssetAllocation.targetInstrumentWeights.values.map(_.id).toSet
> +        hasSipInstruments(instrumentIds).map { hasOnlySip =>
> +          Option.when(hasOnlySip)(plan.planId)
> +        }
> +      }
> +      .mapConcat(identity)
> +      .runWith(Sink.seq)

## A1-1139 — Use collect instead of filter then map

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; operation: [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Use collect instead of filter \+ map

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1156 · comment 724006096 · PR 13025 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis

## A1-1145 — Reuse fetched source goals for customer entrypoint and key names by goalId

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; operation: [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Only target-goal entrypoint needs extra source-goal fetch

**Source-preserving request, proposal, or question:**

> Actually we only need to fetch source goalName if entrypoint is by \(target\) goalId. If entrypoint is by customerId, we would already fetch all live goals which would include the source goals as well?
> 
> And this goalName map can be keyed by goalId. It doesn’t need to repeat and keyed by planId?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1162 · comment 724042423 · PR 13025 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis

## A1-1147 — After contains check getOrElse unnecessary

**Source stance:** open-question

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/EdgeWarningAndRestrictionQueryLogic.scala; operation: [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Just code style generally. We also check contains then why we need getOrElse?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1164 · comment 724088989 · PR 13025 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/EdgeWarningAndRestrictionQueryLogic.scala`

**Explicit source context (pr_title):**

> [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis

**Evidence:** anon-1.jsonl:1164 · comment 724088989 · PR 13025 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/EdgeWarningAndRestrictionQueryLogic.scala`

**Explicit source context (hunk):**

> +        case t: PlanRecurringTransfer =>
> +          for {
> +            sourceGoalName <- if (goalNamesByGoalId.contains(t.sourceGoalId)) {
> +              Future.successful(goalNamesByGoalId(t.sourceGoalId))
> +            } else {
> +              goalService.findGoal(t.sourceGoalId, includePlans = false).map(_.name)
> +            }
> +            planLatestMarketValueResponse <- timeSeriesService.queryLatestMarketValue(planId = Some(t.planId))
> +            planMv = planLatestMarketValueResponse.latestMarketValue.map(_.totalMarketValue).getOrElse(BigDecimal(0))

## A1-1157 — Group acknowledgement plans by customerId first

**Source stance:** open-question

**Context:**

> component: bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/GuardsHandlerLogic.scala; operation: [INV-5022] feat(compliance): create api for financial situation ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Should we groupBy customerId first?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1174 · comment 718836190 · PR 12917 · 2025-11-27

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/GuardsHandlerLogic.scala`

**Explicit source context (pr_title):**

> [INV-5022] feat(compliance): create api for financial situation ack

**Evidence:** anon-1.jsonl:1174 · comment 718836190 · PR 12917 · 2025-11-27

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/GuardsHandlerLogic.scala`

**Explicit source context (hunk):**

> +    for {
> +      plans <- goalService.GoalApi.findPlansByIds(planIds.mkString(",")).withRetry(AlwaysRetryOnException, retrySettings)
> +      additionalContexts <- Source(plans)
> +        .mapAsync(parallelism = 4)(
> +          plan =>
> +            innerCanActionForCustomer(
> +              s"`canActionForCustomerPlan` for RequestedPlanId[${plan.planId}] of Customer[${plan.customerId}]",
> +              plan.customerId,
> +              authorized

## A1-1159 — Validate one grouped customer rather than traverse every plan again

**Source stance:** requested-change

**Context:**

> component: bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/GuardsHandlerLogic.scala; operation: [INV-5022] feat(compliance): create api for financial situation ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> After groupBy already \(and even assert only 1 customer is allowed\), then we just need to check for that one, no need to traverse all plans again right?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1176 · comment 719253956 · PR 12917 · 2025-11-28

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/GuardsHandlerLogic.scala`

**Explicit source context (pr_title):**

> [INV-5022] feat(compliance): create api for financial situation ack

## A1-1253 — Use groupMapReduce for variant grouping

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/LocaleAwareInstrumentCache.scala; operation: Feat/INV-4922 consolidate advisory duplicate caches; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> groupMapReduce? :rofl:

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1268 · comment 718832772 · PR 12908 · 2025-11-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/LocaleAwareInstrumentCache.scala`

**Explicit source context (pr_title):**

> Feat/INV-4922 consolidate advisory duplicate caches

**Evidence:** anon-1.jsonl:1268 · comment 718832772 · PR 12908 · 2025-11-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/LocaleAwareInstrumentCache.scala`

**Explicit source context (hunk):**

> +    * @return Map of LocaleAwareInstrumentCacheKey -> instrumentInfoDto
> +    */
> +  private def getRemoteInstruments(queryInputs: Iterable[LocaleAwareInstrumentCacheKey]): Future[Map[LocaleAwareInstrumentCacheKey, InstrumentInfoDto]] = {
> +    val groupedInstrumentId = queryInputs
> +      .groupMap(s => (s.locale, s.withMstarDocs))(_.instrumentId)
> +
> +    Source(groupedInstrumentId)
> +      .mapAsync(2) {
> +        case ((locale, withMstarDocs), instrumentIds) =>

## A1-1278 — Use exists

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala; operation: [INV-4994] feat(advisory, goal): Decouple logic between risk misalignment and financial situation and add SIP acknowledgement; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Just change this to `exists`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1293 · comment 714640092 · PR 12924 · 2025-11-17

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Explicit source context (pr_title):**

> [INV-4994] feat(advisory, goal): Decouple logic between risk misalignment and financial situation and add SIP acknowledgement

**Evidence:** anon-1.jsonl:1293 · comment 714640092 · PR 12924 · 2025-11-17

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Explicit source context (hunk):**

> +      } else {
> +        Future.successful(false)
> +      }
> +    } yield isSipAckApplicable
> +  }
> +
> +  private def checkInstrumentsEipSipStatus(instruments: List[InstrumentInfoDto]): Boolean =
> +    instruments.exists { i =>
> +      getMasDetails(i)

## A1-1343 — Search RPC tasks by tenantId and later goalId/planId

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala; operation: [BB-3055] feat(rebalance): adding RPC approvals; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Unscoped results can be too large

**Source-preserving request, proposal, or question:**

> Let’s put at least tenantId in this search too? And let’s have followup task to allow searching by goalId/planId in this search, otherwise we can be at risk of returning too large data here

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1358 · comment 705355409 · PR 12776 · 2025-10-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala`

**Explicit source context (pr_title):**

> [BB-3055] feat(rebalance): adding RPC approvals

## A1-1348 — Use Set for RPC identifiers

**Source stance:** suggestion

**Context:**

> component: composition-api/src/main/scala/com/endowus/silver/composition/api/models/breakdown/package.scala; operation: [BB-3055] feat(rebalance): adding RPC approvals; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Use Set instead?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1363 · comment 705341401 · PR 12776 · 2025-10-27

Source path: `composition-api/src/main/scala/com/endowus/silver/composition/api/models/breakdown/package.scala`

**Explicit source context (pr_title):**

> [BB-3055] feat(rebalance): adding RPC approvals

**Evidence:** anon-1.jsonl:1363 · comment 705341401 · PR 12776 · 2025-10-27

Source path: `composition-api/src/main/scala/com/endowus/silver/composition/api/models/breakdown/package.scala`

**Explicit source context (hunk):**

> topMarketExposures: List[IndividualHoldingItemDto],
>      topSectorAllocations: List[IndividualHoldingItemDto]
> -  )
> +  ) {
> +    lazy val instrumentIds: Set[String] =
> +      instrumentBreakdowns.map(_.instrumentId).toSet
> +
> +    lazy val instrumentTargetWeights: Map[String, BigDecimal] =
> +      instrumentBreakdowns.map(b => b.instrumentId -> b.targetWeight).toMap

## A1-1384 — Unapply totalFee totalBufferedFeeAmount unchargedFees directly

**Source stance:** suggestion

**Context:**

> component: redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/logic/service/BaseServiceLogicImpl.scala; operation: [INV-4563] feat(bff, goal, redemption, trading): Add full redemption threshold endpoint; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I think you can just unapply here directly
> 
> ```scala
> (totalFee, totalBufferedFeeAmount, unchargedFees) <- ...
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1400 · comment 703516921 · PR 12525 · 2025-10-23

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/logic/service/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4563] feat(bff, goal, redemption, trading): Add full redemption threshold endpoint

## A1-1412 — FilterNot hasCpfSaAccount then map investor type and empty fallback

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartInstrumentBuilder.scala; operation: Feat/INV-4904 display cpf sa public; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Isn’t it just swap the condition and getOrElse?
> 
> ```scala
> _.filterNot(RegionalCustomerDto.hasCpfSaAccount)
>   .map(_ => Set(InvestorType.SINGAPORE_CPF_SA_INVESTOR))
>   .getOrElse(Set.empty[InvestorType])
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1428 · comment 698869093 · PR 12756 · 2025-10-13

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> Feat/INV-4904 display cpf sa public

## A1-1426 — Only top25Holdings switched to takeTopKBy

**Source stance:** explanation

**Context:**

> component: composition-impl/src/main/scala/com/endowus/silver/composition/impl/calculators/InstrumentBreakdownCalculator.scala; operation: [INV-4908] feat(advisory)(bff)(composition)(portfolio): Support top exposure items in PortfolioBreakdownDto; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Other holdings maps should derive from top25 but deferred pending replacement

**Source-preserving request, proposal, or question:**

> I change only `top25Holdings` to use this `takeTopKBy`
> 
> All the maps below `assetClassHoldingItems`, `countryHoldingItems` etc ideally should have started from `top25Holdings` instead of full `underlyingHoldingsForInstrument` again. But will leave them for now, as we are expected to change / get rid of them soon.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1442 · comment 697943885 · PR 12736 · 2025-10-10

Source path: `composition-impl/src/main/scala/com/endowus/silver/composition/impl/calculators/InstrumentBreakdownCalculator.scala`

**Explicit source context (pr_title):**

> [INV-4908] feat(advisory)(bff)(composition)(portfolio): Support top exposure items in PortfolioBreakdownDto

## A1-1478 — Optional broker rebate lookups require flatMap and minOption

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala; operation: [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Since the lookup from `brokerBasedRebateRatio.ratios` may return None, don’t we need to flatMap and minOption instead?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1495 · comment 691888678 · PR 12661 · 2025-10-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources

## A1-1483 — flatMap optional broker ratios then minOption and fallback

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala; operation: [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Resulting Set may be empty

**Source-preserving request, proposal, or question:**

> Shouldn’t it be `tradingAccountTypes.flatMap { ... }.minOption.getOrElse(...)` instead?
> 
> The inner lookup by broker will return `Option[BigDecimal]`, so we need to flatMap? Then resulting Set might be empty, so we need minOption?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1500 · comment 691951056 · PR 12661 · 2025-10-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources

## A1-1484 — Inline runFold merges instruments distinctBy id, goal-type unions, investor-type union

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala; operation: [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Map merge starts from combined keysets

**Source-preserving request, proposal, or question:**

> Maybe just put inline like this?
> 
> ```scala
> .runFold(((Seq.empty[InstrumentInfoDto], Map.empty[String, Set[InvestmentGoalType]]), Set.empty[InvestorType])) {
>   case (
>       ((accInstruments, accInstrumentGoalTypes), accInvestorTypes),
>       ((currInstruments, currInstrumentGoalTypes), currInvestorTypes)
>       ) =>
>     val mergedInstruments = (accInstruments ++ currInstruments).distinctBy(_.id)
>     
>     val mergedInstrumentGoalTypes = (accInstrumentGoalTypes.keySet ++ currInstrumentGoalTypes.keySet).map { instrumentId =>
>       instrumentId -> (accInstrumentGoalTypes.getOrElse(instrumentId, Set.empty) ++ currInstrumentGoalTypes.getOrElse(instrumentId, Set.empty))
>     }.toMap
>     
>     val mergedInvestorTypes = accInvestorTypes ++ currInvestorTypes
>     
>     ((mergedInstruments, mergedInstrumentGoalTypes), mergedInvestorTypes)
> }
> ```
> 
> ‌
> 
> Note on the map merging logic, we can simply start from the keys

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1501 · comment 691960569 · PR 12661 · 2025-10-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources

## A1-1485 — Apply same funding-source merge improvement here

**Source stance:** requested-change

**Context:**

> component: advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala; operation: [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Same here

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1502 · comment 691945656 · PR 12661 · 2025-10-01

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources

**Evidence:** anon-1.jsonl:1502 · comment 691945656 · PR 12661 · 2025-10-01

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Explicit source context (hunk):**

> -      def handle(locale: Option[Locale], investmentGoalType: Option[InvestmentGoalType], tradingAccountType: Option[TradingAccountType], includeAlts: Option[Boolean]): Future[Out]
> +      def handle(locale: Option[Locale], investmentGoalType: Option[InvestmentGoalType], tradingAccountTypes: Option[CommaSeparatedSetParam[TradingAccountType]], includeAlts: Option[Boolean]): Future[Out]
>      }
>  
>      //GET /api/v1/advisory/edge/tenant/instrument-list?locale&goalType&tradingAccountType&includeAlts
>      val getInstrumentListForTenant: EndpointDef[GetInstrumentListForTenantType] = {
>        val locale = qs[Option[Locale]]("locale")
>        val goalType = qs[Option[InvestmentGoalType.Value]]("goalType")
> -      val tradingAccountType = qs[Option[TradingAccountType.Value]]("tradingAccountType")

## A1-1500 — Convert toList at intended point

**Source stance:** requested-change

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/utils/FeeChargeDetailsCalculator.scala; operation: TT-7047 adjust fee charge details when handling more than 1 trading account types during withdrawal; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> toList here instead

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1517 · comment 696524154 · PR 12713 · 2025-10-08

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/utils/FeeChargeDetailsCalculator.scala`

**Explicit source context (pr_title):**

> TT-7047 adjust fee charge details when handling more than 1 trading account types during withdrawal

**Evidence:** anon-1.jsonl:1517 · comment 696524154 · PR 12713 · 2025-10-08

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/utils/FeeChargeDetailsCalculator.scala`

**Explicit source context (hunk):**

> +                    baseAmount = weightedBaseMap(accountType),
> +                    taxRate = taxRate,
> +                    taxAmount = weightedTaxMap(accountType)
> +                  )
> +                  (accountType, cr, Some(feeChargeDetails.copy(taxDetails = Some(weightedTaxDetail))))
> +                }
> +            }
> +          case None =>
> +            cashReservations.toList.map { case (accountType, cr) => (accountType, cr, originalFeeChargeDetails) }

## A1-1547 — Use optionA.orElse(optionB) rather than wrapping getOrElse in Some

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateConfirmationBehaviour.scala; operation: [INV-4773] feat(advisory, charge, goal): Create implementation for Income Enhanced to support goal create flow API's; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> nits: it’s almost the same, but using `optionA.orElse(optionB)` is slightly better then `Some(optionA.getOrElse(B))`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1564 · comment 689819826 · PR 12621 · 2025-09-26

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateConfirmationBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-4773] feat(advisory, charge, goal): Create implementation for Income Enhanced to support goal create flow API's

## A1-1568 — Sort offerings by displayOrder

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioOfferingsManager.scala; operation: [INV-4769] feat(advisory): create portfolio offerings api for income enhanced; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This one we sort by displayOrder right?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1585 · comment 689432614 · PR 12618 · 2025-09-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioOfferingsManager.scala`

**Explicit source context (pr_title):**

> [INV-4769] feat(advisory): create portfolio offerings api for income enhanced

**Evidence:** anon-1.jsonl:1585 · comment 689432614 · PR 12618 · 2025-09-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioOfferingsManager.scala`

**Explicit source context (hunk):**

> +
> +        buildPortfolioOfferings(
> +          incomeEnhancedProductPortfolioSource,
> +          buildIncomeEnhancedPortfolioOffering
> +        ).map(_.sortBy(_.displayOrder))
> +
> +      } else {
> +        logger.info(s"Income enhanced product only available to AI customers so returning empty for customer $customerId")
> +        Future.successful(Seq.empty[IncomeEnhancedPortfolio])

## A1-1572 — span daily NAV by not-after start; retain last prior plus later entries

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyNavCache.scala; operation: [INV-4822] feat(advisory, marketdata): Filter out daily index before inception date; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> How about checking by `!isAfter` instead?
> 
> ```scala
> val (upToStartDate, afterStartDate) = dailyNav.span { case (date, _) => !date.isAfter(dataStartDate) }
> upToStartDate.lastOption.toList ++ afterStartDate
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1589 · comment 690789588 · PR 12653 · 2025-09-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyNavCache.scala`

**Explicit source context (pr_title):**

> [INV-4822] feat(advisory, marketdata): Filter out daily index before inception date

## A1-1574 — No maxByOption because ordering already assumed

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyNavCache.scala; operation: [INV-4822] feat(advisory, marketdata): Filter out daily index before inception date; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No need `maxByOption` cuz we anyhow rely on the fact that it’s already sorted

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1591 · comment 690791015 · PR 12653 · 2025-09-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyNavCache.scala`

**Explicit source context (pr_title):**

> [INV-4822] feat(advisory, marketdata): Filter out daily index before inception date

**Evidence:** anon-1.jsonl:1591 · comment 690791015 · PR 12653 · 2025-09-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyNavCache.scala`

**Explicit source context (hunk):**

> private def getRemoteInstrumentPrice(
>      inputs: Iterable[(String, CurrencyUnit)]
>    ): Future[Map[(String, CurrencyUnit), List[DateValuePairDto]]] = {
> +    def handleCommonStartDateData(dailyNav: List[(LocalDate, BigDecimal)], dataStartDate: LocalDate): List[(LocalDate, BigDecimal)] = {
> +      val (beforeStartDate, afterStartDate) = dailyNav.span{ case(date, _) => !date.isAfter(dataStartDate) }
> +      beforeStartDate.lastOption.toList ++ afterStartDate
> +    }
> +
>      logger.logTime("Remote get instrument price lookup") {

## A1-1576 — Resolve optional inception using filter/map/getOrElse or fold, not get

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyNavCache.scala; operation: [INV-4822] feat(advisory, marketdata): Filter out daily index before inception date; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Try to write idiomatic scala when you can… `getOrElse` or `fold`, but not `get`
> 
> ```scala
> (dataStartDate, queryStartDate) = maybeInceptionDate
>   .filter(_.isAfter(commonStartDate))
>   .map(inceptionDateAfterCommon => (inceptionDateAfterCommon, inceptionDateAfterCommon))
>   .getOrElse((commonStartDate, commonStartDate.minusMonths(1)))
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1593 · comment 690846306 · PR 12653 · 2025-09-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyNavCache.scala`

**Explicit source context (pr_title):**

> [INV-4822] feat(advisory, marketdata): Filter out daily index before inception date

## A1-1583 — Use anonymous parameter for addDerivedTagsV2 mapping

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartInstrumentBuilder.scala; operation: TT-6560 allow singapore cpf sa investor type; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> It’s just preference, but in case you’re not aware, you can anonymous parameter, and write as something like this
> 
> ```scala
> validInstruments.map(addDerivedTagsV2(_, blacklistedInvestorTypes))
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1600 · comment 689381468 · PR 12204 · 2025-09-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> TT-6560 allow singapore cpf sa investor type

## A1-1630 — Use mapValues or groupMap

**Source stance:** suggestion

**Context:**

> component: bff-impl/src/main/scala/com/endowus/silver/bff/impl/logic/ApprovalsWorkflowServiceLogicImpl.scala; operation: [BB-2784] feat(bff)(workflow): exposing task by status api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can use mapValues, or even groupMap

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1646 · comment 682650586 · PR 12434 · 2025-09-12

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/logic/ApprovalsWorkflowServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [BB-2784] feat(bff)(workflow): exposing task by status api

**Evidence:** anon-1.jsonl:1646 · comment 682650586 · PR 12434 · 2025-09-12

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/logic/ApprovalsWorkflowServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +        .groupMap(_._1)(_._2)
> +
> +    Source(tasksGroupedByTenant.toList)
> +      .mapAsync(2) { case (tenantId, groupedTasks) =>
> +        val groupedTaskIds = groupedTasks.map(_.taskId)
> +        tenantProvider.runWithContext(Tenant(tenantId)) {
> +          advisoryServiceClient.SgAdvisoryApi
> +            .checkTasksApprovalValidity(TaskListApprovalValidityRequest(groupedTaskIds))
> +            .map(_.taskIdValidation)

## A1-1662 — Use Option.when

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala; operation: [INV-4760] feat(advisory): Add filters for CCY-Hedged to filters; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> nit: Can use Option.when

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1679 · comment 682694037 · PR 12596 · 2025-09-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> [INV-4760] feat(advisory): Add filters for CCY-Hedged to filters

**Evidence:** anon-1.jsonl:1679 · comment 682694037 · PR 12596 · 2025-09-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (hunk):**

> }
>  
> +  final protected def createCurrencyHedgingTag(instrument: InstrumentInfoDto): Option[Tag] = {
> +    Option.when(instrument.fundDetails.isCurrencyHedged.getOrElse(false)) {
> +      createTagFromName(instrument.ccy.toString + "-hedged", fundSmartFilter.currencyHedgingSection)
> +    }
> +  }
> +
>    final protected def buildAllPossibleTagsMap(instrumentsWithDerivedTags: Seq[InstrumentInfoDto], maybeLocale: Option[Locale]): Future[Map[String, Tag]] = {

## A1-1667 — Pass merged instead of already evaluated accumulator

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala; operation: Feat/INV-4568 Automating stitched data computation; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Actually we can just pass the `merged` right? No need `acc` again \(it’s already evaluated anyway\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1684 · comment 681422878 · PR 12467 · 2025-09-10

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-4568 Automating stitched data computation

**Evidence:** anon-1.jsonl:1684 · comment 681422878 · PR 12467 · 2025-09-10

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala`

**Explicit source context (hunk):**

> +
> +  private[managers] def validateSourceGroups(sourceGroups: List[StitchSourceGroupDto]): Unit = {
> +    sourceGroups.foreach { group =>
> +      val allAreMstarIdBased = group.sourceGroup.forall {
> +        case mstar: models.MstarStitchSourceDto => mstar.idType == InstrumentIdType.MSTAR_ID
> +      }
> +      if (!allAreMstarIdBased) {
> +        throw BadRequest(s"Only MSTAR_ID is supported for stitching")
> +      }

## A1-1684 — Prefer checking accumulator first for early stitch termination

**Source stance:** suggestion

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala; operation: Feat/INV-4568 Automating stitched data computation; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Alternative accepted

**Source-preserving request, proposal, or question:**

> I actually prefer we check the acc first and end fast, but I guess this is ok too

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1701 · comment 684353456 · PR 12467 · 2025-09-16

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-4568 Automating stitched data computation

**Evidence:** anon-1.jsonl:1701 · comment 684353456 · PR 12467 · 2025-09-16

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala`

**Explicit source context (hunk):**

> +  ): Future[Map[YearMonth, MstarMonthlyChange]] = {
> +    for {
> +      returns <- calculateGroupedMonthlyReturn(thisSource, l1Ter, l1BaseCcy, maybeEndYmExclusive)
> +      filteredReturns = returns.map(mc => mc.yearMonth -> mc).toMap
> +    } yield filteredReturns ++ acc
> +  }
> +
> +  private[managers] def processStitchedData(
> +    request: ComputeStitchedMonthlyChangesRequest,

## A1-1712 — Use Option.when for CPF/SRS detail

**Source stance:** requested-change

**Context:**

> component: redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/logic/service/SgServiceLogicImpl.scala; operation: Feat/BB-2653 show cpf srs details; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can use Option.when

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1730 · comment 646265076 · PR 12048 · 2025-06-18

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/logic/service/SgServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/BB-2653 show cpf srs details

**Evidence:** anon-1.jsonl:1730 · comment 646265076 · PR 12048 · 2025-06-18

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/logic/service/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> pendingApprovers = taskData.pendingApprovers,
>          supportingDocuments = taskData.payload.supportingDocuments,
> -        approvalValidity = ValidApproval
> +        approvalValidity = ValidApproval,
> +        cpfDetails = if (TradingAccountType.isCpf(plan.tradingAccountType)) singaporeSpecificDetails.flatMap(_.cpfDetails) else None,
> +        srsDetails = if (TradingAccountType.isSrs(plan.tradingAccountType)) singaporeSpecificDetails.flatMap(_.srsDetails) else None
>        )
>      }

## A1-1816 — Portfolio cache unnecessary toList

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala; operation: Resolve INV-4111: Add cache for product portfolio, composition; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need this toList

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1836 · comment 633528937 · PR 11443 · 2025-05-16

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala`

**Explicit source context (pr_title):**

> Resolve INV-4111: Add cache for product portfolio, composition

**Evidence:** anon-1.jsonl:1836 · comment 633528937 · PR 11443 · 2025-05-16

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala`

**Explicit source context (hunk):**

> +      fut.map { portfolios =>
> +        portfolios.flatMap { portfolio =>
> +          extractor(portfolio)
> +            .map((portfolio, _))
> +        }
> +      }
> +    }
> +  }
>  }

## A1-1840 — Use forall rather than validated Option.get

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/ModifyPlanFeePreferenceCmdHandler.scala; operation: TT-6674 Cmd, evts, msgs to update plan fee preferences in Goal Entity; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> In a way it’s already checked so we don’t care if it’s empty here. We can just use forall instead of Option.get

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1860 · comment 664084786 · PR 12350 · 2025-07-31

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/ModifyPlanFeePreferenceCmdHandler.scala`

**Explicit source context (pr_title):**

> TT-6674 Cmd, evts, msgs to update plan fee preferences in Goal Entity

## A1-1860 — Filter sorted return index then head; empty range returns empty

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; operation: Feat/INV-4001 daily nav and performance; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> `dailyReturnIndexPre` is sorted already, so we can just filter by date range \(if set\), then take head?
> 
> Also if data in specified date range, just return empty result instead of throwing?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1880 · comment 630686105 · PR 11805 · 2025-05-09

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-4001 daily nav and performance

## A1-1876 — Filter before DTO except investorType

**Source stance:** requested-change

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Legacy endpoints later cleanup

**Source-preserving request, proposal, or question:**

> Let’s apply this filter before converting to DTO? The investorType filter no choice we have to do after.
> 
> These endpoints should be obsolete after productline, but I guess we can clean them up separately

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1896 · comment 632776311 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

## A1-1879 — Take head before converting all

**Source stance:** requested-change

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Take head first right? Why waste time converting for all?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1899 · comment 632776735 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

**Evidence:** anon-1.jsonl:1899 · comment 632776735 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      val grouped = dtos.groupBy(_.portfolioType)
> +      ModelPortfolioGroupedResult(
> +        groupedPortfolios = grouped.map(s => s._1 -> s._2.sortBy(_.currentAllocationTarget.targetBondRatio))
> +      )
> +    }
>    }
>  
>    override def updatePortfolioDetails(request: requests.UpdatePortfolioDetailsRequest): Future[Done] = {

## A1-1898 — Filter then maxByOption

**Source stance:** suggestion

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; operation: Feat/INV-4231 safe guard price change; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> filter first then use maxByOption instead?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1918 · comment 630678322 · PR 11701 · 2025-05-09

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-4231 safe guard price change

## A1-1907 — Deduplicate MStar documents by documentId

**Source stance:** open-question

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/MstarInstrumentDocumentManager.scala; operation: [INV-4632] feat(instrument): remove kiid urls and support fetch doc by isin from mstar; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Should we dedup by `documentId` in the `MstarDocument`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1927 · comment 667768118 · PR 12403 · 2025-08-08

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/MstarInstrumentDocumentManager.scala`

**Explicit source context (pr_title):**

> [INV-4632] feat(instrument): remove kiid urls and support fetch doc by isin from mstar

**Evidence:** anon-1.jsonl:1927 · comment 667768118 · PR 12403 · 2025-08-08

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/MstarInstrumentDocumentManager.scala`

**Explicit source context (hunk):**

> +          docs <- docsFuture
> +          docsByIsin <- isinDocsFuture
> +        } yield {
> +          MstarHistoricalDocuments(
> +            documents = (docs.documents ++ docsByIsin.documents).distinctBy(_.documentId)
> +          )
> +        }
> +      }
>        latestDocuments = mstarHistoricalDocuments.documents.foldLeft(Map.empty[FundDocumentType, MstarDocument]) {

## A1-1921 — Use forall

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: [INV-4569] feat(marketdata): support source of price update; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can use `forall`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1941 · comment 665730890 · PR 12355 · 2025-08-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-4569] feat(marketdata): support source of price update

**Evidence:** anon-1.jsonl:1941 · comment 665730890 · PR 12355 · 2025-08-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (hunk):**

> -      } else {
> -        fetchedNotSeenPriceDates
> -      }
> +      val filteredPriceDatesToBeUpdated = fetchedPrices.filter { price =>
> +          existingPriceInfo.get(price.priceDate) match {
> +            case None                         => true // New date
> +            case Some((existingValue, Mstar)) => existingValue != price.value // All Mstar prices changed
> +            case Some((_, Manual))            => forceOverrideManualPrice.contains(true) // All Manual prices can be overridden
> +          }

## A1-1933 — Unapply recurring frequency/amount tuple instead of _1 _2

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgB2bNotificationManager.scala; operation: [INV-4134] feat(advisory): handle recurring edit and stop investment b2b notifications; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> You can use it like this to avoid \_1 \_2 below
> 
> ```
> (maybeRecurringFrequencyDetail, maybeRecurringAmount) = if (isStopRecurringWithNoInvestments) {
>  ...
> } else {
>  ...
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1953 · comment 630172564 · PR 11757 · 2025-05-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgB2bNotificationManager.scala`

**Explicit source context (pr_title):**

> [INV-4134] feat(advisory): handle recurring edit and stop investment b2b notifications

## A1-1954 — Expression now simple if/else

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/helper/ExploreHelper.scala; operation: [INV-4379] feat(advisory): support locale based image url; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This is just if else now

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1975 · comment 661078258 · PR 12289 · 2025-07-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/helper/ExploreHelper.scala`

**Explicit source context (pr_title):**

> [INV-4379] feat(advisory): support locale based image url

## A1-2010 — Do not collect large planId list without need

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala; operation: [INV-1946] feat(rebalance): remove taa entity; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Why do we need to collect all the planIds here? It would be quite large use of memory, but really for nothing right?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2029 · comment 657158800 · PR 12157 · 2025-07-15

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala`

**Explicit source context (pr_title):**

> [INV-1946] feat(rebalance): remove taa entity

## A1-2011 — Keep count only instead of full UUID list

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala; operation: [INV-1946] feat(rebalance): remove taa entity; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> If we just want count, then keep only count. No need to keep the full UUID list

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:2030 · comment 657167695 · PR 12157 · 2025-07-15

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala`

**Explicit source context (pr_title):**

> [INV-1946] feat(rebalance): remove taa entity

## A1-2018 — Avoid Option.get; filter fold/getOrElse

**Source stance:** requested-change

**Context:**

> component: composition-impl/src/main/scala/com/endowus/silver/composition/impl/logic/service/impl/ServiceLogicImpl.scala; operation: [INV-3999] feat(composition): pull mstar data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Avoid Option.get as much as you can.
> 
> Here you can use filter & fold/getOrElse instead

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2037 · comment 655814705 · PR 12004 · 2025-07-11

Source path: `composition-impl/src/main/scala/com/endowus/silver/composition/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-3999] feat(composition): pull mstar data

**Evidence:** anon-1.jsonl:2037 · comment 655814705 · PR 12004 · 2025-07-11

Source path: `composition-impl/src/main/scala/com/endowus/silver/composition/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +            .toSet
> +        }
> +      } { ids =>
> +        Future.successful(ids.toSet)
> +      }
> +  }
> +
>  }

## A1-2019 — Mapping withFilter produces List[WithFilter] rather than instrument list

**Source stance:** observed-defect

**Context:**

> component: composition-impl/src/main/scala/com/endowus/silver/composition/impl/utils/DownloaderHelper.scala; operation: [INV-3999] feat(composition): pull mstar data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This looks wrong. Wouldn’t `validInstruments` of type `List[WithFilter]` here, but we actually want `List[InstrumentInfoDto]`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2038 · comment 655818941 · PR 12004 · 2025-07-11

Source path: `composition-impl/src/main/scala/com/endowus/silver/composition/impl/utils/DownloaderHelper.scala`

**Explicit source context (pr_title):**

> [INV-3999] feat(composition): pull mstar data

## A1-2054 — Group RPC by plan and maxBy createdAt status directly into map

**Source stance:** suggestion

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/GoalEdgeLogicImpl.scala; operation: Feat/EN-4720 additional fields goal overview api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Why don’t we just collect the map here?
> 
> ```
> latestRpcStatusesByPlanId = recommendedPortfolioChanges
>   .groupBy(_.planId).view
>   .mapValues(_.maxBy(_.createdAt).status)
>   .toMap
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2074 · comment 619395014 · PR 11541 · 2025-04-14

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/GoalEdgeLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/EN-4720 additional fields goal overview api

## A1-2129 — Prepend if ordering irrelevant; append slower

**Source stance:** requested-change

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/SkipPlanFeeChargeHelper.scala; operation: [INV-3720] feat(advisory, charge): enable fee charge for rf corporate client holding non rf funds; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We don’t care about ordering right? Let’s prepend instead of append, otherwise it’s much slower

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2146 · comment 573399056 · PR 10434 · 2024-12-04

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/SkipPlanFeeChargeHelper.scala`

**Explicit source context (pr_title):**

> [INV-3720] feat(advisory, charge): enable fee charge for rf corporate client holding non rf funds

**Evidence:** anon-1.jsonl:2146 · comment 573399056 · PR 10434 · 2024-12-04

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/SkipPlanFeeChargeHelper.scala`

**Explicit source context (hunk):**

> +
> +    val tradingAccountTypes = diyPlanProfiles.map(_.tradingAccountType).toSet
> +
> +    for {
> +      allowedInstrumentsByAccountType <- fetchAllowedInstruments(tradingAccountTypes)
> +      classification <- Source(diyPlanProfiles)
> +        .mapAsync(parallelism = 4)(profile => classifyDiyProfile(profile, allowedInstrumentsByAccountType))
> +        .runWith(Sink.fold(PlanProfileClassification(Seq.empty, Seq.empty, Seq.empty)) {
> +          case (classification, Success(Left(rfProfile))) =>

## A1-2296 — Pattern-match only context when rest same

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgB2bNotificationManager.scala; operation: [INV-3765] feat(adviosry): create apis for b2b approval notifcations; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Since this is same for both, better to pattern match only to resolve the context

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2313 · comment 598613332 · PR 11000 · 2025-02-21

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgB2bNotificationManager.scala`

**Explicit source context (pr_title):**

> [INV-3765] feat(adviosry): create apis for b2b approval notifcations

**Evidence:** anon-1.jsonl:2313 · comment 598613332 · PR 11000 · 2025-02-21

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgB2bNotificationManager.scala`

**Explicit source context (hunk):**

> +        case ActorRole.FA_MANAGER => B2bEmployeeContext(tenantId = tenantId)
> +      }
> +    )
> +  }
> +
> +  private def sendNotificationToFAManagerAndCopyToFa(
> +    managerId: UUID,
> +    taskId: UUID,
> +    communicationContext: CommunicationContext,

## A1-2308 — Set tags collapse duplicated sector/asset labels before display List

**Source stance:** observed-defect

**Context:**

> component: instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/InstrumentTags.scala; operation: Feat/INV-4007 new display tags and refactor; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Consider sector suffix in tag names

**Source-preserving request, proposal, or question:**

> `instrument.endowusDetails.tags` is a Set before getting converted to List\[String\] for displayTags, so looks like this won’t work?
> 
> Maybe we include “-sector” in all these sector tags?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2325 · comment 636029118 · PR 11846 · 2025-05-22

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/InstrumentTags.scala`

**Explicit source context (pr_title):**

> Feat/INV-4007 new display tags and refactor

## A1-2316 — FE-added two filters should sort last

**Source stance:** open-question

**Context:**

> component: instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/InstrumentTags.scala; operation: Feat/INV-4007 new display tags and refactor; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> The 2 added by FE should be last right?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:2333 · comment 645300356 · PR 11846 · 2025-06-16

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/InstrumentTags.scala`

**Explicit source context (pr_title):**

> Feat/INV-4007 new display tags and refactor

## A1-2317 — Static FilterOrder lookup; dummy-section helper may unnecessary

**Source stance:** suggestion

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/InstrumentTagsHelper.scala; operation: Feat/INV-4007 new display tags and refactor; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Missing order already-1

**Source-preserving request, proposal, or question:**

> I guess instrument svc doesn’t care about filtering, but why don’t follow similar approach as advisory here? To lookup the section ordering against the static `FilterOrder`
> 
> Also we don’t need `getTagsFromDummySection` right? The `getFilterOrderingBySection` already can return -1?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2334 · comment 645306067 · PR 11846 · 2025-06-16

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/InstrumentTagsHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-4007 new display tags and refactor

## A1-2320 — Regional filterOrder alone controls allowed sections then extra skips

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartInstrumentTagFilter.scala; operation: Feat/INV-4007 new display tags and refactor; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Remove redundant SectionNames diff/hide/top-up machinery

**Source-preserving request, proposal, or question:**

> _<assuming we follow region specific approach>_
> 
> Also we currently defines both `SectionNames` and `FilterOrder`. Then diff them to find `FilterSectionsToHide`. Then support top up to `FilterSectionsToHide`, either via `additionalSections` or region specific logic \(to remove `CiesSectionName` for SG\)
> 
> Does it feel cleaner if we define only region specific `FilterOrder`?
> 
> * each `FundSmartFilter` defines its own `filterSectionsOrder`
> * remove `getSectionsToSkip` in `FundSmartFilter`
> * refactor `generateFilters`:
> 
>     * sectionsToSkip will only include additional skips \(i.e. InvestorType section if retail\)
>     * additional check for sections in `filterSectionsOrder` only
>     
> 
> ```
> uniqueSections
>   .filter(s => filterSectionsOrder.contains(s.name))
>   .filter(s => !sectionsToSkip.contains(s.name))
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2337 · comment 646263988 · PR 11846 · 2025-06-18

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartInstrumentTagFilter.scala`

**Explicit source context (pr_title):**

> Feat/INV-4007 new display tags and refactor

## A1-2348 — Use collect

**Source stance:** requested-change

**Context:**

> component: rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculator.scala; operation: Resolve INV-3823: Changes to skip rebate distribution for b2b clients.; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Use collect is better

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2363 · comment 595678902 · PR 11013 · 2025-02-12

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculator.scala`

**Explicit source context (pr_title):**

> Resolve INV-3823: Changes to skip rebate distribution for b2b clients.

**Evidence:** anon-1.jsonl:2363 · comment 595678902 · PR 11013 · 2025-02-12

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculator.scala`

**Explicit source context (hunk):**

> +        for {
> +          isCustomerEligible <- isCustomerEligibleForRebates(planMarketValue.customerId)
> +        } yield Option.when(isCustomerEligible)(planMarketValue)
> +      )
> +      .collect {
> +        case Some(planMarketValue) => planMarketValue
> +      }
>        .foldAsync((mutable.Map[UUID, PlanMarketValue](), BigDecimal(0))) {
>          case ((planMvById, accumulatedMv), planMv) =>

## A1-2356 — Use exists account type instead of map-toSet

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/BrokerAccountHelpers.scala; operation: Feat/TT-5730 advisory create broker account; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No need to map and toSet. Can just check using `exists(_.tradingAccountType == tradingAccountType)`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2371 · comment 595276261 · PR 11089 · 2025-02-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/BrokerAccountHelpers.scala`

**Explicit source context (pr_title):**

> Feat/TT-5730 advisory create broker account

**Evidence:** anon-1.jsonl:2371 · comment 595276261 · PR 11089 · 2025-02-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/BrokerAccountHelpers.scala`

**Explicit source context (hunk):**

> +        .findActiveBrokerAccountsForCustomer(customerId)
> +        .invoke()
> +        .withRetry(AlwaysRetryOnException)
> +
> +      _ <- if(!brokerAccounts.exists(_.tradingAccountType == tradingAccountType)) {
> +        logger.info(s"Creating mccy broker account for trading account type ${tradingAccountType} for customerId $customerId")
> +        brokerService.createMccyBrokerAccount.invoke(
> +          CreateMccyBrokerAccountRequest(
> +            customerId = customerId,

## A1-2362 — Use collect instead of filter/map

**Source stance:** requested-change

**Context:**

> component: broker-impl/src/main/scala/com/endowus/silver/broker/impl/loaders/files/uobkh/outgoing/transfer/UobkhInstrumentTransferFileManager.scala; operation: Feat/INV-3708/inter plan transfer sg broker; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Use collect instead of filter\+map

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2377 · comment 581758710 · PR 10596 · 2024-12-30

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/loaders/files/uobkh/outgoing/transfer/UobkhInstrumentTransferFileManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-3708/inter plan transfer sg broker

**Evidence:** anon-1.jsonl:2377 · comment 581758710 · PR 10596 · 2024-12-30

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/loaders/files/uobkh/outgoing/transfer/UobkhInstrumentTransferFileManager.scala`

**Explicit source context (hunk):**

> )
> -        .map(_.map(idWithTx => Transaction.toDto(idWithTx._1, idWithTx._2)))
> -
> +        .map(_.collect {
> +          // [INV-3708] This JDBC query must always be exclusive from that in UobkhInterAccountInstrumentTransferFileManager to prevent an intersection of transactions from being exported.
> +          case (id, tx) if tx.instrumentTransferDetail.exists(_.counterpartyDetails.isExternal) =>
> +            Transaction.toDto(id, tx)
> +        })
>        brokerAccounts <- brokerAccountJdbcRepository.findBrokerAccountsMapByBrokers(brokers = Broker.regionToBrokersMap(SilverRegion.Sg))

## A1-2365 — Only project nonempty goal when requested; filter empty monthlyResults

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalmodify/sg/SgGoalModifySummaryBehaviour.scala; operation: [INV-4487] fix(advisory): SG/HK hide fs modify goal summary projection if insufficient historical data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ```scala
> maybeProjection <- Option.whenOptFut(shouldShowProjection && !isEmptyGoal) {
>   ...
> }.map(_.filter(_.monthlyResults.nonEmpty))
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2380 · comment 651309169 · PR 12141 · 2025-06-30

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalmodify/sg/SgGoalModifySummaryBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-4487] fix(advisory): SG/HK hide fs modify goal summary projection if insufficient historical data

## A1-2405 — Map optional fee config and Option.when positive applied fee instead of get

**Source stance:** suggestion

**Context:**

> component: investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala; operation: Resolve INV-3516: Changes to flow investment transaction fees to transaction svc.; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can avoid Option.get
> 
> ```
> transactionFee.map(_.config).flatMap(feeConfig -> Option.when(accumulatedAppliedFeeAmount > 0) { ... })
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2425 · comment 581739965 · PR 10415 · 2024-12-30

Source path: `investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala`

**Explicit source context (pr_title):**

> Resolve INV-3516: Changes to flow investment transaction fees to transaction svc.

## A1-2421 — Build optional AI-only mismatch error then flatten blocked-error list

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala; operation: Feat/INV-3794 extra validation before submit for approval; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ```
> maybeAiOnlyError = aiOnlyInstruments.headOption(_ => HasAIInstrumentsMismatchedWithInvestorType(aiOnlyInstruments.map(_.id)))
> approvalBlockedErrors = List(maybeAiOnlyError, .., ..).flatten
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2441 · comment 583716018 · PR 10777 · 2025-01-09

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Explicit source context (pr_title):**

> Feat/INV-3794 extra validation before submit for approval

## A1-2434 — Use statuses.forall(isTerminal) rather than confusing transfer helper

**Source stance:** suggestion

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/CancelInstrumentTransferCmdHandler.scala; operation: [INV-3710] feat(inter plan transfer): handle comms for transfer instructions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> A bit weird to see this method `InstrumentTransfer.isTransferInstructionTerminal(distinctStatuses)`
> 
> Maybe just `distinctStatuses.forall(isTerminal)` or sth like that?
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2455 · comment 578131384 · PR 10435 · 2024-12-16

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/CancelInstrumentTransferCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3710] feat(inter plan transfer): handle comms for transfer instructions

## A1-2435 — No distinct needed before forall

**Source stance:** requested-change

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/CancelInstrumentTransferCmdHandler.scala; operation: [INV-3710] feat(inter plan transfer): handle comms for transfer instructions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No need to distinct either

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2456 · comment 578131500 · PR 10435 · 2024-12-16

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/CancelInstrumentTransferCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3710] feat(inter plan transfer): handle comms for transfer instructions

**Evidence:** anon-1.jsonl:2456 · comment 578131500 · PR 10435 · 2024-12-16

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/CancelInstrumentTransferCmdHandler.scala`

**Explicit source context (hunk):**

> +          updatedInstrumentTransfers = updatedInstrumentTransfers,
> +          planProfile = planProfile,
> +          finishedAt = cmd.cancelledAt
> +        )
> +
> +        Effect
> +          .persist(
> +            events.toList
> +          )

## A1-2446 — Avoid eager return via Nil/head pattern then optional counterparty match

**Source stance:** suggestion

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala; operation: [INV-3710] feat(inter plan transfer): handle comms for transfer instructions; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Common code can serve both events; invalid cases log and Done

**Source-preserving request, proposal, or question:**

> Generally we want to avoid eager returns like this. Scala treats `return` differently. Here it works but most of the time can be avoided.
> 
> Maybe we can write it as sth like this \(which can be extracted as common code between these 2 events too\)
> 
> ```
> instrumentTransfers match {
>   case Nil =>
>     // log error cannot proceed
>     Future.successful(Done)
>   case firstInstrumentTransfer :: _ =>
>     (InstrumentTransfer.getInternalCounterpartyBrokerAccountId(firstInstrumentTransfer), InstrumentTransfer.getInternalCounterpartyPlanId(firstInstrumentTransfer)) match {
>       case (Some(counterpartyBrokerAccountId), Some(counterpartyPlanId)) =>
>         // blah
>       case _ =>
>         // log error cannot proceed
>         Future.successful(Done)
>     }
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2467 · comment 579363042 · PR 10435 · 2024-12-18

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> [INV-3710] feat(inter plan transfer): handle comms for transfer instructions

## A1-2453 — Use map.get(key).contains

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/WorkflowEngineHelpers.scala; operation: Resolve INV-4055: Changes to validate existing goal names with names from pending approval workflows; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> `.get(key).contains` instead

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2474 · comment 608487890 · PR 11306 · 2025-03-13

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/WorkflowEngineHelpers.scala`

**Explicit source context (pr_title):**

> Resolve INV-4055: Changes to validate existing goal names with names from pending approval workflows

**Evidence:** anon-1.jsonl:2474 · comment 608487890 · PR 11306 · 2025-03-13

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/WorkflowEngineHelpers.scala`

**Explicit source context (hunk):**

> }
>  
> +  def getGoalNamesFromPendingWorkflowsForCustomer(employeeId: UUID, customerId: UUID): Future[Set[String]] = {
> +    workflowEngineService.SgWorkflowEngineApi.getTasksByCreator(employeeId, None, Some(TaskType.CREATE_GOAL)).map { tasks =>
> +      tasks.filter(_.references.get(WorkflowReferenceKey.CustomerId).contains(customerId.toString))
> +        .flatMap(_.references.get(WorkflowReferenceKey.GoalName))
> +        .toSet
> +    }
> +  }

## A2-0002 — PortfolioUnderlyingManager: This is existing code, but let’s double check if we should filter only active here

**Source stance:** open-question

**Context:**

> PR 10991 (Feat/EN-4318 portfolio aaa bff integration), portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala; original row 2.

**Concern stated in the source:** Whether portfolio underlying plan lookup should include only active plans is unresolved.

**Source-preserving request, proposal, or question:**

> This is existing code, but let’s double check if we should filter only active here

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:2 · comment 607197256 · PR 10991 · 2025-03-12

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

**Evidence:** anon-2.jsonl:2 · comment 607197256 · PR 10991 · 2025-03-12

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

**Explicit source context (pr_title):**

> Feat/EN-4318 portfolio aaa bff integration

## A2-0003 — PortfolioUnderlyingManager: Let’s use sort \+ reverse instead

**Source stance:** requested-change

**Context:**

> PR 10991 (Feat/EN-4318 portfolio aaa bff integration), portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala; original row 3.

**Source-preserving request, proposal, or question:**

> Let’s use sort \+ reverse instead

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:3 · comment 607199508 · PR 10991 · 2025-03-12

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

**Evidence:** anon-2.jsonl:3 · comment 607199508 · PR 10991 · 2025-03-12

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

**Explicit source context (pr_title):**

> Feat/EN-4318 portfolio aaa bff integration

## A2-0007 — HkPortfolioMetricsManager: AnnualYield is fetched and calculated based on instrument data, regardless of goalType. I think we don’t need to this extra filter

**Source stance:** explanation

**Context:**

> PR 10991 (Feat/EN-4318 portfolio aaa bff integration), portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/hk/HkPortfolioMetricsManager.scala; original row 7.

**Concern stated in the source:** AnnualYield uses instrument data regardless of goalType; the additional filter appears unnecessary.

**Source-preserving request, proposal, or question:**

> AnnualYield is fetched and calculated based on instrument data, regardless of goalType. I think we don’t need to this extra filter

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:7 · comment 607204102 · PR 10991 · 2025-03-12

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/hk/HkPortfolioMetricsManager.scala`

**Evidence:** anon-2.jsonl:7 · comment 607204102 · PR 10991 · 2025-03-12

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/hk/HkPortfolioMetricsManager.scala`

**Explicit source context (pr_title):**

> Feat/EN-4318 portfolio aaa bff integration

## A2-0026 — BackfillPlanProfileTenantIdCmdHandler: Let’s also return without events if same tenantId already exists. Then we won’t have duplicated events, as the subscriber might process a ...

**Source stance:** requested-change

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/BackfillPlanProfileTenantIdCmdHandler.scala; original row 26.

**Concern stated in the source:** A subscriber can process a task more than once and generate duplicate tenant-backfill events.

**Source-preserving request, proposal, or question:**

> Let’s also return without events if same tenantId already exists. Then we won’t have duplicated events, as the subscriber might process a task multiple times.

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:26 · comment 609026873 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/BackfillPlanProfileTenantIdCmdHandler.scala`

**Evidence:** anon-2.jsonl:26 · comment 609026873 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/BackfillPlanProfileTenantIdCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0061 — TagTransactionAdvisoryClassification: L32 returns tuple of `(transactionId, customerId)`

**Source stance:** suggestion

**Context:**

> PR 8453 (Feat/INV-2101 transaction backfill scripts), amend-scripts/src/main/scala/transaction/TagTransactionAdvisoryClassification.scala; original row 61.

**Source-preserving request, proposal, or question:**

> L32 returns tuple of `(transactionId, customerId)`

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:61 · comment 476110092 · PR 8453 · 2024-02-27

Source path: `amend-scripts/src/main/scala/transaction/TagTransactionAdvisoryClassification.scala`

**Evidence:** anon-2.jsonl:61 · comment 476110092 · PR 8453 · 2024-02-27

Source path: `amend-scripts/src/main/scala/transaction/TagTransactionAdvisoryClassification.scala`

**Explicit source context (hunk):**

> +            customerTransactions.filter(s => List(
> +                TransactionType.REBALANCE,
> +                TransactionType.ASSET_TRANSFER,
> +                TransactionType.INVESTMENT
> +              ).contains(s.transactionType))
> +      })
> +      .mapConcat(identity)

**Evidence:** anon-2.jsonl:61 · comment 476110092 · PR 8453 · 2024-02-27

Source path: `amend-scripts/src/main/scala/transaction/TagTransactionAdvisoryClassification.scala`

**Explicit source context (pr_title):**

> Feat/INV-2101 transaction backfill scripts

## A2-0066 — HkTradingSimulationHelper: Actually Set.map will return a new set…. so it’s better to use `errors.exists(_.category == SuitabilityBreach)` instead

**Source stance:** explanation

**Context:**

> PR 5423 (Refactor (compliance/investment): Refactor RestrictionError/RestrictionWarning to include categories.), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/HkTradingSimulationHelper.scala; original row 66.

**Concern stated in the source:** Set.map creates a new set.

**Source-preserving request, proposal, or question:**

> Actually Set.map will return a new set…. so it’s better to use `errors.exists(_.category == SuitabilityBreach)` instead

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:66 · comment 374972542 · PR 5423 · 2023-03-06

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/HkTradingSimulationHelper.scala`

**Evidence:** anon-2.jsonl:66 · comment 374972542 · PR 5423 · 2023-03-06

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/HkTradingSimulationHelper.scala`

**Explicit source context (pr_title):**

> Refactor (compliance/investment): Refactor RestrictionError/RestrictionWarning to include categories.

## A2-0078 — FixV3DividendsTransactions: Why don’t we add more filter here, to reduce the payload size? Also maybe groupBy customerId so that we don’t repeat the query again?

**Source stance:** suggestion

**Context:**

> PR 7209 ([INV-1976] feat(amend): Scripts to amend dividends, redemption and deleted order transactions), amend-scripts/src/main/scala/transaction/FixV3DividendsTransactions.scala; original row 78.

**Concern stated in the source:** Repeated queries and oversized payloads may be avoided by additional filters and grouping by customerId.

**Source-preserving request, proposal, or question:**

> Why don’t we add more filter here, to reduce the payload size? Also maybe groupBy customerId so that we don’t repeat the query again?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:78 · comment 436531435 · PR 7209 · 2023-10-17

Source path: `amend-scripts/src/main/scala/transaction/FixV3DividendsTransactions.scala`

**Evidence:** anon-2.jsonl:78 · comment 436531435 · PR 7209 · 2023-10-17

Source path: `amend-scripts/src/main/scala/transaction/FixV3DividendsTransactions.scala`

**Explicit source context (pr_title):**

> [INV-1976] feat(amend): Scripts to amend dividends, redemption and deleted order transactions

## A2-0080 — ExportFeeEstimation: Are we using only 1st customerId and 1st broker that matches tradingAccount? Need to groupBy customer first right?

**Source stance:** open-question

**Context:**

> PR 6185 (Resolve INV-1298: Script to convert fee query response to csv), amend-scripts/src/main/scala/charge/ExportFeeEstimation.scala; original row 80.

**Concern stated in the source:** Selecting only the first customer/broker matching tradingAccount may lose grouping by customer.

**Source-preserving request, proposal, or question:**

> Are we using only 1st customerId and 1st broker that matches tradingAccount? Need to groupBy customer first right?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:80 · comment 402496322 · PR 6185 · 2023-06-12

Source path: `amend-scripts/src/main/scala/charge/ExportFeeEstimation.scala`

**Evidence:** anon-2.jsonl:80 · comment 402496322 · PR 6185 · 2023-06-12

Source path: `amend-scripts/src/main/scala/charge/ExportFeeEstimation.scala`

**Explicit source context (pr_title):**

> Resolve INV-1298: Script to convert fee query response to csv

## A2-0093 — InstrumentTransferHelper: Existing code would match by specified brokerAccountId too.

**Source stance:** explanation

**Context:**

> PR 11820 (TT-5817 Use case for full transfer plan out), trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/InstrumentTransferHelper.scala; original row 93.

**Concern stated in the source:** Existing extraction filters by brokerAccountId and availableUnits > 0.

**Source-preserving request, proposal, or question:**

> Existing code would match by specified brokerAccountId too.
> 
> It is using
> 
> ```
> def extractAvailableUnits(instrumentBalances: List[InstrumentBalance], brokerAccountId: BrokerAccountId): Map[String, BigDecimal] = {
>   instrumentBalances
>     .filter(_.brokerAccountId == brokerAccountId)
>     .collect {
>       case instrumentBalance if instrumentBalance.availableUnits > BigDecimal(0) =>
>         (instrumentBalance.instrumentId, instrumentBalance.availableUnits)
>     }
>     .toMap
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:93 · comment 632627765 · PR 11820 · 2025-05-14

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/InstrumentTransferHelper.scala`

**Evidence:** anon-2.jsonl:93 · comment 632627765 · PR 11820 · 2025-05-14

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/InstrumentTransferHelper.scala`

**Explicit source context (pr_title):**

> TT-5817 Use case for full transfer plan out

## A2-0111 — B2BProductHelpers: Do we need Option here? Maybe just use `task.payload.exists` above and return boolean here

**Source stance:** open-question

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/B2BProductHelpers.scala; original row 111.

**Source-preserving request, proposal, or question:**

> Do we need Option here? Maybe just use `task.payload.exists` above and return boolean here

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:111 · comment 587735288 · PR 10896 · 2025-01-20

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/B2BProductHelpers.scala`

**Evidence:** anon-2.jsonl:111 · comment 587735288 · PR 10896 · 2025-01-20

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/B2BProductHelpers.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0140 — InvestOnceCmdHandler: Nit: `maybeInvestmentRequestCreationApprovedEvt.toList` is sufficient

**Source stance:** suggestion

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala; original row 140.

**Source-preserving request, proposal, or question:**

> Nit: `maybeInvestmentRequestCreationApprovedEvt.toList` is sufficient

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:140 · comment 601749287 · PR 10896 · 2025-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala`

**Evidence:** anon-2.jsonl:140 · comment 601749287 · PR 10896 · 2025-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0143 — StopRecurringInvestmentScheduleCmdHandler: Same here and the cmd handler below. Can use Option#toList

**Source stance:** suggestion

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/StopRecurringInvestmentScheduleCmdHandler.scala; original row 143.

**Source-preserving request, proposal, or question:**

> Same here and the cmd handler below. Can use Option#toList

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:143 · comment 601752486 · PR 10896 · 2025-03-04

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/StopRecurringInvestmentScheduleCmdHandler.scala`

**Evidence:** anon-2.jsonl:143 · comment 601752486 · PR 10896 · 2025-03-04

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/StopRecurringInvestmentScheduleCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0275 — FeeInstructionHelper: Since it’s a little bit tricky, maybe put a comment here explaining that we want `inclusive maxBefore` which is not available. Author of scala TreeMap seem...

**Source stance:** suggestion

**Context:**

> PR 10097 ([EN-3954] (charge) integrate fee instruction with context), charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/FeeInstructionHelper.scala; original row 275.

**Concern stated in the source:** TreeMap lacks inclusive maxBefore; the cited workaround reverses sorting and uses inclusive minAfter.

**Source-preserving request, proposal, or question:**

> Since it’s a little bit tricky, maybe put a comment here explaining that we want `inclusive maxBefore` which is not available. Author of scala TreeMap seems to expect user to sort in reverse and use `minAfter` \(which is inclusive\) instead

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:275 · comment 552738324 · PR 10097 · 2024-10-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/FeeInstructionHelper.scala`

**Evidence:** anon-2.jsonl:275 · comment 552738324 · PR 10097 · 2024-10-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/FeeInstructionHelper.scala`

**Explicit source context (pr_title):**

> [EN-3954] (charge) integrate fee instruction with context

## A2-0282 — PlanFeeInstructionEntity: The entity state is default with empty fee instructions, it means the plan always exists, just without any data. Modelling it this way means you can’t ...

**Source stance:** open-question

**Context:**

> PR 10030 ([EN-3952] (charge) Create new PlanFeeInstructionEntity), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala; original row 282.

**Concern stated in the source:** Empty default instructions cannot distinguish never-initialized from upserted-then-deleted plan state.

**Source-preserving request, proposal, or question:**

> The entity state is default with empty fee instructions, it means the plan always exists, just without any data. Modelling it this way means you can’t distinguish between a uninitialized plan vs a plan with upserted-then-deleted fee instructions.
> 
> If we care enough about this, then we probably should make state a sealed trait, default with case object NotInitialized, otherwise it’s case class Initialized\(feeInstructions\). Then you can throw for GetCmd/DeleteCmd on NotInitialized. And no-op without error if deleting already deleted fee instruction for Initialized, and even throw if deleting last entry for Initialized \(to ensure there’s always an entry to support the fee rate query\)

**Conditions and limits:**

- The sealed NotInitialized/Initialized state is conditional on caring about that distinction; no-op deletion and last-entry rejection are proposals within that model.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:282 · comment 552218834 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Evidence:** anon-2.jsonl:282 · comment 552218834 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Explicit source context (pr_title):**

> [EN-3952] (charge) Create new PlanFeeInstructionEntity

## A2-0300 — BackfillPlanInvestmentCmdHandler: I think this could be confusing to read, e.g. what if existing but doesn’t match the resolve? Well it cannot be, due to how we resolve. So mayb...

**Source stance:** suggestion

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala; original row 300.

**Concern stated in the source:** The existing branching appears to imply a possible existing-but-different resolved value, although resolution rules make it impossible.

**Source-preserving request, proposal, or question:**

> I think this could be confusing to read, e.g. what if existing but doesn’t match the resolve? Well it cannot be, due to how we resolve. So maybe we can write this part differently
> 
> ```
> val maybeInitialInvestmentBackfilledEvt = plan.initialInvestmentRequest match {
>   case None => Some(....)
>   case Some(_) => None
> }
> 
> val maybeRecurringInvestmentScheduleBackfilledEvt = plan.recurringInvestmentSchedule.flatMap { schedule =>
>   schedule.fundingInstructions match {
>     case None => Some(...)
>     case Some(_) => None
>   }
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:300 · comment 570115418 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala`

**Evidence:** anon-2.jsonl:300 · comment 570115418 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0314 — BaseServiceLogicImpl: No need this filter

**Source stance:** suggestion

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; original row 314.

**Source-preserving request, proposal, or question:**

> No need this filter

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:314 · comment 570860833 · PR 10417 · 2024-11-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:314 · comment 570860833 · PR 10417 · 2024-11-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +        .map(goalId => Source(List(goalId)))
> +        .getOrElse(goalJdbcRepository.sourceAllGoalIds)
> +        .mapAsync(2)(issueCommand)
> +        .runWithReporting(
> +          "Backfilled investment amounts for all plans.",
> +        )
> +    } yield Done

**Evidence:** anon-2.jsonl:314 · comment 570860833 · PR 10417 · 2024-11-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0365 — GoalSupportingDataJdbcDbHandler: I suppose this would return 0, if row already exists? Do we log error or something cuz we don’t expect that to happen?

**Source stance:** open-question

**Context:**

> PR 10335 (Feat/INV-3508 goal create projections), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataJdbcDbHandler.scala; original row 365.

**Concern stated in the source:** An unexpected duplicate insert returning 0 may need error logging; outcome remains a question.

**Source-preserving request, proposal, or question:**

> I suppose this would return 0, if row already exists? Do we log error or something cuz we don’t expect that to happen?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:365 · comment 565310581 · PR 10335 · 2024-11-15

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataJdbcDbHandler.scala`

**Evidence:** anon-2.jsonl:365 · comment 565310581 · PR 10335 · 2024-11-15

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 goal create projections

## A2-0385 — BaseAdvisoryServiceE4s: If In is not tuple, then we don’t need to define `handle` or `toTupled`

**Source stance:** suggestion

**Context:**

> PR 10184 ([INV-3559] feat(bff, advisory): Portfolio Builder Portfolio Summary), advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala; original row 385.

**Concern stated in the source:** Endpoint In that is not a tuple does not need handle/toTupled definitions.

**Source-preserving request, proposal, or question:**

> If In is not tuple, then we don’t need to define `handle` or `toTupled`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:385 · comment 562904670 · PR 10184 · 2024-11-08

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Evidence:** anon-2.jsonl:385 · comment 562904670 · PR 10184 · 2024-11-08

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> [INV-3559] feat(bff, advisory): Portfolio Builder Portfolio Summary

## A2-0400 — SgFundDetailsManager: Let’s structure these as

**Source stance:** suggestion

**Context:**

> PR 10183 ([INV-3558] feat(bff, advisory): Portfolio Builder Fund Details), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundDetailsManager.scala; original row 400.

**Concern stated in the source:** Let’s structure these as

```
// for existing B2C (customerId is optional) ->> to be called by SgFundSmartManagerV3
def getInstrumentDetailsForCustomer(...) {
  // keep existing logic here, i.e. switch on maybeCustomerId
  // if customerId:
  // - filterInstrumentDataForCustomer: remove Ai/Pi sensitive data depending on customer
  // - checkInstrumentAccessForCustomer: user allowedInstrumentsBasedOnCorporateProfile
  // - validateInstrumentDueDiligenceDetails: block NoDueDiligence
  //
  // if no customerId:
  // - filterInstrumentDataForCustomer: remove Ai/Pi sensitive data always
  // - checkInstrumentAccessForCustomer: use whitelisted goal types only
  // - validateInstrumentDueDiligenceDetails: use whitelisted only
}

// for no-auth endpoint ->> to be called by SgFundSmartManagerV3 (not SgTenantAwareInstrumentManager, since it's not specific to tenant')
def getInstrumentDetails(...) {
  // should behave almost the same as B2C w/o customerId, but stricter is mismatch AI/PI status
  // - filterInstrumentDataForCustomer: throw if mismatch Ai/Pi
  // - checkInstrumentAccessForCustomer: use whitelisted goal types only
  // - validateInstrumentDueDiligenceDetails: use whitelisted only
}

// for authenticated tenant customer ->> to be called by SgTenantAwareInstrumentManager
def getInstrumentDetailsForTenantCustomer(...) {
  // should behave almost the same as B2C with customerId, but use tenant when checking instrument access
  // - filterInstrumentDataForCustomer: remove Ai/Pi sensitive data depending on customer
  // - checkInstrumentAccessForCustomer: user allowedInstrumentsBasedOnCorporateProfileForTenant
  // - validateInstrumentDueDiligenceDetails: block NoDueDiligence
}

// for authenticated tenant fa ->> to be called by SgTenantAwareInstrumentManager
def getInstrumentDetailsForTenantFa(...) {
  // should behave almost the same as B2B with customerId, but use AI/PI status always
  // - filterInstrumentDataForCustomer: no filter
  // - checkInstrumentAccessForCustomer: user allowedInstrumentsBasedOnCorporateProfileForTenant
  // - validateInstrumentDueDiligenceDetails: block NoDueDiligence
}

private def innerGetInstrumentDetails(...)
```

‌

**Source-preserving request, proposal, or question:**

> Let’s structure these as
> 
> ```
> // for existing B2C (customerId is optional) ->> to be called by SgFundSmartManagerV3
> def getInstrumentDetailsForCustomer(...) {
>   // keep existing logic here, i.e. switch on maybeCustomerId
>   // if customerId:
>   // - filterInstrumentDataForCustomer: remove Ai/Pi sensitive data depending on customer
>   // - checkInstrumentAccessForCustomer: user allowedInstrumentsBasedOnCorporateProfile
>   // - validateInstrumentDueDiligenceDetails: block NoDueDiligence
>   //
>   // if no customerId:
>   // - filterInstrumentDataForCustomer: remove Ai/Pi sensitive data always
>   // - checkInstrumentAccessForCustomer: use whitelisted goal types only
>   // - validateInstrumentDueDiligenceDetails: use whitelisted only
> }
> 
> // for no-auth endpoint ->> to be called by SgFundSmartManagerV3 (not SgTenantAwareInstrumentManager, since it's not specific to tenant')
> def getInstrumentDetails(...) {
>   // should behave almost the same as B2C w/o customerId, but stricter is mismatch AI/PI status
>   // - filterInstrumentDataForCustomer: throw if mismatch Ai/Pi
>   // - checkInstrumentAccessForCustomer: use whitelisted goal types only
>   // - validateInstrumentDueDiligenceDetails: use whitelisted only
> }
> 
> // for authenticated tenant customer ->> to be called by SgTenantAwareInstrumentManager
> def getInstrumentDetailsForTenantCustomer(...) {
>   // should behave almost the same as B2C with customerId, but use tenant when checking instrument access
>   // - filterInstrumentDataForCustomer: remove Ai/Pi sensitive data depending on customer
>   // - checkInstrumentAccessForCustomer: user allowedInstrumentsBasedOnCorporateProfileForTenant
>   // - validateInstrumentDueDiligenceDetails: block NoDueDiligence
> }
> 
> // for authenticated tenant fa ->> to be called by SgTenantAwareInstrumentManager
> def getInstrumentDetailsForTenantFa(...) {
>   // should behave almost the same as B2B with customerId, but use AI/PI status always
>   // - filterInstrumentDataForCustomer: no filter
>   // - checkInstrumentAccessForCustomer: user allowedInstrumentsBasedOnCorporateProfileForTenant
>   // - validateInstrumentDueDiligenceDetails: block NoDueDiligence
> }
> 
> private def innerGetInstrumentDetails(...)
> ```
> 
> ‌

**Conditions and limits:**

- Preserve four distinct instrument-detail flows: existing B2C optional customer; no-auth strict AI/PI mismatch; tenant customer corporate rules; tenant FA always AI/PI.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:400 · comment 562338150 · PR 10183 · 2024-11-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundDetailsManager.scala`

**Evidence:** anon-2.jsonl:400 · comment 562338150 · PR 10183 · 2024-11-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundDetailsManager.scala`

**Explicit source context (pr_title):**

> [INV-3558] feat(bff, advisory): Portfolio Builder Fund Details

## A2-0418 — CorporateProductRuleService: [person] pointed out to me that we already checked this below

**Source stance:** explanation

**Context:**

> PR 10182 ([INV-3430] feat(bff, advisory): Portfolio Builder Fund List), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/corporate/CorporateProductRuleService.scala; original row 418.

**Concern stated in the source:** The commenter later locates the final instrument allowedInvestorTypes filter, correcting the earlier concern.

**Source-preserving request, proposal, or question:**

> [person] pointed out to me that we already checked this below
> 
> ```
>     val allowedInstruments = resolvedInstruments
>       .filter(instrument => maybeCcy.forall(_ == instrument.ccy))
>       .filter(instrument => maybeInvestorType.forall(instrument.tradingConfigDetails.allowedInvestorTypes.contains))
> ```
> 
> ‌
> 
> so it’s all good :see_no_evil:

**Conditions and limits:**

- This is a reported code inspection resolving the row 416 concern, not a broad claim that all investor-type checks are always correct.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:418 · comment 558132779 · PR 10182 · 2024-10-28

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/corporate/CorporateProductRuleService.scala`

> pointed out to me that we already checked this below
> 
> ```
>     val allowedInstruments = resolvedInstruments
>       .filter(instrument => maybeCcy.forall(_ == instrument.ccy))
>       .filter(instrument => maybeInvestorType.forall(instrument.tradingConfigDetails.allowedInvestorTypes.contains))
> ```
> 
> ‌
> 
> so it’s all good :see_no_evil:

**Evidence:** anon-2.jsonl:418 · comment 558132779 · PR 10182 · 2024-10-28

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/corporate/CorporateProductRuleService.scala`

**Explicit source context (pr_title):**

> [INV-3430] feat(bff, advisory): Portfolio Builder Fund List

## A2-0438 — DocumentServiceE4s: We only need to create these `handle` methods if In is tuple

**Source stance:** suggestion

**Context:**

> PR 10262 (Feat/INV-3637 bff endpoint upload document), document-api/src/main/scala/com/endowus/silver/document/api/DocumentServiceE4s.scala; original row 438.

**Concern stated in the source:** Explicit handle methods are needed only when In is a tuple.

**Source-preserving request, proposal, or question:**

> We only need to create these `handle` methods if In is tuple

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:438 · comment 562878055 · PR 10262 · 2024-11-08

Source path: `document-api/src/main/scala/com/endowus/silver/document/api/DocumentServiceE4s.scala`

**Evidence:** anon-2.jsonl:438 · comment 562878055 · PR 10262 · 2024-11-08

Source path: `document-api/src/main/scala/com/endowus/silver/document/api/DocumentServiceE4s.scala`

**Explicit source context (pr_title):**

> Feat/INV-3637 bff endpoint upload document

## A2-0440 — InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs: This won’t work cuz we already filter out invalid data on the way out from domain model to DTO. I think we just need to use what...

**Source stance:** explanation

**Context:**

> PR 9436 ([INV-3011] feat(instrument): fix wrong investor type mapping with instrument (cpf and srs)), amend-scripts/src/main/scala/instrument/InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs.scala; original row 440.

**Concern stated in the source:** Invalid investor-type data is already filtered during domain-to-DTO mapping, so this repair cannot rediscover it from the DTO.

**Source-preserving request, proposal, or question:**

> This won’t work cuz we already filter out invalid data on the way out from domain model to DTO. I think we just need to use whatever existing data and update to same values

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:440 · comment 513369367 · PR 9436 · 2024-06-25

Source path: `amend-scripts/src/main/scala/instrument/InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs.scala`

**Evidence:** anon-2.jsonl:440 · comment 513369367 · PR 9436 · 2024-06-25

Source path: `amend-scripts/src/main/scala/instrument/InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(instrument): fix wrong investor type mapping with instrument (cpf and srs)

## A2-0514 — BaseBffRouteDefinitionsE4s: Should be `lines.headOption.map(_ => lines.flatten.mkString("\n"))`

**Source stance:** suggestion

**Context:**

> PR 10151 (Document Authenticated endpoints with permissions), bff-impl/src/main/scala/com/endowus/silver/bff/impl/routes/BaseBffRouteDefinitionsE4s.scala; original row 514.

**Concern stated in the source:** Should be `lines.headOption.map(_ => lines.flatten.mkString("\n"))`

**Source-preserving request, proposal, or question:**

> Should be `lines.headOption.map(_ => lines.flatten.mkString("\n"))`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:514 · comment 551557108 · PR 10151 · 2024-10-11

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/routes/BaseBffRouteDefinitionsE4s.scala`

**Evidence:** anon-2.jsonl:514 · comment 551557108 · PR 10151 · 2024-10-11

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/routes/BaseBffRouteDefinitionsE4s.scala`

**Explicit source context (pr_title):**

> Document Authenticated endpoints with permissions

## A2-0544 — HkChargeCommunicationProjection: This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala; original row 544.

**Concern stated in the source:** This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.

The communication logic in fact can be region agnostic as well \(the same way `InitiateFeeRedemptionCmdHandler` doesn’t care about sg or hk\). We can simply use the `redemptionDetails` \(instead of using amount from `discountDetails`, and having to assume that there is no tax involved\)

```
event.feeChargeRequest.redemptionDetails match {
  case Some(redemptionDetails) =>
    redemptionDetails.redeemedAmount match {
      case Some(chargeAmount) =>
        ...communication logic goes here...
      case None =>
        logger.error("... <unexpected-please-check> ... ")
        Future.successful(Done)
    }
  case None =>
    // waived without vouchers
    Future.successful(Done)
}
```

‌

**Source-preserving request, proposal, or question:**

> This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.
> 
> The communication logic in fact can be region agnostic as well \(the same way `InitiateFeeRedemptionCmdHandler` doesn’t care about sg or hk\). We can simply use the `redemptionDetails` \(instead of using amount from `discountDetails`, and having to assume that there is no tax involved\)
> 
> ```
> event.feeChargeRequest.redemptionDetails match {
>   case Some(redemptionDetails) =>
>     redemptionDetails.redeemedAmount match {
>       case Some(chargeAmount) =>
>         ...communication logic goes here...
>       case None =>
>         logger.error("... <unexpected-please-check> ... ")
>         Future.successful(Done)
>     }
>   case None =>
>     // waived without vouchers
>     Future.successful(Done)
> }
> ```
> 
> ‌

**Conditions and limits:**

- Communication follows FeeChargeCompletedEvt redemptionDetails: Some redeemedAmount sends; missing redeemedAmount logs unexpected and returns Done; None redemptionDetails is waived without vouchers and returns Done.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:544 · comment 550155826 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Evidence:** anon-2.jsonl:544 · comment 550155826 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0549 — MarketDataUploader: Blind me didn’t realize this method `retrievePrices` already exists. The `getPricesToUpdate` sorts again anyway

**Source stance:** explanation

**Context:**

> PR 10146 ([INV-3557] feat(marketdata): Limit price recon to 1year period if startDate not specified. Skip checking if transiently missing latest MStar price), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 549.

**Concern stated in the source:** Blind me didn’t realize this method `retrievePrices` already exists. The `getPricesToUpdate` sorts again anyway

**Source-preserving request, proposal, or question:**

> Blind me didn’t realize this method `retrievePrices` already exists. The `getPricesToUpdate` sorts again anyway

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:549 · comment 551473037 · PR 10146 · 2024-10-11

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:549 · comment 551473037 · PR 10146 · 2024-10-11

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-3557] feat(marketdata): Limit price recon to 1year period if startDate not specified. Skip checking if transiently missing latest MStar price

## A2-0593 — MstarDailyPerformance: This should be the only logic change. If ccy mismatched, we shouldn’t really fallback to headOption

**Source stance:** explanation

**Context:**

> PR 10085 ([INV-3509] feat(composition)(marketdata): Handle missing data from MStar. Retry if unexpected exception), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mstar/xmls/MstarDailyPerformance.scala; original row 593.

**Concern stated in the source:** This should be the only logic change. If ccy mismatched, we shouldn’t really fallback to headOption

**Source-preserving request, proposal, or question:**

> This should be the only logic change. If ccy mismatched, we shouldn’t really fallback to headOption

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:593 · comment 546466314 · PR 10085 · 2024-09-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mstar/xmls/MstarDailyPerformance.scala`

**Evidence:** anon-2.jsonl:593 · comment 546466314 · PR 10085 · 2024-09-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mstar/xmls/MstarDailyPerformance.scala`

**Explicit source context (pr_title):**

> [INV-3509] feat(composition)(marketdata): Handle missing data from MStar. Retry if unexpected exception

## A2-0602 — HkFundSmartManagerV3: So we block returning AI-only collections, but do not filter out AI data for instrument? What’s the expectation from Product?

**Source stance:** open-question

**Context:**

> PR 9835 (Resolve INV-3401: Expose endpoints for instrument/collection details for public webflow), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManagerV3.scala; original row 602.

**Concern stated in the source:** So we block returning AI-only collections, but do not filter out AI data for instrument? What’s the expectation from Product?

**Source-preserving request, proposal, or question:**

> So we block returning AI-only collections, but do not filter out AI data for instrument? What’s the expectation from Product?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:602 · comment 536685643 · PR 9835 · 2024-08-30

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManagerV3.scala`

**Evidence:** anon-2.jsonl:602 · comment 536685643 · PR 9835 · 2024-08-30

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManagerV3.scala`

**Explicit source context (pr_title):**

> Resolve INV-3401: Expose endpoints for instrument/collection details for public webflow

## A2-0640 — BaseAdvisoryServiceE4s: Actually, would it be easier if we just change `Endpoint` to `EndpointDef`, without touching the jsonRequest and jsonResponse? Anyway, we won’t be able t...

**Source stance:** open-question

**Context:**

> PR 9877 (phase 1 changes), advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala; original row 640.

**Concern stated in the source:** Actually, would it be easier if we just change `Endpoint` to `EndpointDef`, without touching the jsonRequest and jsonResponse? Anyway, we won’t be able to use `#In` when it’s a tuple right?

**Source-preserving request, proposal, or question:**

> Actually, would it be easier if we just change `Endpoint` to `EndpointDef`, without touching the jsonRequest and jsonResponse? Anyway, we won’t be able to use `#In` when it’s a tuple right?

**Conditions and limits:**

- EndpointDef rename without request/response refactor is an option; tuple input cannot use #In in the proposed way.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:640 · comment 537297719 · PR 9877 · 2024-09-02

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Evidence:** anon-2.jsonl:640 · comment 537297719 · PR 9877 · 2024-09-02

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> phase 1 changes

## A2-0673 — GoalModifyBehaviourHelpers: throw if using map \(`_ = ...`\), or `Future.failed` if using flatmap \(`_ <- ...`\)

**Source stance:** explanation

**Context:**

> PR 9715 ([INV-3238] feat(advisory): create apis for goal modify flow), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/GoalModifyBehaviourHelpers.scala; original row 673.

**Concern stated in the source:** throw if using map \(`_ = ...`\), or `Future.failed` if using flatmap \(`_ <- ...`\)

**Source-preserving request, proposal, or question:**

> throw if using map \(`_ = ...`\), or `Future.failed` if using flatmap \(`_ <- ...`\)

**Conditions and limits:**

- Map branch uses throw with `_ = ...`; flatMap branch uses Future.failed with `_ <- ...`.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:673 · comment 535558264 · PR 9715 · 2024-08-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/GoalModifyBehaviourHelpers.scala`

**Evidence:** anon-2.jsonl:673 · comment 535558264 · PR 9715 · 2024-08-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/GoalModifyBehaviourHelpers.scala`

**Explicit source context (pr_title):**

> [INV-3238] feat(advisory): create apis for goal modify flow

## A2-0675 — ServiceLogicImpl: Use collect

**Source stance:** suggestion

**Context:**

> PR 9825 (Feat/INV-3335 switch to jdbc monthly changes), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; original row 675.

**Source-preserving request, proposal, or question:**

> Use collect

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Use collect in monthly-data refactor; exact replacement expression is not supplied in this short comment.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:675 · comment 535259307 · PR 9825 · 2024-08-26

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:675 · comment 535259307 · PR 9825 · 2024-08-26

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +    } yield portfolioTaa
>    }
>  
> -  //TODO Move this to on-the-fly calculation later
> -  override def getPortfolioAnnualYield(portfolioId: UUID, effectiveDate: LocalDate, marketDataCcy: CurrencyUnit): Future[BigDecimal] = {
> -    refProvider
> -      .getPortfolioMarketDataEntity(

**Evidence:** anon-2.jsonl:675 · comment 535259307 · PR 9825 · 2024-08-26

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-3335 switch to jdbc monthly changes

## A2-0677 — ServiceLogicImpl: This method doesnt need to know about TAA, it should just load given set of instrumentIds \(and at most additionally marketdataCcy\)

**Source stance:** suggestion

**Context:**

> PR 9825 (Feat/INV-3335 switch to jdbc monthly changes), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; original row 677.

**Concern stated in the source:** This method doesnt need to know about TAA, it should just load given set of instrumentIds \(and at most additionally marketdataCcy\)

Also generally try to avoid Option.get as much as we can. Maybe sth like this

```
instrumentMStarDataRepository.findByInstrumentIds(instrumentIds)
  .map { _
    .map(x => x.instrumentId -> x.annualYield.map(AnnualYield.toDto))
    .collect {
      case (instrumentId, Some(annualYield)) => instrumentId -> annualYield
    }
    .toMap
  }
```

‌

**Source-preserving request, proposal, or question:**

> This method doesnt need to know about TAA, it should just load given set of instrumentIds \(and at most additionally marketdataCcy\)
> 
> Also generally try to avoid Option.get as much as we can. Maybe sth like this
> 
> ```
> instrumentMStarDataRepository.findByInstrumentIds(instrumentIds)
>   .map { _
>     .map(x => x.instrumentId -> x.annualYield.map(AnnualYield.toDto))
>     .collect {
>       case (instrumentId, Some(annualYield)) => instrumentId -> annualYield
>     }
>     .toMap
>   }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:677 · comment 535560228 · PR 9825 · 2024-08-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:677 · comment 535560228 · PR 9825 · 2024-08-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-3335 switch to jdbc monthly changes

## A2-0710 — PortfolioMonthlyChangesHelper: Use collect

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala; original row 710.

**Source-preserving request, proposal, or question:**

> Use collect

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:710 · comment 524609644 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Evidence:** anon-2.jsonl:710 · comment 524609644 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Explicit source context (hunk):**

> +    effectiveDate: LocalDate,
> +  ): Future[Map[String,BigDecimal]] = {
> +    portfolioService
> +      .getPortfolioById(
> +        portfolioId = portfolioId,
> +        effectiveDate = Some(effectiveDate.toString))
> +      .invoke()

**Evidence:** anon-2.jsonl:710 · comment 524609644 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0730 — InstrumentMonthlyChangesJdbcRepository: Move filter up, and select specific columns

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala; original row 730.

**Concern stated in the source:** Move filter up, and select specific columns

**Source-preserving request, proposal, or question:**

> Move filter up, and select specific columns

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:730 · comment 531324498 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Evidence:** anon-2.jsonl:730 · comment 531324498 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0732 — ServiceLogicImpl: Maybe drop all these filter out of BENCHMARK

**Source stance:** open-question

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; original row 732.

**Source-preserving request, proposal, or question:**

> Maybe drop all these filter out of BENCHMARK

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:732 · comment 531328022 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:732 · comment 531328022 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0746 — BaseAdvisoryServiceE4s: Oh it doesn’t work if you don’t make this inner tuple? Or you do it for clarity?

**Source stance:** open-question

**Context:**

> PR 9633 (Feat/INV-3339/fund smart goal modify sg additional fields), advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala; original row 746.

**Concern stated in the source:** Oh it doesn’t work if you don’t make this inner tuple? Or you do it for clarity?

**Source-preserving request, proposal, or question:**

> Oh it doesn’t work if you don’t make this inner tuple? Or you do it for clarity?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:746 · comment 531560761 · PR 9633 · 2024-08-16

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Evidence:** anon-2.jsonl:746 · comment 531560761 · PR 9633 · 2024-08-16

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> Feat/INV-3339/fund smart goal modify sg additional fields

## A2-0781 — SgRecommendedInvestmentManager: After the month filter, we don’t need to worry about it anymore

**Source stance:** suggestion

**Context:**

> PR 9739 (Feat/EN-3683 sg create a new api to get recommended investment amount), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala; original row 781.

**Concern stated in the source:** After the month filter, we don’t need to worry about it anymore

```
.groupBy(_.month)
.map {
  case (_, contributions) => contributions.map(_.amount).sum
}
.min
```

‌

**Source-preserving request, proposal, or question:**

> After the month filter, we don’t need to worry about it anymore
> 
> ```
> .groupBy(_.month)
> .map {
>   case (_, contributions) => contributions.map(_.amount).sum
> }
> .min
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:781 · comment 530394277 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Evidence:** anon-2.jsonl:781 · comment 530394277 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Explicit source context (pr_title):**

> Feat/EN-3683 sg create a new api to get recommended investment amount

## A2-0782 — SgRecommendedInvestmentManager: Let’s return Set in `getLastThreeMonths` so it’s a bit faster to filter here

**Source stance:** suggestion

**Context:**

> PR 9739 (Feat/EN-3683 sg create a new api to get recommended investment amount), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala; original row 782.

**Concern stated in the source:** Let’s return Set in `getLastThreeMonths` so it’s a bit faster to filter here

**Source-preserving request, proposal, or question:**

> Let’s return Set in `getLastThreeMonths` so it’s a bit faster to filter here

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:782 · comment 530394130 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Evidence:** anon-2.jsonl:782 · comment 530394130 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Explicit source context (pr_title):**

> Feat/EN-3683 sg create a new api to get recommended investment amount

## A2-0784 — SgRecommendedInvestmentManager: Can we change to this style instead

**Source stance:** suggestion

**Context:**

> PR 9739 (Feat/EN-3683 sg create a new api to get recommended investment amount), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala; original row 784.

**Concern stated in the source:** Can we change to this style instead

```
(myInfoFinancialData.updatedAt, myInfoFinancialData.cpfBalances.flatMap(_.oa), myInfoFinancialData.cpfContributions) match {
  case (Some(updatedAt), Some(cpfOaBalance), Some(cpfContributions)) =>
    ...
  case _ =>
    None
}
```

A bit dangerous to extract `cpfOaBalance` via extractor if we mess up refactoring, cuz all the fields there are `Option[Decimal]`

**Source-preserving request, proposal, or question:**

> Can we change to this style instead
> 
> ```
> (myInfoFinancialData.updatedAt, myInfoFinancialData.cpfBalances.flatMap(_.oa), myInfoFinancialData.cpfContributions) match {
>   case (Some(updatedAt), Some(cpfOaBalance), Some(cpfContributions)) =>
>     ...
>   case _ =>
>     None
> }
> ```
> 
> A bit dangerous to extract `cpfOaBalance` via extractor if we mess up refactoring, cuz all the fields there are `Option[Decimal]`

**Conditions and limits:**

- Tuple matching is proposed because many Option[Decimal] extractor fields make refactoring mixups easy.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:784 · comment 530398441 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Evidence:** anon-2.jsonl:784 · comment 530398441 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Explicit source context (pr_title):**

> Feat/EN-3683 sg create a new api to get recommended investment amount

## A2-0794 — ServiceLogicImpl: Just extract this filter and map as well? Also use collect instead

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; original row 794.

**Concern stated in the source:** Just extract this filter and map as well? Also use collect instead

**Source-preserving request, proposal, or question:**

> Just extract this filter and map as well? Also use collect instead

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:794 · comment 528900082 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:794 · comment 528900082 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0821 — ProductPortfolioRepository: Maybe we can keep this method generic, but only handle for CoreEnhanced for now…

**Source stance:** suggestion

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala; original row 821.

**Concern stated in the source:** Maybe we can keep this method generic, but only handle for CoreEnhanced for now…

```
def findProductPortfolio(
  advisoryTag: AdvisoryTag,
  riskTarget: ModelPortfolioRiskTarget,
  tradingAccountType: TradingAccountType
): Future[ProductPortfolio] = {
  findAllActiveForAdvisoryTag(advisoryTag)
    .filter(p => filterForTradingAccountType(advisoryTag, tradingAccountType, p))
    .filter(p => filterForRiskTarget(advisoryTag, riskTarget, p))
    .runWith(Sink.headOption)
    .flatMap({
      case Some(productPortfolio) => Future.successful(productPortfolio)
      case None =>
        Future
          .failed(BadRequest(s"Unable to find $advisoryTag portfolio for trading account $tradingAccountType with risk target of $riskTarget"))
    })
}

private def filterForRiskTarget(advisoryTag: AdvisoryTag, riskTarget: ModelPortfolioRiskTarget, p: ProductPortfolio): Boolean = {
  advisoryTag match {
    case AdvisoryTag.CORE_ENHANCED =>
      ProductPortfolio.extractCoreEnhancedMetaData(p).exists(_.riskTarget == riskTarget)
    case _ => false
  }
}
```

‌

I want to keep the method signature as close to the lookup by targetStockRatio one so it’s easier to switch later for Flagship/Esg/Factors/FlagshipDpm

**Source-preserving request, proposal, or question:**

> Maybe we can keep this method generic, but only handle for CoreEnhanced for now…
> 
> ```
> def findProductPortfolio(
>   advisoryTag: AdvisoryTag,
>   riskTarget: ModelPortfolioRiskTarget,
>   tradingAccountType: TradingAccountType
> ): Future[ProductPortfolio] = {
>   findAllActiveForAdvisoryTag(advisoryTag)
>     .filter(p => filterForTradingAccountType(advisoryTag, tradingAccountType, p))
>     .filter(p => filterForRiskTarget(advisoryTag, riskTarget, p))
>     .runWith(Sink.headOption)
>     .flatMap({
>       case Some(productPortfolio) => Future.successful(productPortfolio)
>       case None =>
>         Future
>           .failed(BadRequest(s"Unable to find $advisoryTag portfolio for trading account $tradingAccountType with risk target of $riskTarget"))
>     })
> }
> 
> private def filterForRiskTarget(advisoryTag: AdvisoryTag, riskTarget: ModelPortfolioRiskTarget, p: ProductPortfolio): Boolean = {
>   advisoryTag match {
>     case AdvisoryTag.CORE_ENHANCED =>
>       ProductPortfolio.extractCoreEnhancedMetaData(p).exists(_.riskTarget == riskTarget)
>     case _ => false
>   }
> }
> ```
> 
> ‌
> 
> I want to keep the method signature as close to the lookup by targetStockRatio one so it’s easier to switch later for Flagship/Esg/Factors/FlagshipDpm

**Conditions and limits:**

- Initial proposed generic signature handles only CoreEnhanced and otherwise returns false; row 837 proposes completing other productlines via ProductPortfolio.riskTarget.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:821 · comment 523845974 · PR 9605 · 2024-07-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Evidence:** anon-2.jsonl:821 · comment 523845974 · PR 9605 · 2024-07-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

## A2-0858 — InstrumentMarketDataEntity: If it’s None, `exists` will return false and we won’t fail

**Source stance:** explanation

**Context:**

> PR 9671 ([INV-3355] feat(marketdata): Allow empty price in DailyPerformance API. Populate instrument ccy if not exists), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala; original row 858.

**Concern stated in the source:** If it’s None, `exists` will return false and we won’t fail

**Source-preserving request, proposal, or question:**

> If it’s None, `exists` will return false and we won’t fail

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:858 · comment 525764413 · PR 9671 · 2024-07-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala`

**Evidence:** anon-2.jsonl:858 · comment 525764413 · PR 9671 · 2024-07-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala`

**Explicit source context (pr_title):**

> [INV-3355] feat(marketdata): Allow empty price in DailyPerformance API. Populate instrument ccy if not exists

## A2-0869 — PerformanceCalculator: Same same only, but I think structuring the logic this way makes it easier for me to visualize

**Source stance:** suggestion

**Context:**

> PR 9543 (Resolve INV-3136: Calculate max draw down for a given set of monthlyChanges.), performance-impl/src/main/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculator.scala; original row 869.

**Concern stated in the source:** Same same only, but I think structuring the logic this way makes it easier for me to visualize

```
var currentPeak, mddPeak, mddTrough = monthlyChanges.head
var maybeCurrentTrough: Option[MonthlyChange] = None
var maxDrawDown = BigDecimal(0)

def calculate(): Unit = {
  maybeCurrentTrough.foreach { currentTrough =>
    val drawDown = ((currentTrough.nav - currentPeak.nav) / currentPeak.nav).setScale(6, RoundingMode.HALF_EVEN)
    if (drawDown < maxDrawDown) {
      maxDrawDown = drawDown
      mddPeak = currentPeak
      mddTrough = currentTrough
    }
  }
  maybeCurrentTrough = None
}

for (current <- monthlyChanges) {
  if (current.nav > currentPeak.nav) {
    // Exiting current peak, attempt to calculate drawdown if already found current trough
    calculate()
    currentPeak = current
  } else if (maybeCurrentTrough.forall(_.nav > current.nav)) {
    // Not captured yet, or found new trough from current peak, just update
    maybeCurrentTrough = Some(current)
  }
}
// calculate for last peak
calculate()

Option.when(maxDrawDown < 0)(
  MaxDrawDown(drawDown = Math.abs(maxDrawDown.doubleValue()), peak = mddPeak, trough = mddTrough)
)
```

‌

**Source-preserving request, proposal, or question:**

> Same same only, but I think structuring the logic this way makes it easier for me to visualize
> 
> ```
> var currentPeak, mddPeak, mddTrough = monthlyChanges.head
> var maybeCurrentTrough: Option[MonthlyChange] = None
> var maxDrawDown = BigDecimal(0)
> 
> def calculate(): Unit = {
>   maybeCurrentTrough.foreach { currentTrough =>
>     val drawDown = ((currentTrough.nav - currentPeak.nav) / currentPeak.nav).setScale(6, RoundingMode.HALF_EVEN)
>     if (drawDown < maxDrawDown) {
>       maxDrawDown = drawDown
>       mddPeak = currentPeak
>       mddTrough = currentTrough
>     }
>   }
>   maybeCurrentTrough = None
> }
> 
> for (current <- monthlyChanges) {
>   if (current.nav > currentPeak.nav) {
>     // Exiting current peak, attempt to calculate drawdown if already found current trough
>     calculate()
>     currentPeak = current
>   } else if (maybeCurrentTrough.forall(_.nav > current.nav)) {
>     // Not captured yet, or found new trough from current peak, just update
>     maybeCurrentTrough = Some(current)
>   }
> }
> // calculate for last peak
> calculate()
> 
> Option.when(maxDrawDown < 0)(
>   MaxDrawDown(drawDown = Math.abs(maxDrawDown.doubleValue()), peak = mddPeak, trough = mddTrough)
> )
> ```
> 
> ‌

**Conditions and limits:**

- Proposed calculation keeps currentPeak/mddPeak/mddTrough, rounds negative drawdown to scale 6 HALF_EVEN, calculates when leaving a peak and once at the end, and returns None unless maxDrawDown<0.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:869 · comment 520477184 · PR 9543 · 2024-07-12

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculator.scala`

**Evidence:** anon-2.jsonl:869 · comment 520477184 · PR 9543 · 2024-07-12

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculator.scala`

**Explicit source context (pr_title):**

> Resolve INV-3136: Calculate max draw down for a given set of monthlyChanges.

## A2-0883 — StatementDataGenerator: Let’s filter for dpmGoals outside, regardless of `ignoreTimeForDebug`

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala; original row 883.

**Concern stated in the source:** Let’s filter for dpmGoals outside, regardless of `ignoreTimeForDebug`

**Source-preserving request, proposal, or question:**

> Let’s filter for dpmGoals outside, regardless of `ignoreTimeForDebug`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:883 · comment 507805408 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Evidence:** anon-2.jsonl:883 · comment 507805408 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0952 — BaseRedemptionCommunicationV2Projection: Can import `TraversableOnceUtils` and use it like this

**Source stance:** suggestion

**Context:**

> PR 9473 (Feat/INV-2450/sg hk retail redemption initiated email v2), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 952.

**Source-preserving request, proposal, or question:**

> Can import `TraversableOnceUtils` and use it like this
> 
> ```
> instruments
>   .flatMap(_.redemptionDetails.flatMap(_.dealingFrequency))
>   .maxByOption(identity)(DealingFrequencyOrdering)
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:952 · comment 516549655 · PR 9473 · 2024-07-02

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:952 · comment 516549655 · PR 9473 · 2024-07-02

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-2450/sg hk retail redemption initiated email v2

## A2-0956 — portfolio: I would think if a benchmark portfolio has missing performance, we should just filter it out, instead of sending with None portfolioStats. So let’s make this required

**Source stance:** suggestion

**Context:**

> PR 9487 ([INV-3233] feat(advisory): Support portfolio-offerings for Core-Enhanced), advisory-api/src/main/scala/com/endowus/silver/advisory/api/models/portfolio.scala; original row 956.

**Concern stated in the source:** I would think if a benchmark portfolio has missing performance, we should just filter it out, instead of sending with None portfolioStats. So let’s make this required

**Source-preserving request, proposal, or question:**

> I would think if a benchmark portfolio has missing performance, we should just filter it out, instead of sending with None portfolioStats. So let’s make this required

**Conditions and limits:**

- Benchmarks missing performance should be filtered out, allowing required portfolioStats.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:956 · comment 518021612 · PR 9487 · 2024-07-05

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/models/portfolio.scala`

**Evidence:** anon-2.jsonl:956 · comment 518021612 · PR 9487 · 2024-07-05

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/models/portfolio.scala`

**Explicit source context (pr_title):**

> [INV-3233] feat(advisory): Support portfolio-offerings for Core-Enhanced

## A2-0957 — package: Either that or we keep it Set\[UUID\] here, and sort \(say by stockRatio and then by name\) in offerings response

**Source stance:** suggestion

**Context:**

> PR 9487 ([INV-3233] feat(advisory): Support portfolio-offerings for Core-Enhanced), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/models/advisoryinfo/package.scala; original row 957.

**Concern stated in the source:** Either that or we keep it Set\[UUID\] here, and sort \(say by stockRatio and then by name\) in offerings response

**Source-preserving request, proposal, or question:**

> Either that or we keep it Set\[UUID\] here, and sort \(say by stockRatio and then by name\) in offerings response

**Conditions and limits:**

- Alternative to source-controlled list ordering is Set[UUID] sorted by stockRatio then name at response time.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:957 · comment 518022338 · PR 9487 · 2024-07-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/models/advisoryinfo/package.scala`

**Evidence:** anon-2.jsonl:957 · comment 518022338 · PR 9487 · 2024-07-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/models/advisoryinfo/package.scala`

**Explicit source context (pr_title):**

> [INV-3233] feat(advisory): Support portfolio-offerings for Core-Enhanced

## A2-1030 — CorporateProfile: Let’s just filter for exclusive, then check

**Source stance:** requested-change

**Context:**

> PR 9403 ([INV-3211] feat(advisory): Add new specific instrument access rule for ringfencing), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/corporate/ces/CorporateProfile.scala; original row 1030.

**Source-preserving request, proposal, or question:**

> Let’s just filter for exclusive, then check

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1030 · comment 513337693 · PR 9403 · 2024-06-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/corporate/ces/CorporateProfile.scala`

**Evidence:** anon-2.jsonl:1030 · comment 513337693 · PR 9403 · 2024-06-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/corporate/ces/CorporateProfile.scala`

**Explicit source context (pr_title):**

> [INV-3211] feat(advisory): Add new specific instrument access rule for ringfencing

## A2-1040 — MonthlyChangeGenerator: [person] maybe just a bit cleaner to change this condition

**Source stance:** suggestion

**Context:**

> PR 9362 (Resolve INV-3153: Fix monthly change generator for empty instrument monthly changes.), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala; original row 1040.

**Concern stated in the source:** [person] maybe just a bit cleaner to change this condition

```
if (targetInstrumentWeights.isEmpty) {
  throw new Exception(s"targetInstrumentWeights is empty!")
}
    
val instrumentsWithMissingMonthlyChanges = targetInstrumentWeights.keys.filterNot(instrumentMonthlyChanges.get(_).exists(_.nonEmpty))
... log warn for these instruments and return
```

‌

**Source-preserving request, proposal, or question:**

> [person] maybe just a bit cleaner to change this condition
> 
> ```
> if (targetInstrumentWeights.isEmpty) {
>   throw new Exception(s"targetInstrumentWeights is empty!")
> }
>     
> val instrumentsWithMissingMonthlyChanges = targetInstrumentWeights.keys.filterNot(instrumentMonthlyChanges.get(_).exists(_.nonEmpty))
> ... log warn for these instruments and return
> ```
> 
> ‌

**Conditions and limits:**

- Empty targetInstrumentWeights throws; any missing/nonempty instrument MC detection should warn and stop calculation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1040 · comment 510728117 · PR 9362 · 2024-06-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala`

> maybe just a bit cleaner to change this condition
> 
> ```
> if (targetInstrumentWeights.isEmpty) {
>   throw new Exception(s"targetInstrumentWeights is empty!")
> }
>     
> val instrumentsWithMissingMonthlyChanges = targetInstrumentWeights.keys.filterNot(instrumentMonthlyChanges.get(_).exists(_.nonEmpty))
> ... log warn for these instruments and return
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:1040 · comment 510728117 · PR 9362 · 2024-06-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala`

**Explicit source context (pr_title):**

> Resolve INV-3153: Fix monthly change generator for empty instrument monthly changes.

## A2-1041 — MonthlyChangeGenerator: Yea we can just find instruments with empty monthly changes, if exists then log them and return empty for whole TAA. If one is empty, we wont be able to ...

**Source stance:** suggestion

**Context:**

> PR 9335 (Resolve INV-3153: Changes to support overriding monthly changes to empty.), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala; original row 1041.

**Concern stated in the source:** Yea we can just find instruments with empty monthly changes, if exists then log them and return empty for whole TAA. If one is empty, we wont be able to calculate for TAA anyway

**Source-preserving request, proposal, or question:**

> Yea we can just find instruments with empty monthly changes, if exists then log them and return empty for whole TAA. If one is empty, we wont be able to calculate for TAA anyway

**Conditions and limits:**

- One empty instrument monthly-change series makes whole TAA calculation impossible, so return empty TAA MC and log affected instruments.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1041 · comment 510035175 · PR 9335 · 2024-06-12

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala`

**Evidence:** anon-2.jsonl:1041 · comment 510035175 · PR 9335 · 2024-06-12

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala`

**Explicit source context (pr_title):**

> Resolve INV-3153: Changes to support overriding monthly changes to empty.

## A2-1059 — PageDataGenerator: Actually we have too many region pattern matching in this method. Maybe consolidate it a bit

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala; original row 1059.

**Concern stated in the source:** Actually we have too many region pattern matching in this method. Maybe consolidate it a bit

```
def headTailMapper(...)

def generate(goals: List[GoalRowDetails], isDPM: Boolean, maxRowsInFirstPage: Int, firstPageTemplate: String, subsequentPageTemplate: String): List[(AllInvestmentGoalsPageData, String)] = ...

region match {
  case SilverRegion.Sg =>
    // SG AllInvestmentGoals templates do not distinguish DPM and non-DPM goals, hence treating all goals as non-DPM
    generate(
      goals = pageData.goalDetails.asScala.toList,
      isDPM = false,
      maxRowsInFirstPage = maxRowsPerAllInvestmentsPage,
      firstPageTemplate = "allInvestmentGoalsPage",
      subsequentPageTemplate = "allInvestmentGoalsPureGoalsPage"
    )
  case SilverRegion.Hk =>
    // HK AllInvestmentGoals templates have special empty page
    if (pageData.goalDetails.isEmpty) {
      List((pageData.copy(goalDetails = pageData.goalDetails), "allInvestmentGoalsPageWithoutGoal"))
    } else {
      val allInvestmentDPMPageData = generate(
        goals = pageData.goalDetails.asScala.toList.filter(_.isDiscretionary),
        isDPM = true,
        maxRowsInFirstPage = maxRowsPerAllInvestmentsPageForFirstDPMPage,
        firstPageTemplate = "allInvestmentGoalsPage",
        subsequentPageTemplate = "allInvestmentGoalsPureGoalsPage"
      )
      val allInvestmentNonDPMPageData = generate(
        goals = pageData.goalDetails.asScala.toList.filterNot(_.isDiscretionary),
        isDPM = false,
        maxRowsInFirstPage = maxRowsPerAllInvestmentsPage,
        firstPageTemplate = "allInvestmentNonDPMGoalsPage",
        subsequentPageTemplate = "allInvestmentGoalsPureGoalsPage"
      )
      allInvestmentDPMPageData ++ allInvestmentNonDPMPageData
    }
  case _ => throw new Exception(s"AllInvestmentGoalsPageData generator behaviour not configured for region $region.")
}
```

‌

**Source-preserving request, proposal, or question:**

> Actually we have too many region pattern matching in this method. Maybe consolidate it a bit
> 
> ```
> def headTailMapper(...)
> 
> def generate(goals: List[GoalRowDetails], isDPM: Boolean, maxRowsInFirstPage: Int, firstPageTemplate: String, subsequentPageTemplate: String): List[(AllInvestmentGoalsPageData, String)] = ...
> 
> region match {
>   case SilverRegion.Sg =>
>     // SG AllInvestmentGoals templates do not distinguish DPM and non-DPM goals, hence treating all goals as non-DPM
>     generate(
>       goals = pageData.goalDetails.asScala.toList,
>       isDPM = false,
>       maxRowsInFirstPage = maxRowsPerAllInvestmentsPage,
>       firstPageTemplate = "allInvestmentGoalsPage",
>       subsequentPageTemplate = "allInvestmentGoalsPureGoalsPage"
>     )
>   case SilverRegion.Hk =>
>     // HK AllInvestmentGoals templates have special empty page
>     if (pageData.goalDetails.isEmpty) {
>       List((pageData.copy(goalDetails = pageData.goalDetails), "allInvestmentGoalsPageWithoutGoal"))
>     } else {
>       val allInvestmentDPMPageData = generate(
>         goals = pageData.goalDetails.asScala.toList.filter(_.isDiscretionary),
>         isDPM = true,
>         maxRowsInFirstPage = maxRowsPerAllInvestmentsPageForFirstDPMPage,
>         firstPageTemplate = "allInvestmentGoalsPage",
>         subsequentPageTemplate = "allInvestmentGoalsPureGoalsPage"
>       )
>       val allInvestmentNonDPMPageData = generate(
>         goals = pageData.goalDetails.asScala.toList.filterNot(_.isDiscretionary),
>         isDPM = false,
>         maxRowsInFirstPage = maxRowsPerAllInvestmentsPage,
>         firstPageTemplate = "allInvestmentNonDPMGoalsPage",
>         subsequentPageTemplate = "allInvestmentGoalsPureGoalsPage"
>       )
>       allInvestmentDPMPageData ++ allInvestmentNonDPMPageData
>     }
>   case _ => throw new Exception(s"AllInvestmentGoalsPageData generator behaviour not configured for region $region.")
> }
> ```
> 
> ‌

**Conditions and limits:**

- Preserve SG all-non-DPM template handling versus HK DPM/non-DPM splitting and special empty page; the entire example is a proposal.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1059 · comment 502467840 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala`

**Evidence:** anon-2.jsonl:1059 · comment 502467840 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1116 — RecurringInvestmentProcessor: You can import OptionUtils and use onNone and make this a bit nicer… also better to extract schedule here, so that we don’t have to blindly call ge...

**Source stance:** suggestion

**Context:**

> PR 9091 ([EN-3271] Add autofx recurring support in investment), investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; original row 1116.

**Concern stated in the source:** You can import OptionUtils and use onNone and make this a bit nicer… also better to extract schedule here, so that we don’t have to blindly call get later

```
.map { investmentPlan =>
  investmentPlan.recurringInvestmentSchedule
    .onNone(logger.error("blah"))
    .map((investmentPlan, _))
    .toList
}
.flatMapConcat(Source(_))
```

‌

**Source-preserving request, proposal, or question:**

> You can import OptionUtils and use onNone and make this a bit nicer… also better to extract schedule here, so that we don’t have to blindly call get later
> 
> ```
> .map { investmentPlan =>
>   investmentPlan.recurringInvestmentSchedule
>     .onNone(logger.error("blah"))
>     .map((investmentPlan, _))
>     .toList
> }
> .flatMapConcat(Source(_))
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1116 · comment 505575550 · PR 9091 · 2024-05-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Evidence:** anon-2.jsonl:1116 · comment 505575550 · PR 9091 · 2024-05-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (pr_title):**

> [EN-3271] Add autofx recurring support in investment

## A2-1182 — FlagshipDpmSchemaV1: Can use `exists`

**Source stance:** suggestion

**Context:**

> PR 9146 (feat(advisory): terms agreement ack for add goal flagship dpm simulation summary and confirmation endpoints), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/termsagreement/hk/FlagshipDpmSchemaV1.scala; original row 1182.

**Source-preserving request, proposal, or question:**

> Can use `exists`

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1182 · comment 501686916 · PR 9146 · 2024-05-17

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/termsagreement/hk/FlagshipDpmSchemaV1.scala`

**Evidence:** anon-2.jsonl:1182 · comment 501686916 · PR 9146 · 2024-05-17

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/termsagreement/hk/FlagshipDpmSchemaV1.scala`

**Explicit source context (hunk):**

> +  def getTermsAgreementAck(request: FlagshipDpmGoalCreateRequest): TermsAgreementAck = {
> +    val isAutoFx = isAutoFxFundingInstructionsRequest(request.resolvedInitialFundingInstructionsRequest) ||
> +      request.resolvedRecurringInvestmentRequest.exists(r => isAutoFxFundingInstructionsRequest(r.resolvedFundingInstructions))
> +    val orderedTerms = getTermsAgreementItems(isGoalModify = false, isAutoFx = isAutoFx)
> +    TermsAgreementAck(
> +      items = orderedTerms,
> +      footer = Some(FlagshipDpmTermsSchemaV1.footer)

**Evidence:** anon-2.jsonl:1182 · comment 501686916 · PR 9146 · 2024-05-17

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/termsagreement/hk/FlagshipDpmSchemaV1.scala`

**Explicit source context (pr_title):**

> feat(advisory): terms agreement ack for add goal flagship dpm simulation summary and confirmation endpoints

## A2-1197 — InstrumentExportScheduler: You can just batch it here

**Source stance:** suggestion

**Context:**

> PR 9073 (TT-4242 Automate export of Broker transactions for alts), broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala; original row 1197.

**Concern stated in the source:** You can just batch it here

```
Source(instruments)
  .grouped(10)
  .map(_.toSet)
  .mapAsync(2) { instrumentIds =>
    instrumentSvc.getInstrumentV2ByIds(instrumentIds.mkString(",")).invoke().map(_.toList)
  }
  .flatMapConcat(Source(_))
  .runWith(Sink.seq)
```

‌

**Source-preserving request, proposal, or question:**

> You can just batch it here
> 
> ```
> Source(instruments)
>   .grouped(10)
>   .map(_.toSet)
>   .mapAsync(2) { instrumentIds =>
>     instrumentSvc.getInstrumentV2ByIds(instrumentIds.mkString(",")).invoke().map(_.toList)
>   }
>   .flatMapConcat(Source(_))
>   .runWith(Sink.seq)
> ```
> 
> ‌

**Conditions and limits:**

- Exact batching proposal: grouped(10), toSet, mapAsync(2), getInstrumentV2ByIds comma list, flatMapConcat, Sink.seq.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1197 · comment 500780169 · PR 9073 · 2024-05-14

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala`

**Evidence:** anon-2.jsonl:1197 · comment 500780169 · PR 9073 · 2024-05-14

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala`

**Explicit source context (pr_title):**

> TT-4242 Automate export of Broker transactions for alts

## A2-1272 — AdvisedPortfolioHelper: Maybe `exists` instead? We dont need to log if not provided?

**Source stance:** open-question

**Context:**

> PR 8933 (Feat/INV-2808/flagship dpm goal create endpoints), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/advised/AdvisedPortfolioHelper.scala; original row 1272.

**Source-preserving request, proposal, or question:**

> Maybe `exists` instead? We dont need to log if not provided?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1272 · comment 496574113 · PR 8933 · 2024-04-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/advised/AdvisedPortfolioHelper.scala`

**Evidence:** anon-2.jsonl:1272 · comment 496574113 · PR 8933 · 2024-04-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/advised/AdvisedPortfolioHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-2808/flagship dpm goal create endpoints

## A2-1297 — ValidationHelpers: Maybe just make this `maybeAmount`

**Source stance:** open-question

**Context:**

> PR 8933 (Feat/INV-2808/flagship dpm goal create endpoints), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala; original row 1297.

**Source-preserving request, proposal, or question:**

> Maybe just make this `maybeAmount`
> 
> ```
> if (maybeAmount.exists(BigDecimalUtils.hasTooManyDigits))
> ```
> 
> ‌

**Conditions and limits:**

- Proposed maybeAmount.exists(BigDecimalUtils.hasTooManyDigits) keeps absent amount valid for this digits check.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1297 · comment 498544377 · PR 8933 · 2024-05-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Evidence:** anon-2.jsonl:1297 · comment 498544377 · PR 8933 · 2024-05-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Explicit source context (pr_title):**

> Feat/INV-2808/flagship dpm goal create endpoints

## A2-1360 — MarketDataUploader: I suppose it’s also good to log for prices we have in our DB but not in MStar.

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1360.

**Concern stated in the source:** I suppose it’s also good to log for prices we have in our DB but not in MStar.

Speaking of this, the instrument source should probably filter for those we know prices are available in MStar. I think for now, we can start with `instrument.pricingDetails.pricingSource`

**Source-preserving request, proposal, or question:**

> I suppose it’s also good to log for prices we have in our DB but not in MStar.
> 
> Speaking of this, the instrument source should probably filter for those we know prices are available in MStar. I think for now, we can start with `instrument.pricingDetails.pricingSource`

**Conditions and limits:**

- Reconcile prices in DB but absent MStar too; source selection should require known MStar pricingSource.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1360 · comment 493343432 · PR 8931 · 2024-04-17

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1360 · comment 493343432 · PR 8931 · 2024-04-17

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1366 — MarketDataUploader: Nit: no need to start a Source from beginning I think

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1366.

**Concern stated in the source:** Nit: no need to start a Source from beginning I think

```
for {
  instruments <- instrumentIds match {
    ...
  }
  _ <- Source(instruments)
    .filter(... check pricing source)
    .mapAsync(...)
    .run() // consider using SourceUtils.RunWithReportingExt (it has some basic logging for progress/completion)
} yield Done
```

‌

**Source-preserving request, proposal, or question:**

> Nit: no need to start a Source from beginning I think
> 
> ```
> for {
>   instruments <- instrumentIds match {
>     ...
>   }
>   _ <- Source(instruments)
>     .filter(... check pricing source)
>     .mapAsync(...)
>     .run() // consider using SourceUtils.RunWithReportingExt (it has some basic logging for progress/completion)
> } yield Done
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1366 · comment 494946679 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1366 · comment 494946679 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1375 — MarketDataUploader: I think this cassandra table already have priceDate in its clustering key. We should be able to add a method in repository to filter in database itself

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1375.

**Concern stated in the source:** I think this cassandra table already have priceDate in its clustering key. We should be able to add a method in repository to filter in database itself

**Source-preserving request, proposal, or question:**

> I think this cassandra table already have priceDate in its clustering key. We should be able to add a method in repository to filter in database itself

**Conditions and limits:**

- priceDate clustering key allows database-side filtering; source says this is believed to exist, not independently verified.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1375 · comment 495203334 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1375 · comment 495203334 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1378 — MarketDataUploader: We can return `InstrumentPriceReconResult` from here right? In general, avoid using tuple to avoid confusion/mistake unless it’s very isolated and simple

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1378.

**Concern stated in the source:** We can return `InstrumentPriceReconResult` from here right? In general, avoid using tuple to avoid confusion/mistake unless it’s very isolated and simple

**Source-preserving request, proposal, or question:**

> We can return `InstrumentPriceReconResult` from here right? In general, avoid using tuple to avoid confusion/mistake unless it’s very isolated and simple

**Conditions and limits:**

- Use a result case class instead of confusing tuple unless usage is isolated/simple.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1378 · comment 495250607 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1378 · comment 495250607 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1421 — PortfolioSuitabilityAnalysisLogic: Yeah I think we can pass the isDpm flag there and we can reduce a lot of tuple returning here…

**Source stance:** suggestion

**Context:**

> PR 8834 (Feat/INV-2861 dpm portfolio suitability), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala; original row 1421.

**Source-preserving request, proposal, or question:**

> Yeah I think we can pass the isDpm flag there and we can reduce a lot of tuple returning here…

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1421 · comment 488901989 · PR 8834 · 2024-04-04

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala`

**Evidence:** anon-2.jsonl:1421 · comment 488901989 · PR 8834 · 2024-04-04

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-2861 dpm portfolio suitability

## A2-1439 — BaseServiceLogicImpl: Yes all the usage of this API mostly just check if plan exists.. and in general, if you query by not entity-id, you should expect EC regardless

**Source stance:** explanation

**Context:**

> PR 8906 ([INV-2906] feat(goal): Use Plan readside table for getPlansByCustomerId), goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; original row 1439.

**Concern stated in the source:** Yes all the usage of this API mostly just check if plan exists.. and in general, if you query by not entity-id, you should expect EC regardless

**Source-preserving request, proposal, or question:**

> Yes all the usage of this API mostly just check if plan exists.. and in general, if you query by not entity-id, you should expect EC regardless

**Conditions and limits:**

- Non-entity-id plan lookup should be expected eventually consistent; consumers mostly check existence.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1439 · comment 491283491 · PR 8906 · 2024-04-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1439 · comment 491283491 · PR 8906 · 2024-04-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-2906] feat(goal): Use Plan readside table for getPlansByCustomerId

## A2-1455 — BaseServiceLogicImpl: Nits: maybe filter out inactive before we append plans

**Source stance:** suggestion

**Context:**

> PR 8677 ([EN-3097] Remove cassandra readside dependency in goal svc), goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; original row 1455.

**Source-preserving request, proposal, or question:**

> Nits: maybe filter out inactive before we append plans

**Conditions and limits:**

- Filter inactive goals before expensive append-plan lookup.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1455 · comment 483727495 · PR 8677 · 2024-03-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1455 · comment 483727495 · PR 8677 · 2024-03-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [EN-3097] Remove cassandra readside dependency in goal svc

## A2-1493 — FlowUtils: ```

**Source stance:** suggestion

**Context:**

> PR 8764 (Feat/INV-2777 invest systems subscriber tracing), silver-commons/src/main/scala/com/endowus/silver/commons/utils/FlowUtils.scala; original row 1493.

**Concern stated in the source:** ```
.map(message => {
  val incomingContext = message
    .get(KafkaMetadataKeys.Headers)
    .flatMap(s =>
      Try(KafkaInstrumentation.settings.propagator.read(s, Context.Empty)).toOption
    )
    .getOrElse(Context.Empty)
  (incomingContext, message.payload)
})
```

this block is per msg, and it’s identical in all 3 methods… just extract a common method… no need voodoo

**Source-preserving request, proposal, or question:**

> ```
> .map(message => {
>   val incomingContext = message
>     .get(KafkaMetadataKeys.Headers)
>     .flatMap(s =>
>       Try(KafkaInstrumentation.settings.propagator.read(s, Context.Empty)).toOption
>     )
>     .getOrElse(Context.Empty)
>   (incomingContext, message.payload)
> })
> ```
> 
> this block is per msg, and it’s identical in all 3 methods… just extract a common method… no need voodoo

**Conditions and limits:**

- Extract identical per-message KafkaMetadataKeys.Headers/KafkaInstrumentation.propagator.read(...,Context.Empty) mapping, retaining Try-toOption fallback to Context.Empty.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1493 · comment 484249261 · PR 8764 · 2024-03-22

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/FlowUtils.scala`

**Evidence:** anon-2.jsonl:1493 · comment 484249261 · PR 8764 · 2024-03-22

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/FlowUtils.scala`

**Explicit source context (pr_title):**

> Feat/INV-2777 invest systems subscriber tracing

## A2-1517 — HkFundSmartManager: Maybe reuse `InstrumentInfoDto.canBePartOfMultiFundPortfolio` for this instrument count check.. And we simply use `instruments.exists(_.isIlliquidAlts)` for ...

**Source stance:** suggestion

**Context:**

> PR 8619 (Resolve INV-2765: Endpoint to derive advisory questionnaire for a given set of instruments.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManager.scala; original row 1517.

**Concern stated in the source:** Maybe reuse `InstrumentInfoDto.canBePartOfMultiFundPortfolio` for this instrument count check.. And we simply use `instruments.exists(_.isIlliquidAlts)` for isAlts check

**Source-preserving request, proposal, or question:**

> Maybe reuse `InstrumentInfoDto.canBePartOfMultiFundPortfolio` for this instrument count check.. And we simply use `instruments.exists(_.isIlliquidAlts)` for isAlts check

**Conditions and limits:**

- Reuse canBePartOfMultiFundPortfolio; determine isAlts via instruments.exists(_.isIlliquidAlts).
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1517 · comment 480916378 · PR 8619 · 2024-03-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManager.scala`

**Evidence:** anon-2.jsonl:1517 · comment 480916378 · PR 8619 · 2024-03-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManager.scala`

**Explicit source context (pr_title):**

> Resolve INV-2765: Endpoint to derive advisory questionnaire for a given set of instruments.

## A2-1531 — FundSmartHelper: This reads a bit weird, cuz it’s all logic within this trait. It’s the one deciding which fee to fetch per `request.isSingleFund`, then it validates against its...

**Source stance:** suggestion

**Context:**

> PR 8488 (Resolve INV-2640: Changes to include estimation for multi-fund goal access fee for single fund goal creation.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala; original row 1531.

**Concern stated in the source:** This reads a bit weird, cuz it’s all logic within this trait. It’s the one deciding which fee to fetch per `request.isSingleFund`, then it validates against its own logic.

Maybe just decide this inside `getFeeEstimation` returning tuple of `(endowusAccessFee, maybeMultiFundAccessFee)`

**Source-preserving request, proposal, or question:**

> This reads a bit weird, cuz it’s all logic within this trait. It’s the one deciding which fee to fetch per `request.isSingleFund`, then it validates against its own logic.
> 
> Maybe just decide this inside `getFeeEstimation` returning tuple of `(endowusAccessFee, maybeMultiFundAccessFee)`

**Conditions and limits:**

- Trait decides fee fetch from request.isSingleFund then validates itself; proposed getFeeEstimation returns endowusAccessFee and optional multiFundAccessFee.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1531 · comment 482635336 · PR 8488 · 2024-03-18

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala`

**Evidence:** anon-2.jsonl:1531 · comment 482635336 · PR 8488 · 2024-03-18

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala`

**Explicit source context (pr_title):**

> Resolve INV-2640: Changes to include estimation for multi-fund goal access fee for single fund goal creation.

## A2-1547 — HkFundSmartInstrumentBuilder: We’re adding funding source tag for HK too? Today we only have HKD Cash or USD Cash, which the ccy filter should be sufficient?

**Source stance:** open-question

**Context:**

> PR 8429 (Resolve INV-2639: New endpoints for HK fund smart Instruments.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartInstrumentBuilder.scala; original row 1547.

**Concern stated in the source:** We’re adding funding source tag for HK too? Today we only have HKD Cash or USD Cash, which the ccy filter should be sufficient?

**Source-preserving request, proposal, or question:**

> We’re adding funding source tag for HK too? Today we only have HKD Cash or USD Cash, which the ccy filter should be sufficient?

**Conditions and limits:**

- HK funding-source tag is questioned because only HKD/USD cash exist and currency filter may suffice.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1547 · comment 480886207 · PR 8429 · 2024-03-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartInstrumentBuilder.scala`

**Evidence:** anon-2.jsonl:1547 · comment 480886207 · PR 8429 · 2024-03-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> Resolve INV-2639: New endpoints for HK fund smart Instruments.

## A2-1644 — UpdateTemplateDisplayName: Filter for empty displayName instead?

**Source stance:** open-question

**Context:**

> PR 8302 ([EN-2909] feat(advisory): Update recommended model portfolio names), amend-scripts/src/main/scala/advisory/UpdateTemplateDisplayName.scala; original row 1644.

**Source-preserving request, proposal, or question:**

> Filter for empty displayName instead?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1644 · comment 473665828 · PR 8302 · 2024-02-20

Source path: `amend-scripts/src/main/scala/advisory/UpdateTemplateDisplayName.scala`

**Evidence:** anon-2.jsonl:1644 · comment 473665828 · PR 8302 · 2024-02-20

Source path: `amend-scripts/src/main/scala/advisory/UpdateTemplateDisplayName.scala`

**Explicit source context (pr_title):**

> [EN-2909] feat(advisory): Update recommended model portfolio names

## A2-1654 — HkAdvisoryLevelClassificationLogic: exists instead? Today we don’t allow mixing illiquid alts with other funds, but I suppose just one would make it execution-only mode?

**Source stance:** open-question

**Context:**

> PR 8193 (Feat/INV-2101 execution advisory transaction tagging), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/advisorylevel/HkAdvisoryLevelClassificationLogic.scala; original row 1654.

**Concern stated in the source:** exists instead? Today we don’t allow mixing illiquid alts with other funds, but I suppose just one would make it execution-only mode?

**Source-preserving request, proposal, or question:**

> exists instead? Today we don’t allow mixing illiquid alts with other funds, but I suppose just one would make it execution-only mode?

**Conditions and limits:**

- Any illiquid-alts instrument may imply execution-only; source questions exists versus forall.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1654 · comment 465907386 · PR 8193 · 2024-01-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/advisorylevel/HkAdvisoryLevelClassificationLogic.scala`

**Evidence:** anon-2.jsonl:1654 · comment 465907386 · PR 8193 · 2024-01-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/advisorylevel/HkAdvisoryLevelClassificationLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-2101 execution advisory transaction tagging

## A2-1659 — HkAdvisoryLevelClassificationLogic: So exists is correct behaviour, not forall right?

**Source stance:** explanation

**Context:**

> PR 8193 (Feat/INV-2101 execution advisory transaction tagging), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/advisorylevel/HkAdvisoryLevelClassificationLogic.scala; original row 1659.

**Source-preserving request, proposal, or question:**

> So exists is correct behaviour, not forall right?

**Conditions and limits:**

- The follow-up explicitly selects exists over forall; no new implementation is claimed.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1659 · comment 465913665 · PR 8193 · 2024-01-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/advisorylevel/HkAdvisoryLevelClassificationLogic.scala`

**Evidence:** anon-2.jsonl:1659 · comment 465913665 · PR 8193 · 2024-01-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/advisorylevel/HkAdvisoryLevelClassificationLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-2101 execution advisory transaction tagging

## A2-1661 — HkAdvisoryLevelClassificationLogic: Check advisory logic we built for Alts for reference. I think we have been using exists so far \(and sometimes, additionally check single ins...

**Source stance:** explanation

**Context:**

> PR 8193 (Feat/INV-2101 execution advisory transaction tagging), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/advisorylevel/HkAdvisoryLevelClassificationLogic.scala; original row 1661.

**Concern stated in the source:** Check advisory logic we built for Alts for reference. I think we have been using exists so far \(and sometimes, additionally check single instrument\)

**Source-preserving request, proposal, or question:**

> Check advisory logic we built for Alts for reference. I think we have been using exists so far \(and sometimes, additionally check single instrument\)

**Conditions and limits:**

- Existing alts advisory checks use exists, sometimes combined with single instrument, as a reuse reference.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1661 · comment 465918037 · PR 8193 · 2024-01-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/advisorylevel/HkAdvisoryLevelClassificationLogic.scala`

**Evidence:** anon-2.jsonl:1661 · comment 465918037 · PR 8193 · 2024-01-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/advisorylevel/HkAdvisoryLevelClassificationLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-2101 execution advisory transaction tagging

## A2-1701 — BaseRedemptionCommunicationV2Projection: Ah we already filter for this in the main handle method

**Source stance:** explanation

**Context:**

> PR 7858 (Feat/INV-2276/alt emails), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 1701.

**Source-preserving request, proposal, or question:**

> Ah we already filter for this in the main handle method

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1701 · comment 456787557 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:1701 · comment 456787557 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-2276/alt emails

## A2-1721 — models: Maybe sort in here so we don’t need to care if groupBy changes ordering or not

**Source stance:** suggestion

**Context:**

> PR 7826 (Feat/INV-2227 pipe fund document url map), instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala; original row 1721.

**Source-preserving request, proposal, or question:**

> Maybe sort in here so we don’t need to care if groupBy changes ordering or not

**Conditions and limits:**

- Sort within helper instead of relying on groupBy ordering.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1721 · comment 453108369 · PR 7826 · 2023-12-13

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala`

**Evidence:** anon-2.jsonl:1721 · comment 453108369 · PR 7826 · 2023-12-13

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala`

**Explicit source context (pr_title):**

> Feat/INV-2227 pipe fund document url map

## A2-1725 — InvestmentRequestJdbcRepository: Hmm status filter is behaving same as before. I just move the createdAt check to logic layer, cuz we need to check cutOffDate first.

**Source stance:** explanation

**Context:**

> PR 7846 ([INV-2326] feat(investment): Enforce auto cancellation on cutoff date. Support illiquid alts initial investment), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentRequestJdbcRepository.scala; original row 1725.

**Concern stated in the source:** Hmm status filter is behaving same as before. I just move the createdAt check to logic layer, cuz we need to check cutOffDate first.

Performance wise, yes we will have more data to process, but I think should be cuz number of pending investment shouldn’t be too large?

**Source-preserving request, proposal, or question:**

> Hmm status filter is behaving same as before. I just move the createdAt check to logic layer, cuz we need to check cutOffDate first.
> 
> Performance wise, yes we will have more data to process, but I think should be cuz number of pending investment shouldn’t be too large?

**Conditions and limits:**

- createdAt check moves to logic after cutoff check; status filtering is unchanged, with increased pending-data processing considered acceptable but not benchmarked.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1725 · comment 454316925 · PR 7846 · 2023-12-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentRequestJdbcRepository.scala`

**Evidence:** anon-2.jsonl:1725 · comment 454316925 · PR 7846 · 2023-12-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentRequestJdbcRepository.scala`

**Explicit source context (pr_title):**

> [INV-2326] feat(investment): Enforce auto cancellation on cutoff date. Support illiquid alts initial investment

## A2-1729 — InstrumentPerformanceCache: Maybe we can use collect here… sth like this

**Source stance:** suggestion

**Context:**

> PR 7719 (Resolve INV-2348: support bulk look up of performance), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentPerformanceCache.scala; original row 1729.

**Concern stated in the source:** Maybe we can use collect here… sth like this

```
.map { maybePerformances =>
  maybePerformances.zip(inputs) collect {
    case (Some(performance), input) => input -> performance
  }
}
.map(_.toMap)
```

‌

**Source-preserving request, proposal, or question:**

> Maybe we can use collect here… sth like this
> 
> ```
> .map { maybePerformances =>
>   maybePerformances.zip(inputs) collect {
>     case (Some(performance), input) => input -> performance
>   }
> }
> .map(_.toMap)
> ```
> 
> ‌

**Conditions and limits:**

- Zip optional performance with inputs, collect Some pairs, then toMap.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1729 · comment 450193650 · PR 7719 · 2023-12-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentPerformanceCache.scala`

**Evidence:** anon-2.jsonl:1729 · comment 450193650 · PR 7719 · 2023-12-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentPerformanceCache.scala`

**Explicit source context (pr_title):**

> Resolve INV-2348: support bulk look up of performance

## A2-1790 — NewWealthDataFetcher: Nit: `Some(fundDetails.FundManager).filter(_.nonEmpty)`

**Source stance:** suggestion

**Context:**

> PR 7611 (Resolve INV-1796: New wealth sync/MStar on-demand sync), instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/newwealth/NewWealthDataFetcher.scala; original row 1790.

**Concern stated in the source:** Nit: `Some(fundDetails.FundManager).filter(_.nonEmpty)`

You can do sth similarly for risk level below too. In general, use idiomatic syntax as much as you can

**Source-preserving request, proposal, or question:**

> Nit: `Some(fundDetails.FundManager).filter(_.nonEmpty)`
> 
> You can do sth similarly for risk level below too. In general, use idiomatic syntax as much as you can

**Conditions and limits:**

- Some(FundManager).filter(_.nonEmpty) can express optional nonempty strings; analogous risk-level simplification is suggested.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1790 · comment 447874166 · PR 7611 · 2023-11-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/newwealth/NewWealthDataFetcher.scala`

**Evidence:** anon-2.jsonl:1790 · comment 447874166 · PR 7611 · 2023-11-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/newwealth/NewWealthDataFetcher.scala`

**Explicit source context (pr_title):**

> Resolve INV-1796: New wealth sync/MStar on-demand sync

## A3-0010 — ServiceLogicImpl.scala: Does this look better? ``` instrumentId .map(marketDataUploader.syncInstrumentMstarData) .getOrElse { // run in background marketDataUploader.safeSync

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; PR: Feat/INV-2229 marketdata ex dividend bond yield

**Source-preserving request, proposal, or question:**

> Does this look better?
> 
> ```
> instrumentId
>   .map(marketDataUploader.syncInstrumentMstarData)
>   .getOrElse {
>       // run in background
>       marketDataUploader.safeSyncInstrumentMstarData()
>       Future.successful(Done)
>   }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1816 · comment 442802096 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

> Does this look better?
> 
> ```
> instrumentId
>   .map(marketDataUploader.syncInstrumentMstarData)
>   .getOrElse {
>       // run in background
>       marketDataUploader.safeSyncInstrumentMstarData()
>       Future.successful(Done)
>   }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:1816 · comment 442802096 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +    }}
> +  }
> +
> +  override def getInstrumentMstarData(instrumentId: String): Future[Option[InstrumentMstarDataDto]] = {
> +    for {
> +      maybeInstrumentData <- instrumentMStarDataRepository.findByInstrumentId(instrumentId)
> +    } yield maybeInstrumentData.map(InstrumentMstarData.toDto)

## A3-0019 — ServiceLogicImplV2.scala: can extract for both ``` .map(it => it.map(InstrumentV1.toDto)) ```

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala; PR: Resolve INV-2146: Instrument V2 endpoint to validate and upsert to new entity

**Source-preserving request, proposal, or question:**

> can extract for both
> 
> ```
> .map(it => it.map(InstrumentV1.toDto))
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1827 · comment 440558470 · PR 7210 · 2023-10-31

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala`

> can extract for both
> 
> ```
> .map(it => it.map(InstrumentV1.toDto))
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:1827 · comment 440558470 · PR 7210 · 2023-10-31

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala`

**Explicit source context (hunk):**

> +      .map(oldInstrumentJdbcRepository.findByIds)
> +      .getOrElse(oldInstrumentJdbcRepository.findAll(List.empty))
> +      .map(it => it.map(InstrumentV1.toDto))
> +
> +    val simulateOnly = maybeSimulateOnly.getOrElse(true)
> +    val updateFromMStar = maybeUpdateFromMStar.getOrElse(false)
> +

## A3-0022 — ServiceLogicImplV2.scala: Or maybe just pass the Option\[Boolean\] to the other methods so we don’t need to resolve these booleans

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala; PR: Resolve INV-2146: Instrument V2 endpoint to validate and upsert to new entity

**Source-preserving request, proposal, or question:**

> Or maybe just pass the Option\[Boolean\] to the other methods so we don’t need to resolve these booleans

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1830 · comment 440559759 · PR 7210 · 2023-10-31

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala`

**Evidence:** anon-2.jsonl:1830 · comment 440559759 · PR 7210 · 2023-10-31

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala`

**Explicit source context (hunk):**

> +
> +    val simulateOnly = maybeSimulateOnly.getOrElse(true)
> +    val updateFromMStar = maybeUpdateFromMStar.getOrElse(false)
> +
> +    for {
> +      _ <- Future.unit
> +      _ = logger.info(s"Instrument sync started for ids: ${idList.getOrElse(List.empty)}, simulateOnly: $simulateOnly, pullFromMStar: $updateFromMStar.")

## A3-0032 — DailyMvAuditEntry array_agg/customerId optimization deferred over Slick GROUP BY issues

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvAuditEntryJdbcRepository.scala; PR: [INV-2015] feat(charge): Support estimated daily fee

**Concern stated in the source:** so that we can reduce the number of calls, but there are issues with slick and aggregate function with group by [<url> data-inline-card='' }  so I’m not taking chances

**Source-preserving request, proposal, or question:**

> We potentially can aggregate more in db layer, e.g.
> 
> ```
> SELECT customerId, array_agg(businessDate)
> ```
> 
> so that we can reduce the number of calls, but there are issues with slick and aggregate function with group by [<url> data-inline-card='' }  so I’m not taking chances

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- The array_agg/group-by optimization is explicitly deferred due to Slick issues, not required.

**Evidence:** anon-2.jsonl:1842 · comment 438138531 · PR 7266 · 2023-10-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvAuditEntryJdbcRepository.scala`

**Evidence:** anon-2.jsonl:1842 · comment 438138531 · PR 7266 · 2023-10-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvAuditEntryJdbcRepository.scala`

**Explicit source context (hunk):**

> +  implicit private val session: SlickSession = SlickSession.forDbAndProfile(database, ChargeServicePostgresProfile)
> +
> +  private val dailyMvAuditEntries = TableQuery[DailyMvAuditEntryTable]
> +
> +  def streamCustomerUpdatedMvBusinessDates(feeType: FeeType, from: Instant, to: Instant, businessDateCutOff: LocalDate): Source[CustomerUpdatedMvBusinessDate, NotUsed] = {
> +    Slick.source {
> +      dailyMvAuditEntries

## A3-0037 — No daily fee for a plan means remove: retain every planId and relevant MVs

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerFeesCalculator.scala; PR: [INV-2015] feat(charge): Support estimated daily fee

**Source-preserving request, proposal, or question:**

> To keep the logic of DailyFeeCalculationManager simple \(i.e. no daily fee returned for a plan = remove\), change this to retain all planIds. In fact, we have logic to default to empty List in many places.
> 
> Also changed to return only relevant MVs

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1847 · comment 438158731 · PR 7266 · 2023-10-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerFeesCalculator.scala`

**Evidence:** anon-2.jsonl:1847 · comment 438158731 · PR 7266 · 2023-10-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerFeesCalculator.scala`

**Explicit source context (hunk):**

> -      planIdToDailyFee = customerDailyFees.groupBy(_.planId),
> -      customerMvInPlanCcy = mvsInPlanCcy,
> -      customerMvInAccountingCcy = mvsInAccountingCcy
> +      planIdToDailyFee = relevantPlanChargeContexts.keys.map(planId => planId -> availableDailyFeesByPlanId.getOrElse(planId, List.empty)).toMap,
> +      customerMvInPlanCcy = relevantMvsInPlanCcy,
> +      customerMvInAccountingCcy = relevantMvsInAccountingCcy
>      )

## A3-0040 — BaseServiceLogicImpl.scala: Good catch. Let me just handle empty MV inside batchUpsert then

**Source stance:** requested-change

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala; PR: [INV-2015] feat(charge): Support estimated daily fee

**Source-preserving request, proposal, or question:**

> Good catch. Let me just handle empty MV inside batchUpsert then

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1850 · comment 440195725 · PR 7266 · 2023-10-30

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1850 · comment 440195725 · PR 7266 · 2023-10-30

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> -                mv <- db.run(dailyMvJdbcRepository.batchUpsert(dailyMvs)).map(_ => dailyMvs)
> -                r = if (mv.nonEmpty) {
> -                  s"Updated MV(${mv.length}). Customer: ${mv.head.customerId}, Plan: ${mv.head.planId}, GoalType: ${mv.head.goalType} Plan: ${mv.head.planId}, Ccy: ${mv.head.planCcy}, Business dates: ${mv.head.businessDate}."
> +                _ <- dailyMvPersistenceHelper.batchUpsert(
> +                  customerId = plan.customerId,
> +                  goalId = plan.goalId,
> +                  planId = plan.planId,

## A3-0072 — InstrumentDataUpdateManagerV2.scala: no need for comprehend if just single future

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Source-preserving request, proposal, or question:**

> Nit: no need for comprehend if just single future

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1888 · comment 437293213 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Evidence:** anon-2.jsonl:1888 · comment 437293213 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (hunk):**

> +
> +  def instrumentEntity: InstrumentV2Entity
> +  def dateTimeProvider: DateTimeProvider
> +  def instrumentJdbcRepository: InstrumentV2JdbcRepository
> +  def mstarApiService: MstarApiService
> +
> +  override def addInstrumentId(request: commons.AddInstrumentIdRequest): Future[InstrumentInfoDto] = {

## A3-0076 — InstrumentRetrievalManagerV2.scala: This should check for contain instead? Tmr we might add some other restrictions that applicable on top of offline rule right?

**Source stance:** open-question

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentRetrievalManagerV2.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Source-preserving request, proposal, or question:**

> This should check for contain instead? Tmr we might add some other restrictions that applicable on top of offline rule right?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1893 · comment 437302921 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentRetrievalManagerV2.scala`

**Evidence:** anon-2.jsonl:1893 · comment 437302921 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentRetrievalManagerV2.scala`

**Explicit source context (hunk):**

> +
> +    def isAltsB3(instrument: Instrument): Boolean =
> +      instrument.status == InstrumentStatus.Active &&
> +        instrument.tradingConfigDetails.tradingRestrictions.toList.contains(OfflineBuy, OfflineSell)
> +
> +    instrumentJdbcRepository.streamAllInstruments
> +      .filter(isAltsB3)

## A3-0077 — InstrumentV2EntityTest.scala: add a test case to cover that we merge/override existing map correctly with data from request for these update idMap/urlMap

**Source stance:** suggestion

**Context:**

> instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/instrument/v2/InstrumentV2EntityTest.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Source-preserving request, proposal, or question:**

> Maybe add a test case to cover that we merge/override existing map correctly with data from request for these update idMap/urlMap

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1894 · comment 437306426 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/instrument/v2/InstrumentV2EntityTest.scala`

**Evidence:** anon-2.jsonl:1894 · comment 437306426 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/instrument/v2/InstrumentV2EntityTest.scala`

**Explicit source context (hunk):**

> +      "update instrument id map successfully" in withEntitySetup(instrumentId) { driver =>
> +        val outcome = driver.runCommand(updateInstrumentIdCmd)
> +        outcome.state.instrument.get shouldBe updatedInstrument
> +        outcome.reply shouldBe InstrumentReply(updatedInstrument).success
> +        outcome.events should contain only InstrumentDetailsUpdatedEvt(updatedInstrument, "prodOps2@endowus.com")
> +      }
> +

## A3-0081 — InstrumentCommandsHandler.scala: Looks like we can use `i` here?

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommandsHandler.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Source-preserving request, proposal, or question:**

> Looks like we can use `i` here?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1898 · comment 438413299 · PR 7097 · 2023-10-24

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommandsHandler.scala`

**Evidence:** anon-2.jsonl:1898 · comment 438413299 · PR 7097 · 2023-10-24

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommandsHandler.scala`

**Explicit source context (hunk):**

> +        case cmd: UpdateInstrumentUrlCmd           => handleUpdateInstrumentUrlCmd(cmd, i)
> +        case cmd: UpdateInstrumentInvestorTypesCmd => handleUpdateInstrumentInvestorTypesCmd(cmd, i)
> +        case cmd: UpdateInstrumentIdCmd            => handleUpdateInstrumentIdCmd(cmd, i)
> +        case _                                     => handleBaseInstrument(cmd, i)
> +      }
> +  }
> +

## A3-0083 — TransactionV2AccountSerializerRegistry.scala: Don’t var if you can

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala; PR: Feat/INV-2152 hk v2 v3 migration processor

**Source-preserving request, proposal, or question:**

> Don’t var if you can

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1900 · comment 438075484 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala`

**Evidence:** anon-2.jsonl:1900 · comment 438075484 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala`

**Explicit source context (hunk):**

> +object TransactionMigratorHelper {
> +
> +  def fixCancelledStatusDetails(transactionJson: JsObject): JsObject = {
> +    val txnJson = transactionJson
> +    val innerTransactionJson = (txnJson \ "transaction").as[JsObject]
> +    val statusDetails = (transactionJson \ "transaction" \ "statusDetails").as[JsObject]
> +

## A3-0084 — TransactionV2AccountSerializerRegistry.scala: you have to update the field using \+\+ but still you don’t need to reassign to existing val?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala; PR: Feat/INV-2152 hk v2 v3 migration processor

**Source-preserving request, proposal, or question:**

> Yes you have to update the field using \+\+ but still you don’t need to reassign to existing val?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1901 · comment 438079279 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala`

**Evidence:** anon-2.jsonl:1901 · comment 438079279 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala`

**Explicit source context (hunk):**

> +object TransactionMigratorHelper {
> +
> +  def fixCancelledStatusDetails(transactionJson: JsObject): JsObject = {
> +    val txnJson = transactionJson
> +    val innerTransactionJson = (txnJson \ "transaction").as[JsObject]
> +    val statusDetails = (transactionJson \ "transaction" \ "statusDetails").as[JsObject]
> +

## A3-0097 — TransactionTypes.scala: Can we not use this style.. it’s very easy to make mistake. Just do: ``` case Some(settledOrder) => (Some(settledOrder.settledUnits), Some(settledUnit

**Source stance:** requested-change

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: [INV-1141] Fix transaction L1 dates for v2

**Source-preserving request, proposal, or question:**

> Can we not use this style.. it’s very easy to make mistake. Just do:
> 
> ```
> case Some(settledOrder) => (Some(settledOrder.settledUnits), Some(settledUnits.settledPrice))
> ```
> 
> 
> 
> Also let’s name this as `(units, price)`…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1914 · comment 434693143 · PR 7114 · 2023-10-11

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

> Can we not use this style.. it’s very easy to make mistake. Just do:
> 
> ```
> case Some(settledOrder) => (Some(settledOrder.settledUnits), Some(settledUnits.settledPrice))
> ```
> 
> ‌
> 
> Also let’s name this as `(units, price)`…

**Evidence:** anon-2.jsonl:1914 · comment 434693143 · PR 7114 · 2023-10-11

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> -      val (units, priceAmount) = order match {
> -        case Some(SettledOrderDto(_, _, _, _, _, _, settledUnits, settledAmount, _, _, _, _, _, _)) => (Some(settledUnits), Some(settledAmount))
> -        case _                                                                                      => (None, None)
> +      val (units, price) = order match {
> +        case Some(settledOrder: SettledOrderDto) => (Some(settledOrder.settledUnits), Some(settledOrder.settledPrice))
> +        case _                                   => (None, None)
>        }

## A3-0099 — Settled orders without isAssumed: collect/max date, zone start-of-day and confirmedAt fallback

**Source stance:** suggestion

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: [INV-1141] Fix transaction L1 dates for v2

**Source-preserving request, proposal, or question:**

> asInstanceOf \(or too much usage of it\) is a sign that you can refactor
> 
> ```
> val settledAt = sd.orders
>   .collect {
>     case order: SettledOrderDto if !order.isAssumed => order.settledDate
>   }
>   .maxByOption(_.toEpochDay)
>   .map(_.atStartOfDay(dateTimeProvider.zoneId))
>   .getOrElse(sd.confirmedAt)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 1916, 1921: maxByOption code example is followed by explicit Scala2.13-availability correction and TraversableOnceUtils import.

**Evidence:** anon-2.jsonl:1916 · comment 434757027 · PR 7114 · 2023-10-11

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

> asInstanceOf \(or too much usage of it\) is a sign that you can refactor
> 
> ```
> val settledAt = sd.orders
>   .collect {
>     case order: SettledOrderDto if !order.isAssumed => order.settledDate
>   }
>   .maxByOption(_.toEpochDay)
>   .map(_.atStartOfDay(dateTimeProvider.zoneId))
>   .getOrElse(sd.confirmedAt)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:1916 · comment 434757027 · PR 7114 · 2023-10-11

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> case sd: ConfirmedOrdersStatusDetailsDto =>
> +      val settledDate = sd.orders
> +        .collect {
> +          case order: SettledOrderDto if !order.isAssumed => order.settledDate
> +        }
> +        .maxByOption(_.toEpochDay)
> +        .map(_.atStartOfDay(dateTimeProvider.zoneId))

## A3-0104 — Scala2.13 maxByOption unavailable here: import TraversableOnceUtils

**Source stance:** requested-change

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: [INV-1141] Fix transaction L1 dates for v2

**Source-preserving request, proposal, or question:**

> I forgot maxByOption is scala 2.13
> 
> Import `TraversableOnceUtils` instead

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Scala 2.13 maxByOption availability is a source-specific compatibility constraint.
- Related source rows 1916, 1921: maxByOption code example is followed by explicit Scala2.13-availability correction and TraversableOnceUtils import.

**Evidence:** anon-2.jsonl:1921 · comment 434762157 · PR 7114 · 2023-10-11

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:1921 · comment 434762157 · PR 7114 · 2023-10-11

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> case sd: ConfirmedOrdersStatusDetailsDto =>
> +      val settledDate = sd.orders
> +        .collect {
> +          case order: SettledOrderDto if !order.isAssumed => order.settledDate
> +        }
> +        .maxByOption(_.toEpochDay)
> +        .map(_.atStartOfDay(dateTimeProvider.zoneId))

## A3-0124 — ServiceLogicImpl.scala: We have utils in OptionUtils so this can be written as ``` rpcCmsWebflowIdJdbcRepository .find(portfolioId, effectiveDate) .map(_.map { entry => RpcCm

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: Feat/INV-1986/rpc-communication-details-crud

**Source-preserving request, proposal, or question:**

> We have utils in OptionUtils so this can be written as
> 
> ```
> rpcCmsWebflowIdJdbcRepository
>   .find(portfolioId, effectiveDate)
>   .map(_.map { entry =>
>     RpcCmsWebflowIdEntryDto(
>       portfolioId = entry.portfolioId,
>       effectiveDate = entry.effectiveDate,
>       collectionId = entry.collectionId,
>       itemId = entry.itemId,
>       description = entry.description,
>       updatedAt = entry.updatedAt
>     )
>   }.onNone(logger.warn(...)))
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1942 · comment 429926815 · PR 6989 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

> We have utils in OptionUtils so this can be written as
> 
> ```
> rpcCmsWebflowIdJdbcRepository
>   .find(portfolioId, effectiveDate)
>   .map(_.map { entry =>
>     RpcCmsWebflowIdEntryDto(
>       portfolioId = entry.portfolioId,
>       effectiveDate = entry.effectiveDate,
>       collectionId = entry.collectionId,
>       itemId = entry.itemId,
>       description = entry.description,
>       updatedAt = entry.updatedAt
>     )
>   }.onNone(logger.warn(...)))
> ```
> 
> ‌

## A3-0125 — ServiceLogicImpl.scala: Same here, you don’t need to match. Can extract to reuse same toDto method as well ``` rpcCmsWebflowIdJdbcRepository .findByItemId(itemId) .map(_.map(

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: Feat/INV-1986/rpc-communication-details-crud

**Source-preserving request, proposal, or question:**

> Same here, you don’t need to match. Can extract to reuse same toDto method as well
> 
> ```
> rpcCmsWebflowIdJdbcRepository
>   .findByItemId(itemId)
>   .map(_.map(toDto))
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1943 · comment 429927351 · PR 6989 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

> Same here, you don’t need to match. Can extract to reuse same toDto method as well
> 
> ```
> rpcCmsWebflowIdJdbcRepository
>   .findByItemId(itemId)
>   .map(_.map(toDto))
> ```
> 
> ‌

## A3-0162 — models.scala: You can use the util in MapJsonFormat ``` implicit private val brokerRatioMapFormat: Format[Map[Broker, BigDecimal]] = new MapJsonFormat.EnumMap(Broke

**Source stance:** suggestion

**Context:**

> instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/v2/models.scala; PR: Resolve INV-1797: Instrument entity v2 initial work

**Source-preserving request, proposal, or question:**

> You can use the util in MapJsonFormat
> 
> ```
> implicit private val brokerRatioMapFormat: Format[Map[Broker, BigDecimal]] = new MapJsonFormat.EnumMap(Broker).mapFormat
> ```
> 
> Similar for other maps in this file

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1981 · comment 422627278 · PR 6760 · 2023-08-28

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/v2/models.scala`

**Evidence:** anon-2.jsonl:1981 · comment 422627278 · PR 6760 · 2023-08-28

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/v2/models.scala`

**Explicit source context (hunk):**

> +    implicit private val fixedRebateRatioFormat: Format[FixedRebateRatioDto] = Json.format
> +    implicit private val brokerBasedRebateRatioFormat: Format[BrokerBasedRebateRatioDto] = Json.format
> +    implicit val format: Format[TrailerRebateDto] = Json.format
> +  }
> +
> +  sealed trait FeeDetailsDto {
> +    def disclosures: Map[FeeStructureType, String]

## A3-0172 — InstrumentV2-to-V1 mapping: Either instead of exception-based conditional flow

**Source stance:** suggestion

**Context:**

> instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/converter/package.scala; PR: Resolve INV-1797: Instrument entity v2 initial work

**Source-preserving request, proposal, or question:**

> Nit: generally we would advise against using exception for these conditional flows. The smell hint is when I see we throw exception then only use e.getMessage later. Sometimes it’s unavoidable, but here you can make use of Either with for-comprehend
> 
> ```
> val maybeMappedInstrument = for {
>   trailerFeeRebateRatio <- instrument.trailerRebate match {
>     case fixedRebateRatioDto: FixedRebateRatioDto => Right(fixedRebateRatioDto.ratio)
>     case _: BrokerBasedRebateRatioDto             => Left("InstrumentInfoDto cannot convert [BrokerBasedRebateRatioDto] accurately.")
>   }
>   expenseRatio <- ...
>   benchmark <- ...
> } yield InstrumentInfoDto(...)
> 
> maybeMappedInstrument match {
>   case Right(value) => Some(value)
>   case Left(error) =>
>     logger.error(s"Error while converting v2 dto to v1 dto: $error")
>     None
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1991 · comment 430320199 · PR 6760 · 2023-09-25

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/converter/package.scala`

> Nit: generally we would advise against using exception for these conditional flows. The smell hint is when I see we throw exception then only use e.getMessage later. Sometimes it’s unavoidable, but here you can make use of Either with for-comprehend
> 
> ```
> val maybeMappedInstrument = for {
>   trailerFeeRebateRatio <- instrument.trailerRebate match {
>     case fixedRebateRatioDto: FixedRebateRatioDto => Right(fixedRebateRatioDto.ratio)
>     case _: BrokerBasedRebateRatioDto             => Left("InstrumentInfoDto cannot convert [BrokerBasedRebateRatioDto] accurately.")
>   }
>   expenseRatio <- ...
>   benchmark <- ...
> } yield InstrumentInfoDto(...)
> 
> maybeMappedInstrument match {
>   case Right(value) => Some(value)
>   case Left(error) =>
>     logger.error(s"Error while converting v2 dto to v1 dto: $error")
>     None
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:1991 · comment 430320199 · PR 6760 · 2023-09-25

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/converter/package.scala`

**Explicit source context (hunk):**

> +        case Some(_) => Left("InstrumentInfoDto cannot convert [BenchmarkDetailsDto] accurately.")
> +        case None    => Right(None)
> +      }
> +
> +    } yield
> +      InstrumentInfoDto(
> +        id = instrument.id,

## A3-0174 — models.scala: Should this be a List?

**Source stance:** open-question

**Context:**

> instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/v2/models.scala; PR: Resolve INV-1797: Instrument entity v2 initial work

**Source-preserving request, proposal, or question:**

> Should this be a List?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1993 · comment 430321919 · PR 6760 · 2023-09-25

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/v2/models.scala`

**Evidence:** anon-2.jsonl:1993 · comment 430321919 · PR 6760 · 2023-09-25

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/v2/models.scala`

**Explicit source context (hunk):**

> +    projectedReturns: Option[AsOf[ProjectedReturnDto]],
> +    feeComparison: Option[FeeComparisonDto],
> +    dueDiligenceDetails: DueDiligenceDetailsDto,
> +    performanceLabel: List[PerformanceLabelDto]
> +  ) {
> +    import EndowusDetailsDto.ValidationRules
> +

## A3-0202 — RedemptionTransactionV2Transformer.scala: You can write it as ``` transaction.settledAt.orElse(redemptionData.timestamps.completedAt).getOrElse(throw ...) ``` Is same same but I think it looks

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/RedemptionTransactionV2Transformer.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> You can write it as
> 
> ```
> transaction.settledAt.orElse(redemptionData.timestamps.completedAt).getOrElse(throw ...)
> ```
> 
> 
> 
> Is same same but I think it looks a bit cleaner

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2023 · comment 427009962 · PR 6863 · 2023-09-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/RedemptionTransactionV2Transformer.scala`

> You can write it as
> 
> ```
> transaction.settledAt.orElse(redemptionData.timestamps.completedAt).getOrElse(throw ...)
> ```
> 
> ‌
> 
> Is same same but I think it looks a bit cleaner

**Evidence:** anon-2.jsonl:2023 · comment 427009962 · PR 6863 · 2023-09-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/RedemptionTransactionV2Transformer.scala`

**Explicit source context (hunk):**

> +          },
> +          futFallback = for {
> +            planRedemptions <- redemptionService.getRedemptionRequests(transaction.planId.get).invoke()
> +            redemptionData = planRedemptions.find(_.redemptionRequestId == transaction.transactionId).getOrElse(
> +              throw NotFound(s"redemptionId ${transaction.transactionId} not found in redemption entity of ${transaction.planId.get}!")
> +            )
> +          } yield redemptionData

## A3-0203 — TransactionServiceImpl.scala: `accountType.map(TradingAccountType.withName)` should work?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/TransactionServiceImpl.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> `accountType.map(TradingAccountType.withName)` should work?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2024 · comment 427010807 · PR 6863 · 2023-09-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/TransactionServiceImpl.scala`

> `accountType.map(TradingAccountType.withName)` should work?
> 
> ‌

**Evidence:** anon-2.jsonl:2024 · comment 427010807 · PR 6863 · 2023-09-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/TransactionServiceImpl.scala`

**Explicit source context (hunk):**

> +        require(customerId.isDefined, "customerId should be defined!")
> +        for {
> +          customerTransactions <- logic.queryCustomerTransactions(
> +            customerId = customerId.get,
> +            accountType = accountType.map(TradingAccountType.withName),
> +            goalId = goalId,
> +            planId = planId,

## A3-0225 — UUID+CustomerStatus cache estimate32MB/1mio versus larger plan-market-value map

**Source stance:** explanation

**Context:**

> rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculator.scala; PR: [INV-1703] feat(rebate): Exclude all plans of inactive customers from rebate distribution

**Source-preserving request, proposal, or question:**

> UUID is 16 bytes, together with CustomerStatus maybe total 32 bytes at max. This map will eat 32MB if we have 1mio customers.
> 
> If any memory problem, I suppose `Map[UUID, PlanMarketValue]` will get first

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve approximate source estimate: UUID 16 bytes, UUID plus CustomerStatus at most 32 bytes, 1mio customers ~32MB; larger Map[UUID,PlanMarketValue] concern is separate.

**Evidence:** anon-2.jsonl:2048 · comment 425257867 · PR 6872 · 2023-09-06

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculator.scala`

**Evidence:** anon-2.jsonl:2048 · comment 425257867 · PR 6872 · 2023-09-06

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculator.scala`

**Explicit source context (hunk):**

> +class DistributionCalculator(customerService: RegionalCustomerService)(implicit ec: ExecutionContext, mat: Materializer) extends StrictLogging {
> +
> +  private val customerStatusCache: AsyncLoadingCache[UUID, CustomerStatus] =
> +    Scaffeine()
> +      .recordStats()
> +      .expireAfterWrite(1.day)
> +      .maximumSize(100000)

## A3-0239 — BasePlanRecurringInvestmentScheduleManager.scala: Can just use `schedule` cuz we already validate here?

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala; PR: [EN-1992] Add support for recurring investment expiring communications

**Concern stated in the source:** Can just use `schedule` cuz we already validate here?

**Source-preserving request, proposal, or question:**

> Can just use `schedule` cuz we already validate here?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2062 · comment 425177660 · PR 6715 · 2023-09-06

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Evidence:** anon-2.jsonl:2062 · comment 425177660 · PR 6715 · 2023-09-06

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Explicit source context (hunk):**

> +          {
> +            val (schedule, index) = retrievedCustomerWithIndex
> +            val count = index + 1
> +            logger.info(
> +              s"[RECURRING-EXPIRED-TRIGGER][count: $count] for plan ${schedule.planId} for customer ${schedule.customerId}|${schedule.tradingAccountType} using the date [$executeDate]"
> +            )
> +          }

## A3-0245 — PlanCommunicationV2EventProcessor.scala: Why we need to `.map(_ => Done)` again?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-2017] Add support for recurring investment expired removal

**Source-preserving request, proposal, or question:**

> Why we need to `.map(_ => Done)` again?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2068 · comment 425178267 · PR 6804 · 2023-09-06

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2068 · comment 425178267 · PR 6804 · 2023-09-06

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> -        } yield Done
> +            Future.successful(Done)
> +          case Some(removalReason) =>
> +            sendRecurringInvestmentStoppedCommunication(event, previousSchedule, removalReason)
> +          case None =>
> +            sendRecurringInvestmentStoppedCommunication(event, previousSchedule, RecurringInvestmentScheduleRemovalReason.Others)
> +        }

## A3-0255 — RecurringInvestmentScheduleJdbcEventProcessor.scala: You’ll need for-comprehend block

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> You’ll need for-comprehend block

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2078 · comment 422182815 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2078 · comment 422182815 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +
> +  private[processors] def handlePlanCreated(ele: EventEnvelope[PlanCreatedEvt]): Future[Unit] = {
> +    val event = ele.event
> +    for {
> +      _ <- upsert(
> +        ele = ele,
> +        goalId = event.plan.goalId,

## A3-0266 — PlanRecurringInvestmentScheduleDbItem.scala: Isn’t it clearer if we don’t pair these in a single patten match ``` config.flatMap { case SpecificEndDate(userEndDate) => Some(userEndDate) case _: O

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/PlanRecurringInvestmentScheduleDbItem.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> Isn’t it clearer if we don’t pair these in a single patten match
> 
> ```
> config.flatMap {
>   case SpecificEndDate(userEndDate) => Some(userEndDate)
>   case _: Ocurrences => endoingOn
> }
> ```
> 
> assuming endoingOn is populated correctly for ocurrences case..

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2090 · comment 422622485 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/PlanRecurringInvestmentScheduleDbItem.scala`

**Evidence:** anon-2.jsonl:2090 · comment 422622485 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/PlanRecurringInvestmentScheduleDbItem.scala`

**Explicit source context (hunk):**

> +    config.flatMap {
> +      case SpecificEndDate(userEndDate) => Some(userEndDate)
> +      case _: Occurrences               => endingOn
> +    }
> +}

## A3-0272 — scheduledInvestmentId flatMap, matching startingFrom/interval, max sequence+1

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RecurringInvestmentScheduleHelper.scala; PR: More recurring cmd processors schedulers

**Source-preserving request, proposal, or question:**

> Nit: this bit doesn’t look idiomatic \(we filter with isDefined then later calling get directly on Option field\)
> 
> Normally, we should flatMap for these cases.
> 
> ```
> investmentRequests
>   .flatMap(_.scheduledInvestmentId)
>   .filter(s => s.startingFrom == recurringSchedule.startingFrom && s.interval == recurringSchedule.interval)
>   .map(_.sequence)
>   .maxByOption(identity)
>   .map(_ + 1)
>   .getOrElse(0)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2096 · comment 419092813 · PR 6558 · 2023-08-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RecurringInvestmentScheduleHelper.scala`

> Nit: this bit doesn’t look idiomatic \(we filter with isDefined then later calling get directly on Option field\)
> 
> Normally, we should flatMap for these cases.
> 
> ```
> investmentRequests
>   .flatMap(_.scheduledInvestmentId)
>   .filter(s => s.startingFrom == recurringSchedule.startingFrom && s.interval == recurringSchedule.interval)
>   .map(_.sequence)
>   .maxByOption(identity)
>   .map(_ + 1)
>   .getOrElse(0)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2096 · comment 419092813 · PR 6558 · 2023-08-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RecurringInvestmentScheduleHelper.scala`

**Explicit source context (hunk):**

> +      .filter(s => s.startingFrom == recurringSchedule.startingFrom && s.interval == recurringSchedule.interval)
> +      .map(_.sequence)
> +      .maxByOption(identity)
> +      .map(_ + 1)
> +      .getOrElse(0)
> +  }
> +

## A3-0338 — TransactionTypes.scala: t.taxDetails is already Option no?

**Source stance:** open-question

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Source-preserving request, proposal, or question:**

> t.taxDetails is already Option no?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2163 · comment 419068580 · PR 6671 · 2023-08-14

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

## A3-0341 — RedemptionRequestTopicSubscriberV2.scala: pattern match on `request.feeChargeDetails`, extract the mapping methods so it’s easier to follow

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Source-preserving request, proposal, or question:**

> Nit: pattern match on `request.feeChargeDetails`, extract the mapping methods so it’s easier to follow

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2166 · comment 419069909 · PR 6671 · 2023-08-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2166 · comment 419069909 · PR 6671 · 2023-08-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> -    } else {
> +  ): Transaction = {
> +    def buildFeeRedemptionTransaction(feeChargeDetail: FeeChargeDetailsDto): FeeRedemptionTransaction = {
> +      val settledAmount = request.settlementConfirmation.map(_.tradeSettlementConfirmAmount)
> +      val assumedAmount = request.settlementAssumption.map(_.tradeSettlementAssumedAmount)
> +      val chargeAmounts =
> +        calculateChargedByCashAndBySellAmount(

## A3-0343 — RedemptionRequestTopicSubscriberV2.scala: Do we need this filter? Just default to 0? ``` r.confirmedAmount.getOrElse(r.assumedAmount.getOrElse(r.orderAmount.getOrElse(BigDecimal(0)))) ```

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Source-preserving request, proposal, or question:**

> Do we need this filter? Just default to 0?
> 
> ```
> r.confirmedAmount.getOrElse(r.assumedAmount.getOrElse(r.orderAmount.getOrElse(BigDecimal(0))))
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2168 · comment 419070312 · PR 6671 · 2023-08-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

> Do we need this filter? Just default to 0?
> 
> ```
> r.confirmedAmount.getOrElse(r.assumedAmount.getOrElse(r.orderAmount.getOrElse(BigDecimal(0))))
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2168 · comment 419070312 · PR 6671 · 2023-08-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +   */
> +  private def calculateChargedByCashAndBySellAmount(
> +    tradingAccountType: TradingAccountType,
> +    request: RedemptionRequestDto,
> +    transactionAmount: BigDecimal
> +  ): ChargedByCashAndSellAmount = {
> +    val isCashAccount = TradingAccountType.cashAccountSet.contains(tradingAccountType)

## A3-0352 — RedemptionRequestTopicSubscriberV2.scala: Can we pattern match outside and break this into 2 methods

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Source-preserving request, proposal, or question:**

> Can we pattern match outside and break this into 2 methods

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2177 · comment 419358838 · PR 6671 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2177 · comment 419358838 · PR 6671 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> -      throw new Exception("FEE_REDEMPTION transaction not yet implemented")
> -    } else {
> +  ): Transaction = {
> +    def buildFeeRedemptionTransaction(feeChargeDetail: FeeChargeDetailsDto): FeeRedemptionTransaction = {
> +      val settledAmount = request.settlementConfirmation.map(_.tradeSettlementConfirmAmount)
> +      val assumedAmount = request.settlementAssumption.map(_.tradeSettlementAssumedAmount)
> +      val chargeAmounts =

## A3-0353 — RedemptionRequestTopicSubscriberV2.scala: Can just return, no need to assign here. In fact, assigning here create chance for the bug last time, cuz the underlying type is lost via type erasure

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Concern stated in the source:** In fact, assigning here create chance for the bug last time, cuz the underlying type is lost via type erasure

**Source-preserving request, proposal, or question:**

> Can just return, no need to assign here. In fact, assigning here create chance for the bug last time, cuz the underlying type is lost via type erasure

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Source identifies erased type risk when assigning an intermediate value; direct return is the proposed repair.

**Evidence:** anon-2.jsonl:2178 · comment 419359443 · PR 6671 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2178 · comment 419359443 · PR 6671 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  /**
> +   * We returned Option[BigDecimal] here for the express reason to not show 0 on FE
> +   */
> +  private def calculateChargedByCashAndBySellAmount(
> +    tradingAccountType: TradingAccountType,

## A3-0354 — RedemptionRequestTopicSubscriberV2.scala: Does this look better? ``` val amountChargedBySell = request.orders .map(o => o.confirmedAmount.getOrElse(o.assumedAmount.getOrElse(o.orderAmount.getO

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Source-preserving request, proposal, or question:**

> Does this look better?
> 
> ```
> val amountChargedBySell = request.orders
>   .map(o => o.confirmedAmount.getOrElse(o.assumedAmount.getOrElse(o.orderAmount.getOrElse(BigDecimal(0)))))
>   .sum
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2180 · comment 419359870 · PR 6671 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

> Does this look better?
> 
> ```
> val amountChargedBySell = request.orders
>   .map(o => o.confirmedAmount.getOrElse(o.assumedAmount.getOrElse(o.orderAmount.getOrElse(BigDecimal(0)))))
>   .sum
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2180 · comment 419359870 · PR 6671 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +   * We returned Option[BigDecimal] here for the express reason to not show 0 on FE
> +   */
> +  private def calculateChargedByCashAndBySellAmount(
> +    tradingAccountType: TradingAccountType,
> +    request: RedemptionRequestDto,
> +    transactionAmount: BigDecimal
> +  ): ChargedByCashAndSellAmount = {

## A3-0355 — RedemptionRequestTopicSubscriberV2.scala: Better to maintain parity ``` val amountChargedBySell = ... val amountChargedByCash = ... (Some(amountChargedBySell), Some(amountChargedByCash)) ```

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Source-preserving request, proposal, or question:**

> Better to maintain parity
> 
> ```
> val amountChargedBySell = ...
> val amountChargedByCash = ...
> 
> (Some(amountChargedBySell), Some(amountChargedByCash))
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2181 · comment 419360221 · PR 6671 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

> Better to maintain parity
> 
> ```
> val amountChargedBySell = ...
> val amountChargedByCash = ...
> 
> (Some(amountChargedBySell), Some(amountChargedByCash))
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2181 · comment 419360221 · PR 6671 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +            request.orders
> +              .map(r => r.confirmedAmount.orElse(r.assumedAmount).orElse(r.orderAmount).getOrElse(BigDecimal(0)))
> +              .sum
> +        }
> +      } else
> +        //For CPF and SRS
> +        //Flow: full redemption to UOBKH trust account, then withdraw from trust account.

## A3-0356 — RedemptionRequestTopicSubscriberV2.scala: ``` request.cashReservations.map(_.reservedAmount).sum ```

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Source-preserving request, proposal, or question:**

> ```
> request.cashReservations.map(_.reservedAmount).sum
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2182 · comment 419360256 · PR 6671 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

> ```
> request.cashReservations.map(_.reservedAmount).sum
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2182 · comment 419360256 · PR 6671 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +      if (isCashAccount) {
> +        request.orders.headOption.map{ _ =>
> +            request.orders
> +              .map(r => r.confirmedAmount.orElse(r.assumedAmount).orElse(r.orderAmount).getOrElse(BigDecimal(0)))
> +              .sum
> +        }
> +      } else

## A3-0360 — RedemptionRequestTopicSubscriberV2.scala: Actually there’s a better method for this: ``` settledAmount.orElse(assumedAmount).getOrElse(request.requestedAmount) ```

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Source-preserving request, proposal, or question:**

> Actually there’s a better method for this:
> 
> ```
> settledAmount.orElse(assumedAmount).getOrElse(request.requestedAmount)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2186 · comment 419687074 · PR 6671 · 2023-08-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

> Actually there’s a better method for this:
> 
> ```
> settledAmount.orElse(assumedAmount).getOrElse(request.requestedAmount)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2186 · comment 419687074 · PR 6671 · 2023-08-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +        calculateChargedByCashAndBySellAmount(
> +          tradingAccountType = tradingAccountType,
> +          request = request,
> +          transactionAmount = settledAmount
> +            .orElse(assumedAmount)
> +            .getOrElse(request.requestedAmount)
> +        )

## A3-0361 — RedemptionRequestTopicSubscriberV2.scala: Same can use orElse here

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Source-preserving request, proposal, or question:**

> Same can use orElse here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2187 · comment 419687544 · PR 6671 · 2023-08-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2187 · comment 419687544 · PR 6671 · 2023-08-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +              .map(r => r.confirmedAmount.orElse(r.assumedAmount).orElse(r.orderAmount).getOrElse(BigDecimal(0)))
> +              .sum
> +        }
> +      } else
> +        //For CPF and SRS
> +        //Flow: full redemption to UOBKH trust account, then withdraw from trust account.
> +        //This would be shown as withdrawal from "cash" in UI, which is confusing (it's from redemption).

## A3-0370 — DistributionPreferenceDecider.scala: `.exists(_.isPrimary)` should be enough

**Source stance:** suggestion

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividenddistribution/processors/DistributionPreferenceDecider.scala; PR: TT-2732 add validation check that bank account must exist for dividend withdrawal

**Source-preserving request, proposal, or question:**

> Nit: `.exists(_.isPrimary)` should be enough

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2196 · comment 419087090 · PR 6697 · 2023-08-14

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividenddistribution/processors/DistributionPreferenceDecider.scala`

**Evidence:** anon-2.jsonl:2196 · comment 419087090 · PR 6697 · 2023-08-14

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividenddistribution/processors/DistributionPreferenceDecider.scala`

**Explicit source context (hunk):**

> planDividendPortion >= getMinWithdrawalAmount(ccy)
>  
> +  private def hasPrimaryBankAccount(customerId: UUID): Future[Boolean] =
> +    customerService.getRegionalCustomerBankAccountDetails(customerId).invoke().map(_.hasPrimaryBankAccount)
> +
>    private def isCpfOrSrs(plan: PlanDto): Boolean =
>      TradingAccountType.cpfAndSrsAccountSet.contains(plan.tradingAccountType)

## A3-0379 — SgInvestmentServiceImpl.scala: can be written as below so that we call derive once ``` .map { schedule => (schedule, schedule.derive(...)) } .collect { case (schedule, missingDates)

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/SgInvestmentServiceImpl.scala; PR: [ONB-2585] Add endpoint to retrieve missing recurring investments

**Concern stated in the source:** Nit: can be written as below so that we call derive once

**Source-preserving request, proposal, or question:**

> Nit: can be written as below so that we call derive once
> 
> ```
> .map { schedule => (schedule, schedule.derive(...)) }
> .collect {
>   case (schedule, missingDates) if missingDates.nonEmpty => MissingInvestmentTransactionDto(...)
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2206 · comment 416503915 · PR 6619 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/SgInvestmentServiceImpl.scala`

> Nit: can be written as below so that we call derive once
> 
> ```
> .map { schedule => (schedule, schedule.derive(...)) }
> .collect {
>   case (schedule, missingDates) if missingDates.nonEmpty => MissingInvestmentTransactionDto(...)
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2206 · comment 416503915 · PR 6619 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/SgInvestmentServiceImpl.scala`

**Explicit source context (hunk):**

> +    for {
> +      investments <- investmentScheduleActivePeriodJdbcRepository.findAllInvestmentSchedulesByCustomer(customerId)
> +      result = investments
> +        .map { schedule => (schedule, InvestmentScheduleActivePeriod.deriveMissingRequestedDates(schedule, dateTimeProvider.localDateNow)) }
> +        .collect {
> +          case (schedule, missingDates) if missingDates.nonEmpty => MissingInvestmentTransactionDto(
> +            planId = schedule.planId,

## A3-0380 — SgInvestmentServiceImpl.scala: Haha should have used `missingDates` here, but it’s alright

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/SgInvestmentServiceImpl.scala; PR: [ONB-2585] Add endpoint to retrieve missing recurring investments

**Source-preserving request, proposal, or question:**

> Haha should have used `missingDates` here, but it’s alright

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2207 · comment 416566665 · PR 6619 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/SgInvestmentServiceImpl.scala`

**Evidence:** anon-2.jsonl:2207 · comment 416566665 · PR 6619 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/SgInvestmentServiceImpl.scala`

**Explicit source context (hunk):**

> +            recurringAmount = schedule.recurringAmount,
> +            startingDate = schedule.startingDate,
> +            endingDate = schedule.endingDate,
> +            missingDates = InvestmentScheduleActivePeriod.deriveMissingRequestedDates(schedule, dateTimeProvider.localDateNow)
> +          )
> +        }
> +    } yield result.toList

## A3-0384 — InvestmentScheduleActivePeriod.scala: You can use the common method ``` Iterator.iterate(startingDate)(_.plus(CashflowInterval.toTemporalAmount(recurringInterval))) ```

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/models/InvestmentScheduleActivePeriod.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> You can use the common method
> 
> ```
> Iterator.iterate(startingDate)(_.plus(CashflowInterval.toTemporalAmount(recurringInterval)))
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2211 · comment 416496663 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/models/InvestmentScheduleActivePeriod.scala`

> You can use the common method
> 
> ```
> Iterator.iterate(startingDate)(_.plus(CashflowInterval.toTemporalAmount(recurringInterval)))
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2211 · comment 416496663 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/models/InvestmentScheduleActivePeriod.scala`

**Explicit source context (hunk):**

> +  def deriveTransactedDates(activePeriod: InvestmentScheduleActivePeriod, dateToday: LocalDate): List[LocalDate] = {
> +    val endDateToUse = activePeriod.endingDate.getOrElse(dateToday)
> +
> +    Iterator.iterate(activePeriod.startingDate)(_.plus(CashflowInterval.toTemporalAmount(activePeriod.recurringInterval)))
> +      .takeWhile(date => !date.isAfter(endDateToUse))
> +      .toList
> +  }

## A3-0401 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: the better syntax would be ``` _ <- investmentPlan.recurringInvestmentSchedule match { case Some(schedule) => repository.upsert(...) case None => Futu

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Nit: the better syntax would be
> 
> ```
> _ <- investmentPlan.recurringInvestmentSchedule match {
>   case Some(schedule) => repository.upsert(...)
>   case None => Future.successful(Done)
> }
> ```
> 
> This way you don’t need to call Option.get

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2228 · comment 416513540 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2228 · comment 416513540 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +      _ <- investmentPlanFromEvt.recurringInvestmentSchedule match {
> +        case Some(_) =>
> +          investmentScheduleActivePeriodJdbcRepository.upsert(
> +            InvestmentScheduleActivePeriod(
> +              customerId = investmentPlanFromEvt.customerId,
> +              tradingAccountType = investmentPlanFromEvt.tradingAccountType,
> +              planId = planId,

## A3-0408 — SgServiceLogicImpl.scala: Clearer to use `planMarketValues.values.map(_.totalMarketValue)` I think

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> Clearer to use `planMarketValues.values.map(_.totalMarketValue)` I think

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2237 · comment 409388598 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2237 · comment 409388598 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +        goalId = goalId,
> +        goalPerformanceMetrics = goalPerformanceMetrics,
> +        riskTargetPerformanceMetricsMap = riskTargetPerformanceMetricsMap
> +      )
> +      result
> +    }
> +  }

## A3-0409 — SgServiceLogicImpl.scala: Should we calculate MV grouped by planId, then use it for the total in step 1? So we don’t need to repeat that logic here

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> Should we calculate MV grouped by planId, then use it for the total in step 1? So we don’t need to repeat that logic here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2239 · comment 409389275 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

## A3-0410 — SgServiceLogicImpl.scala: So this step is basically split the planMV by TAA for each plan right? See if you can reuse `Calculator#distributeAmountByWeight` in silver-commons

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> So this step is basically split the planMV by TAA for each plan right? See if you can reuse `Calculator#distributeAmountByWeight` in silver-commons

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2240 · comment 409389663 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

## A3-0411 — SgServiceLogicImpl.scala: And this step is to split MV per instrument back into weight. See if you can see `Calculator#weightedRatios`

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> And this step is to split MV per instrument back into weight. See if you can see `Calculator#weightedRatios`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2241 · comment 409390164 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

## A3-0412 — SgServiceLogicImpl.scala: Should we just use `ModelPortfolioRiskTarget.values`?

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> Should we just use `ModelPortfolioRiskTarget.values`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2242 · comment 409390772 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2242 · comment 409390772 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> with BaseServiceLogicImpl
> +    with ComputePerformanceOfAdHocTaa
> +    with GenerateCombinedTaaHelper
>      with StrictLogging {
>  
> +  override def calculateGoalPerformancesAcrossRelatedRiskDrivenPortfolios (
> +    goalId: UUID

## A3-0420 — Risk-target performance example uses mapAsync2 over risks and mapAsync1 over plans

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> I give it a go…
> 
> ```
> riskTargetPerformanceMetricsMap <- Source(riskTargets)
>   .mapAsync(2) { riskTarget =>
>     val riskToleranceLevel = RiskToleranceUtils.riskToleranceLevelForUsage(riskTarget)
>     val targetStockRatio = RiskToleranceUtils.mapToTargetStockRatioForGeneralInvesting(riskToleranceLevel).getOrElse(...)
>     for {
>       planRiskTargetPortfolioTaaMap <- Source(validPlans)
>         .mapAsync(1) { plan =>
>           lookupProductPortfolioTaa(advisoryTag, targetStockRatio, plan.tradingAccountType).map(plan.planId -> _)
>         }
>         .runWith(Sink.seq)
>         .map(_.toMap)
> 
>       riskTargetGoalTaa = generateCombinedTaa(planMarketValues, planRiskTargetPortfolioTaaMap)
> 
>       performanceMetrics <- getPerformanceMetrics(taa = riskTargetGoalTaa, ccy = planCcy, period = PerformanceMetricsPeriodEnum.COMMON)
>         .map(response => response.performanceMetrics)
>     } yield riskTarget -> performanceMetrics
>   }
>   .runWith(Sink.seq)
>   .map(_.toMap)
> 
> goalRiskTarget = ModelPortfolioRiskTarget.calculateRiskTargetFromStockRatio(goal.targetStockRatio)
> goalPerformanceMetrics = riskTargetPerformanceMetricsMap.find(goalRiskTarget).getOrElse(...)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve nested mapAsync parallelism 2 over riskTargets and 1 over validPlans, risk ratio mapping, common-period performance, and goal risk lookup.

**Evidence:** anon-2.jsonl:2250 · comment 411332427 · PR 6389 · 2023-07-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

> I give it a go…
> 
> ```
> riskTargetPerformanceMetricsMap <- Source(riskTargets)
>   .mapAsync(2) { riskTarget =>
>     val riskToleranceLevel = RiskToleranceUtils.riskToleranceLevelForUsage(riskTarget)
>     val targetStockRatio = RiskToleranceUtils.mapToTargetStockRatioForGeneralInvesting(riskToleranceLevel).getOrElse(...)
>     for {
>       planRiskTargetPortfolioTaaMap <- Source(validPlans)
>         .mapAsync(1) { plan =>
>           lookupProductPortfolioTaa(advisoryTag, targetStockRatio, plan.tradingAccountType).map(plan.planId -> _)
>         }
>         .runWith(Sink.seq)
>         .map(_.toMap)
> 
>       riskTargetGoalTaa = generateCombinedTaa(planMarketValues, planRiskTargetPortfolioTaaMap)
> 
>       performanceMetrics <- getPerformanceMetrics(taa = riskTargetGoalTaa, ccy = planCcy, period = PerformanceMetricsPeriodEnum.COMMON)
>         .map(response => response.performanceMetrics)
>     } yield riskTarget -> performanceMetrics
>   }
>   .runWith(Sink.seq)
>   .map(_.toMap)
> 
> goalRiskTarget = ModelPortfolioRiskTarget.calculateRiskTargetFromStockRatio(goal.targetStockRatio)
> goalPerformanceMetrics = riskTargetPerformanceMetricsMap.find(goalRiskTarget).getOrElse(...)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2250 · comment 411332427 · PR 6389 · 2023-07-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +          )
> +        advisoryTag = getAdvisoryTagFromProductLineAndIntent(product = productLineAndIntent)
> +        riskTargetPerformanceMetricsMap <- Source(riskTargets)
> +          .mapAsync(2) { riskTarget =>
> +            val riskToleranceLevel = RiskToleranceUtils.riskToleranceLevelForUsage(riskTarget)
> +            val targetStockRatio = RiskToleranceUtils.mapToTargetStockRatioForGeneralInvesting(riskToleranceLevel)
> +              .getOrElse(throw BadRequest(

## A3-0421 — AdHocTaaHelpers.scala: Seems not used… but otherwise, `planMarketValues.size` is good

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/AdHocTaaHelpers.scala; PR: Feat/INV-1633/goal perf across risk targets

**Concern stated in the source:** Seems not used… but otherwise, `planMarketValues.size` is good

**Source-preserving request, proposal, or question:**

> Seems not used… but otherwise, `planMarketValues.size` is good

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2251 · comment 411335089 · PR 6389 · 2023-07-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/AdHocTaaHelpers.scala`

**Evidence:** anon-2.jsonl:2251 · comment 411335089 · PR 6389 · 2023-07-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/AdHocTaaHelpers.scala`

**Explicit source context (hunk):**

> +
> +  def generateCombinedTaa(planMarketValues: Map[UUID, MarketValueDto], planInstrumentTargetsMap: Map[UUID, Map[String, BigDecimal]]): Map[String, BigDecimal] = {
> +    val planMvs = planMarketValues.map { case (planId, mv) =>
> +      planId -> {
> +        val assumedMv = mv.totalMarketValue
> +        val pendingInvestment = mv.pendingInvestmentAmountTotal.getOrElse(BigDecimal(0))
> +        assumedMv + pendingInvestment

## A3-0422 — AdHocTaaHelpers.scala: Use Calculator.weightedRatio here too

**Source stance:** requested-change

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/AdHocTaaHelpers.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> Use Calculator.weightedRatio here too

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2252 · comment 411338540 · PR 6389 · 2023-07-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/AdHocTaaHelpers.scala`

**Evidence:** anon-2.jsonl:2252 · comment 411338540 · PR 6389 · 2023-07-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/AdHocTaaHelpers.scala`

**Explicit source context (hunk):**

> +      planInstrumentTargetsMap.mapValues(_ => BigDecimal(1)) // using the plan targets map as planMvs can return empty Map
> +    } else {
> +      planMvs
> +    }
> +
> +    val aggregatedInstrumentWeights = planInstrumentTargetsMap
> +      .toSeq

## A3-0423 — Combined TAA weights use assumedMV+pending investment; equal weights when all zero

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/AdHocTaaHelpers.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> On 2nd thought, maybe we can structure the code a bit to treat planMvs as weight
> 
> ```
>   def generateCombinedTaa(planMarketValues: Map[UUID, MarketValueDto], planInstrumentTargetsMap: Map[UUID, Map[String, BigDecimal]]): Map[String, BigDecimal] = {
>     val planMvs = planMarketValues.map { case (planId, mv) =>
>       planId -> {
>         val assumedMv = mv.totalMarketValue
>         val pendingInvestment = mv.pendingInvestmentAmountTotal.getOrElse(BigDecimal(0))
>         assumedMv + pendingInvestment
>       }
>     }
> 
>     // Use planMvs as weighted among the plans
>     // If no MV, assume all plans have same weight
>     val planWeights = if (planMvs.values.sum == 0) {
>       planMvs.mapValues(_ => BigDecimal(1))
>     } else {
>       planMvs
>     }
> 
>     val aggregatedInstrumentWeights = planInstrumentTargetsMap
>       .toSeq
>       .flatMap { case (planId, taa) =>
>         taa.mapValues(_ * planWeights(planId))
>       }
>       .groupBy { case (instrument, _) => instrument }
>       .map { case (instrument, targetMvsOfInstrument) =>
>         instrument -> targetMvsOfInstrument.map(_._2).sum
>       }
>     
>     Calculator.weightedRatios(aggregatedInstrumentWeights)
>   }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Source example weights each plan by assumedMV plus pending investment; all-zero plan MVs receive weight1 before aggregation and Calculator.weightedRatios.

**Evidence:** anon-2.jsonl:2253 · comment 411340511 · PR 6389 · 2023-07-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/AdHocTaaHelpers.scala`

> On 2nd thought, maybe we can structure the code a bit to treat planMvs as weight
> 
> ```
>   def generateCombinedTaa(planMarketValues: Map[UUID, MarketValueDto], planInstrumentTargetsMap: Map[UUID, Map[String, BigDecimal]]): Map[String, BigDecimal] = {
>     val planMvs = planMarketValues.map { case (planId, mv) =>
>       planId -> {
>         val assumedMv = mv.totalMarketValue
>         val pendingInvestment = mv.pendingInvestmentAmountTotal.getOrElse(BigDecimal(0))
>         assumedMv + pendingInvestment
>       }
>     }
> 
>     // Use planMvs as weighted among the plans
>     // If no MV, assume all plans have same weight
>     val planWeights = if (planMvs.values.sum == 0) {
>       planMvs.mapValues(_ => BigDecimal(1))
>     } else {
>       planMvs
>     }
> 
>     val aggregatedInstrumentWeights = planInstrumentTargetsMap
>       .toSeq
>       .flatMap { case (planId, taa) =>
>         taa.mapValues(_ * planWeights(planId))
>       }
>       .groupBy { case (instrument, _) => instrument }
>       .map { case (instrument, targetMvsOfInstrument) =>
>         instrument -> targetMvsOfInstrument.map(_._2).sum
>       }
>     
>     Calculator.weightedRatios(aggregatedInstrumentWeights)
>   }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2253 · comment 411340511 · PR 6389 · 2023-07-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/AdHocTaaHelpers.scala`

**Explicit source context (hunk):**

> +
> +    val aggregatedInstrumentWeights = planInstrumentTargetsMap
> +      .toSeq
> +      .flatMap { case (planId, taa) =>
> +        taa.mapValues(_ * planWeights.getOrElse(planId, 0))
> +      }
> +      .groupBy { case (instrument, _) => instrument }

## A3-0430 — BaseServiceLogicImpl.scala: A bit redundant to check this as `resolveNewTaasFromProvidedParam` requires the planIds set to match

**Source stance:** observed-defect

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; PR: Feat/INV-1600/productline cash smart goal create and modify

**Source-preserving request, proposal, or question:**

> A bit redundant to check this as `resolveNewTaasFromProvidedParam` requires the planIds set to match

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2260 · comment 405845554 · PR 6115 · 2023-06-23

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2260 · comment 405845554 · PR 6115 · 2023-06-23

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +        throw NotFound(s"Goal [${request.goalId}] does not have any plans!")
> +      }
> +
> +      newTaas <- resolveNewTaasFromProvidedParam(plans, request.planTaaMap)
> +      _ <- {
> +        //block if only sell only instrument
> +        val newInstrumentIds = newTaas.getOrElse(Seq.empty).flatMap {

## A3-0435 — RebalanceRequestJdbcRepositoryImpl.scala: ``` filterOpt(planId)(_.planId === _) ``` Does this work?

**Source stance:** open-question

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala; PR: Feat/INV-1663 migrate to readside rebalance

**Source-preserving request, proposal, or question:**

> ```
> filterOpt(planId)(_.planId === _)
> ```
> 
> Does this work?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2265 · comment 412992702 · PR 6482 · 2023-07-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala`

**Evidence:** anon-2.jsonl:2265 · comment 412992702 · PR 6482 · 2023-07-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala`

**Explicit source context (hunk):**

> +            v.assetAllocationToUse.asColumnOf[JsValue].+>>("effectiveDate").asColumnOf[LocalDate] === target)
> +          .sortBy(_.createdAt)
> +          .result
> +      }
> +      .map(_.toList)
> +  }
> +

## A3-0455 — WithdrawalTopicSubscriber.scala: Also, query by planId if exists would give fewer results, so let’s match that first

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriber.scala; PR: [INV-1425] feat(report): Added tax details to instrumentTransactionDto and refactor accessFeeTax statement calculation

**Source-preserving request, proposal, or question:**

> Also, query by planId if exists would give fewer results, so let’s match that first

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2288 · comment 407989870 · PR 6309 · 2023-07-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriber.scala`

## A3-0490 — RebalanceMsgLogicImpl.scala: just add another method similar to `calculateRequestedAmount` ``` def calculateSettledAmount(orders: List[OrderV2]): BigDecimal = { val orderAmounts =

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala; PR: Resolve INV-1745: Rebalance transaction to show netted sell orders if rebalance completed without buy orders.

**Source-preserving request, proposal, or question:**

> Maybe just add another method similar to `calculateRequestedAmount`
> 
> ```
>   def calculateSettledAmount(orders: List[OrderV2]): BigDecimal = {
>     val orderAmounts = orders.collect {
>       case so: SettledOrder => so.requestedAmount
>     }
>     orderAmounts.foldLeft(BigDecimal(0))((a, b) => a + b))
>   }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2326 · comment 407562901 · PR 6322 · 2023-06-30

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala`

> Maybe just add another method similar to `calculateRequestedAmount`
> 
> ```
>   def calculateSettledAmount(orders: List[OrderV2]): BigDecimal = {
>     val orderAmounts = orders.collect {
>       case so: SettledOrder => so.requestedAmount
>     }
>     orderAmounts.foldLeft(BigDecimal(0))((a, b) => a + b))
>   }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2326 · comment 407562901 · PR 6322 · 2023-06-30

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala`

**Explicit source context (hunk):**

> orderAmounts.foldLeft(BigDecimal(0))((a, r) => a + r.getOrElse(BigDecimal(0)))
>    }
> +
> +  private def calculateSettledAmount(orders: List[OrderV2]): BigDecimal = {
> +    val orderAmounts = orders.collect {
> +      case settledOrder: SettledOrder => settledOrder.settledAmount
> +    }

## A3-0492 — RebalanceMsgLogicImpl.scala: change for all the places that cast `SettledOrder` ?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala; PR: Resolve INV-1745: Rebalance transaction to show netted sell orders if rebalance completed without buy orders.

**Source-preserving request, proposal, or question:**

> Let’s change for all the places that cast `SettledOrder` ?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2328 · comment 407981213 · PR 6322 · 2023-07-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala`

**Evidence:** anon-2.jsonl:2328 · comment 407981213 · PR 6322 · 2023-07-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala`

**Explicit source context (hunk):**

> // Logging to sentry so we can detect if it actually ever happens else we can get rid of this.
>        // TODO: convert to warn log or remove log once have more information on this case
> -      logger.error(s"Received RebalanceRequestDeletedMsg but marking transactionID (${msg.rebalanceRequest.rebalanceRequestId}) as confirmed as it has confirmed sell orders")
> +      logger.error(
> +        s"Received RebalanceRequestDeletedMsg but marking transactionID (${msg.rebalanceRequest.rebalanceRequestId}) as confirmed as it has confirmed sell orders"
> +      )
>        val sellOrders = getOrders(msg.rebalanceRequest.sellOrders)

## A3-0494 — RebalanceMsgLogicImpl.scala: collect = filter \+ map… here we don’t care about PendingOrder, so we can simply drop it

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala; PR: Resolve INV-1745: Rebalance transaction to show netted sell orders if rebalance completed without buy orders.

**Source-preserving request, proposal, or question:**

> collect = filter \+ map… here we don’t care about PendingOrder, so we can simply drop it

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2330 · comment 408307656 · PR 6322 · 2023-07-04

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala`

**Evidence:** anon-2.jsonl:2330 · comment 408307656 · PR 6322 · 2023-07-04

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala`

**Explicit source context (hunk):**

> +
> +  private def calculateSettledAmount(orders: List[OrderV2]): BigDecimal = {
> +    val orderAmounts = orders.collect {
> +      case settledOrder: SettledOrder => settledOrder.settledAmount
> +    }
> +    orderAmounts.foldLeft(BigDecimal(0))((a, b) => a + b)
> +  }

## A3-0556 — CustomerPIMatcher.scala: change this method a bit: ``` def getPIInstrumentsForNonPI(customerId: UUID, instruments: Seq[InstrumentProfile]): Future[Set[String]] ``` Makes the c

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/pi/CustomerPIMatcher.scala; PR: Feat/INV-1551 be advisory modify fundsmart

**Source-preserving request, proposal, or question:**

> Let’s change this method a bit:
> 
> ```
> def getPIInstrumentsForNonPI(customerId: UUID, instruments: Seq[InstrumentProfile]): Future[Set[String]]
> ```
> 
>   
> Makes the caller’s usage a bit cleaner

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2401 · comment 402471542 · PR 6165 · 2023-06-12

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/pi/CustomerPIMatcher.scala`

## A3-0557 — PortfolioSuitabilityAnalysisLogic.scala: How about we create a local scaffiene cache for instrument performance in this method \(i.e. invalidate all after we are done with all the `instrument

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala; PR: Feat/INV-1551 be advisory modify fundsmart

**Source-preserving request, proposal, or question:**

> How about we create a local scaffiene cache for instrument performance in this method \(i.e. invalidate all after we are done with all the `instrumentWeights`\)
> 
> The lookup count is same, but maybe code is cleaner?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2402 · comment 402475537 · PR 6165 · 2023-06-12

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala`

## A3-0569 — CustomerAltsFeesCalculator.scala: change these 2 methods to accept `PlanProfile` / `PlanChargeContext` ``` isRelevantPlan(planProfile: PlanProfile): Boolean isRelevantPlan(planChargeCo

**Source stance:** requested-change

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerAltsFeesCalculator.scala; PR: Resolve INV-1298: Charge different fees for quant edge

**Source-preserving request, proposal, or question:**

> Let’s change these 2 methods to accept `PlanProfile` / `PlanChargeContext`
> 
> ```
> isRelevantPlan(planProfile: PlanProfile): Boolean
> isRelevantPlan(planChargeContext: PlanChargeContext): Boolean
> ```
> 
> The caller can handle the collection bits themselves

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2416 · comment 400696144 · PR 6038 · 2023-06-06

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerAltsFeesCalculator.scala`

**Evidence:** anon-2.jsonl:2416 · comment 400696144 · PR 6038 · 2023-06-06

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerAltsFeesCalculator.scala`

**Explicit source context (hunk):**

> -    allPlanChargeContext.filter {
> -      case (_, fundsmart: FundSmartPlanChargeContext) =>
> -        fundsmart.isAlternative.contains(true)
> +  override def isRelevantPlan(planProfile: PlanProfile): Boolean =
> +    planProfile.productLineAndIntent.exists {
> +      case FundSmartProductDto(_, _, _, _, _, isAlternativeInvestment) =>
> +        isAlternativeInvestment.contains(true)

## A3-0601 — ServiceLogicImpl.scala: Can we extract some var here, and also reformat this code block… idk what’s going with all these wonky indentation \+ brackets here…

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [INV-1643] fix(transaction): Extract from tuple for safety

**Source-preserving request, proposal, or question:**

> Can we extract some var here, and also reformat this code block… idk what’s going with all these wonky indentation \+ brackets here…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2448 · comment 400273603 · PR 6119 · 2023-06-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2448 · comment 400273603 · PR 6119 · 2023-06-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +        val totalChargeAmount = transaction.settledAmount
> +          .orElse(transaction.assumedAmount)
> +          .getOrElse(transaction.requestedAmount.get)
> +        val amountChargedBySell = feeChargeDetails
> +          .amountChargedBySell
> +          .getOrElse(BigDecimal(0))
> +        val amountChargedByCash = totalChargeAmount - amountChargedBySell

## A3-0611 — CustomerFeeEstimator.scala: we can pattern match to avoid calling Option.get ``` (maybeYear, maybeQuarter) match { case (Some(year), Some(quarter)) => Some(...) case _ => None } 

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerFeeEstimator.scala; PR: Resolve INV-1570: Update estimate fee endpoint for user specified duration based estimation.

**Source-preserving request, proposal, or question:**

> Nit: we can pattern match to avoid calling Option.get
> 
> ```
> (maybeYear, maybeQuarter) match {
>   case (Some(year), Some(quarter)) => Some(...)
>   case _ => None
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2460 · comment 397098138 · PR 5980 · 2023-05-24

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerFeeEstimator.scala`

> Nit: we can pattern match to avoid calling Option.get
> 
> ```
> (maybeYear, maybeQuarter) match {
>   case (Some(year), Some(quarter)) => Some(...)
>   case _ => None
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2460 · comment 397098138 · PR 5980 · 2023-05-24

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerFeeEstimator.scala`

**Explicit source context (hunk):**

> +
> +  object CustomerFeeEstimationPeriod {
> +
> +    def from(maybeYear: Option[Int], maybeQuarter: Option[String]): Option[CustomerFeeEstimationPeriod] = {
> +      (maybeYear, maybeQuarter) match {
> +        case (Some(year), Some(quarter)) =>
> +          val (startDate, endDate) = ChargeUtil.parseQuarter(year, Quarter.withName(quarter))

## A3-0687 — TransactionFxConverter.scala: Not good hide var like this \(e.g `maybeConvertedSettlementDetail` was a fut, and then reassigned as an Option How about just ``` maybeConvertedSettle

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala; PR: [INV-1437] feat(transaction): Models

**Source-preserving request, proposal, or question:**

> Not good hide var like this \(e.g `maybeConvertedSettlementDetail` was a fut, and then reassigned as an Option
> 
> How about just
> 
> ```
> maybeConvertedSettlementDetail <- transaction.assetTransferDetails.flatMap(_.settledAssetTransferDetail) match {
>   case Some(value) => convertSettlementDetail(value).map(Some(_))
>   case None => Future.successful(None)
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2538 · comment 391031530 · PR 5770 · 2023-05-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

> Not good hide var like this \(e.g `maybeConvertedSettlementDetail` was a fut, and then reassigned as an Option
> 
> How about just
> 
> ```
> maybeConvertedSettlementDetail <- transaction.assetTransferDetails.flatMap(_.settledAssetTransferDetail) match {
>   case Some(value) => convertSettlementDetail(value).map(Some(_))
>   case None => Future.successful(None)
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2538 · comment 391031530 · PR 5770 · 2023-05-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Explicit source context (hunk):**

> +        ccy = targetCcy,
> +        amount = maybeConvertedSettlementDetail.flatMap(_.displayTransferDateAmount),
> +        originalAmount = maybeConvertedSettlementDetail.map(_.transferDateAmount),
> +        assetTransferDetails = transaction.assetTransferDetails.map(
> +          assetTransferDetails => assetTransferDetails.copy(
> +            settledAssetTransferDetail = maybeConvertedSettlementDetail
> +          )

## A3-0697 — package.scala: Both are already Option, so no we don’t need

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/models/package.scala; PR: Feat/INV-1447/sync with latest performance

**Source-preserving request, proposal, or question:**

> Both are already Option, so no we don’t need

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2548 · comment 387899476 · PR 5777 · 2023-04-19

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/models/package.scala`

**Evidence:** anon-2.jsonl:2548 · comment 387899476 · PR 5777 · 2023-04-19

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/models/package.scala`

**Explicit source context (hunk):**

> vol = s.monthlyReturnsVol,
>        sharpeRatio = s.sharpeRatio,
> +      monthlyReturnStart = s.monthlyReturnStart,
> +      monthlyReturnEnd = s.monthlyReturnEnd,
>        oneYearRollingStats = RollingStats.toDto(s.oneYearRollingStats),
>        fiveYearRollingStats = RollingStats.toDto(s.fiveYearRollingStats),
>        tenYearRollingStats = RollingStats.toDto(s.tenYearRollingStats),

## A3-0702 — PortfolioVersionUpgradeRebalanceRequestsGenerator.scala: Good point. Added the runFold back

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala; PR: feat(rebalance): RPC improvements

**Source-preserving request, proposal, or question:**

> Good point. Added the runFold back

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2553 · comment 388288323 · PR 5776 · 2023-04-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala`

**Evidence:** anon-2.jsonl:2553 · comment 388288323 · PR 5776 · 2023-04-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala`

**Explicit source context (hunk):**

> -                  skippedCountForExistentRequest,
> -                  failedCount
> -                  ) if result.proceed =>
> +        .runFold((0L, 0L, Map.empty[SkippedReason, Long])) {
> +          case ((totalCount, successfulCount, skippedReasonBreakdown), result) =>
> +            result match {
> +              case Left(skippedReason) =>

## A3-0705 — PreRpcValidation.scala: Ah yeah I just need to sort based on something so that the ordering is same when I run multiple times

**Source stance:** explanation

**Context:**

> amend-scripts/src/main/scala/rebalance/PreRpcValidation.scala; PR: [INV-1432] feat(amend-scripts): Pre-RPC data consistency validation

**Concern stated in the source:** Ah yeah I just need to sort based on something so that the ordering is same when I run multiple times

**Source-preserving request, proposal, or question:**

> Ah yeah I just need to sort based on something so that the ordering is same when I run multiple times

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2556 · comment 387563324 · PR 5762 · 2023-04-18

Source path: `amend-scripts/src/main/scala/rebalance/PreRpcValidation.scala`

**Evidence:** anon-2.jsonl:2556 · comment 387563324 · PR 5762 · 2023-04-18

Source path: `amend-scripts/src/main/scala/rebalance/PreRpcValidation.scala`

**Explicit source context (hunk):**

> +        )
> +        .filter(i => i.effectiveDate.isBefore(portfolioInfo.latestEffectiveDate))
> +        .toList
> +        .sortBy(_.effectiveDate.toString)
> +      _ = logger.info(s"Found ${portfolioVersionInfos.size} previous version of $portfolioInfo")
> +    } yield portfolioVersionInfos
> +  }

## A3-0712 — PlanTimeseriesTopicSubscriber.scala: How about ``` _ <- maybeLatestStoredMV match { case Some(latestStoredMV) if latestStoredMV.updatedAt.isAfter(msg.updatedAt) => logger.info("Skipping..

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala; PR: Feat/INV-1151 rebalance entity refactor phase 2 projections

**Source-preserving request, proposal, or question:**

> How about
> 
> ```
> _ <- maybeLatestStoredMV match {
>   case Some(latestStoredMV) if latestStoredMV.updatedAt.isAfter(msg.updatedAt) =>
>     logger.info("Skipping.....")
>     Future.successful(Done)
>   case _ =>
>     // upsert
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2564 · comment 382583244 · PR 5603 · 2023-03-30

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

> How about
> 
> ```
> _ <- maybeLatestStoredMV match {
>   case Some(latestStoredMV) if latestStoredMV.updatedAt.isAfter(msg.updatedAt) =>
>     logger.info("Skipping.....")
>     Future.successful(Done)
>   case _ =>
>     // upsert
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2564 · comment 382583244 · PR 5603 · 2023-03-30

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> +        ) {
> +          for {
> +            rebalancePlan <- logger.logTime(s"Loading rebalance plan entity for planId ${msg.planId}") {
> +              refProvider.getPlanRebalancerEntityRef(msg.planId).ask(GetRebalancePlanCmd(_))
> +            }
> +            _ <- if (rebalancePlan.isEmpty) {
> +              logger.error(s"${UpdateMarketValueCmd.getClass.getName} is skipped for planId [${msg.planId}] because rebalancePlan is empty")

## A3-0720 — PlanTimeseriesTopicSubscriber.scala: just keep the old check in the patten matching above. Then the method isValid below doesn’t need that check anymore, and purely checking the MV data

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala; PR: Feat/INV-1151 rebalance entity refactor phase 2 projections

**Source-preserving request, proposal, or question:**

> Maybe just keep the old check in the patten matching above. Then the method isValid below doesn’t need that check anymore, and purely checking the MV data

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2572 · comment 385713658 · PR 5603 · 2023-04-11

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2572 · comment 385713658 · PR 5603 · 2023-04-11

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> -        } yield Done
> +    case msg: LatestPlanMarketValueUpdatedMsg if PlanTimeseriesTopicSubscriber.isNotOldMsg(dateTimeProvider, msg) =>
> +      upsertToProjection(msg)
> +
> +      //TODO @

**Evidence:** anon-2.jsonl:2572 · comment 385713658 · PR 5603 · 2023-04-11

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> : Legacy, will be refactored in phase 3
> +      if (PlanTimeseriesTopicSubscriber.isValidLatestPlanMarketValueUpdatedMsg(dateTimeProvider, msg)) {
> +        logger.logTime(

## A3-0723 — AssumeTransactionSettlementCmdHandler.scala: that amount vs unit check might be specific to rebalance sell order. Based on new logic, this condition `areAllOrdersUnAssumedRebalanceSell` should re

**Source stance:** suggestion

**Context:**

> broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/handlers/AssumeTransactionSettlementCmdHandler.scala; PR: [TT-1943] feat(broker): removed filtering rebalance order

**Concern stated in the source:** Nevertheless, I suggest this removal because I find the logging now misleading

**Source-preserving request, proposal, or question:**

> I think that amount vs unit check might be specific to rebalance sell order. Based on new logic, this condition `areAllOrdersUnAssumedRebalanceSell` should return false always if `validOrders.isEmpty`?
> 
> Nevertheless, I suggest this removal because I find the logging now misleading
> 
> ```
> handleAssumeTransactionSettlementCmd has are all un-assumed rebalance sell, which does not need to be assumed
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2575 · comment 384588596 · PR 5666 · 2023-04-05

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/handlers/AssumeTransactionSettlementCmdHandler.scala`

> I think that amount vs unit check might be specific to rebalance sell order. Based on new logic, this condition `areAllOrdersUnAssumedRebalanceSell` should return false always if `validOrders.isEmpty`?
> 
> Nevertheless, I suggest this removal because I find the logging now misleading
> 
> ```
> handleAssumeTransactionSettlementCmd has are all un-assumed rebalance sell, which does not need to be assumed
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2575 · comment 384588596 · PR 5666 · 2023-04-05

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/handlers/AssumeTransactionSettlementCmdHandler.scala`

**Explicit source context (hunk):**

> +      logger.warn(
> +        s"[$entityId] handleAssumeTransactionSettlementCmd got empty SettlementAssumption because all orders for instrumentId(${orderGroup.instrumentId}) is not valid. orderGroup is ${Json.toJson(orderGroup).toString()} "
> +      )
>        ctx.reply(Done)
>        return ctx.done
>      }

## A3-0758 — Transaction FX conversion Futures: bounded Source.mapAsync2 proposed

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> I’m a little skeptical with spawning all the futures at once here. We would be capped by the number of cores anyway. Maybe the usual Source\(transactions\).mapAsync\(2\) \{….\} ?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2610 · comment 370756717 · PR 5266 · 2023-02-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Evidence:** anon-2.jsonl:2610 · comment 370756717 · PR 5266 · 2023-02-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Explicit source context (hunk):**

> +        .runWith(Sink.seq)
> +        .map(_.toList)
>      }
>    }
>  
> -  private def fetchFxRatesAndRefreshCache(baseCcy: CurrencyUnit, quoteCcy: CurrencyUnit): Future[List[(LocalDate, BigDecimal)]] = {
> -    logger.info(s"fetchFxRatesAndRefreshCache started for [$baseCcy$quoteCcy]...")

## A3-0772 — TransactionFxConverter.scala: distinct the pairs before loading?

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> Let’s distinct the pairs before loading?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2626 · comment 377730008 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Evidence:** anon-2.jsonl:2626 · comment 377730008 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Explicit source context (hunk):**

> +    toCcy: CurrencyUnit
> +  ): Future[List[TransactionDto]] = {
> +    logger.logTime(s"fxConvertTransactions for ${transactions.size}") {
> +      Source(transactions)
> +        .mapAsync(2) { transaction =>
> +          transaction.transactionType match {
> +            case TransactionType.FX_CONVERSION => applyDisplayAmountForFxSettlementDetails(transaction, toCcy)

## A3-0774 — FxRateHelper.scala: ``` fxRateCache .getIfPresent(fxId) .map(Future.successful) .getOrElse(loadCacheAndFind(fxId)) ``` Try to use Option more idiomatically

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> ```
> fxRateCache
>   .getIfPresent(fxId)
>   .map(Future.successful)
>   .getOrElse(loadCacheAndFind(fxId))
> ```
> 
> Try to use Option more idiomatically

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2628 · comment 377730484 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Evidence:** anon-2.jsonl:2628 · comment 377730484 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +          NO_FX_RATES_AVAILABLE
> +        )))
> +    }
> +  }
> +
> +  private def loadFxRates(baseCcy: CurrencyUnit, quoteCcy: CurrencyUnit) = {
> +    logger.logTime(s"Loading fx rates for baseCcy [$baseCcy] to quoteCcy [$quoteCcy] from source") {

## A3-0776 — FxRateHelper.scala: create a TreeMap keyed by priceDate first, then just lookup here? Otherwise we traverse the Seq everytime

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Concern stated in the source:** Otherwise we traverse the Seq everytime

**Source-preserving request, proposal, or question:**

> Maybe create a TreeMap keyed by priceDate first, then just lookup here? Otherwise we traverse the Seq everytime

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2630 · comment 377731048 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Evidence:** anon-2.jsonl:2630 · comment 377731048 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +      _ = fxRateCache.synchronous.invalidateAll()
> +    } yield projectionData
> +  }
> +
> +}
> +
> +object FxRateHelper {

## A3-0787 — SgServiceLogicImpl.scala: If you want to log when we generate for all, then should check both `includeCustomers` and `excludeCustomers` to be empty

**Source stance:** requested-change

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/SgServiceLogicImpl.scala; PR: Feat/EN-870 sg auto generate report meta data

**Source-preserving request, proposal, or question:**

> If you want to log when we generate for all, then should check both `includeCustomers` and `excludeCustomers` to be empty

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2642 · comment 377383926 · PR 5350 · 2023-03-13

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/SgServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2642 · comment 377383926 · PR 5350 · 2023-03-13

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> validateMonthlyStatementsRequest(request, "createMonthlyStatementsV2")
>      val yearMonth = request.yearMonth
> +    if (request.includeCustomers.isEmpty && request.excludeCustomers.isEmpty) {
> +      slackNotificationSender.sendSlackMessage(
> +        msg = s"Started generating MonthlyStatements, yearMonth [$yearMonth] in SG, requested by [${request.requestedBy}]",
> +        level = SlackNotificationColorEnum.GOOD

## A3-0795 — SftpRunner.scala: This can be `val` now

**Source stance:** requested-change

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/sftp/SftpRunner.scala; PR: Feat/EN-870 sg auto generate report meta data

**Source-preserving request, proposal, or question:**

> This can be `val` now

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2650 · comment 379033841 · PR 5350 · 2023-03-17

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/sftp/SftpRunner.scala`

**Evidence:** anon-2.jsonl:2650 · comment 379033841 · PR 5350 · 2023-03-17

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/sftp/SftpRunner.scala`

**Explicit source context (hunk):**

> -      case ex: Exception => throw SftpRunnerException("Failed to retrieve ChannelSftp from pool, hence cannot execute " + task, ex)
> -    }
> +  def execute[T](task: SftpTask[T]): T = {
> +    val channelSftp = getChannel
>  
>      try {
>        task.run(channelSftp)

## A3-0796 — SftpRunner.scala: No need to assign to var `channelSftp` anymore. Can just return

**Source stance:** requested-change

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/sftp/SftpRunner.scala; PR: Feat/EN-870 sg auto generate report meta data

**Source-preserving request, proposal, or question:**

> No need to assign to var `channelSftp` anymore. Can just return

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2651 · comment 379033930 · PR 5350 · 2023-03-17

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/sftp/SftpRunner.scala`

**Evidence:** anon-2.jsonl:2651 · comment 379033930 · PR 5350 · 2023-03-17

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/sftp/SftpRunner.scala`

**Explicit source context (hunk):**

> +  // This should always be private, and shall only exposed to runner itself
> +  private def getChannel: ChannelSftp = {
> +    try {
> +      pool.borrowObject()
> +    } catch {
> +      case ex: Exception => throw SftpRunnerException("Failed to retrieve ChannelSftp from pool", ex)
> +    }

## A3-0809 — AdvisedPortfolioOfferingsManager.scala: Hmm I don’t want this logic to be aware that flagship portfolios are available in Cash/CPF/SRS. Can we find allowed trading accounts by using superset

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala; PR: [INV-1116] feat(advisory, invest.20): Recommended core portfolios

**Source-preserving request, proposal, or question:**

> Hmm I don’t want this logic to be aware that flagship portfolios are available in Cash/CPF/SRS. Can we find allowed trading accounts by using superset of all flagshipOfferings' `tradingAccountTypes`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2664 · comment 372614983 · PR 5295 · 2023-02-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala`

**Evidence:** anon-2.jsonl:2664 · comment 372614983 · PR 5295 · 2023-02-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala`

**Explicit source context (hunk):**

> EsgPortfolioOfferingResponse(
>            portfolioId = productPortfolio.portfolioId,
>            shortName = productPortfolio.shortName.getOrElse(""),
>            summary = metaData.summary,
>            description = metaData.description.getOrElse(productPortfolio.description),
> -          riskTarget = ModelPortfolioRiskTarget.calculateRiskTargetFromStockRatio(productPortfolio.stockProportion),
> +          riskTarget = riskTarget,

## A3-0810 — MaaPageLoaderV2.scala: We handled the performance fetch error in advisory, so it’s possible to have empty performance here. `offering.performance.get` is not safe. We don’t 

**Source stance:** observed-defect

**Context:**

> gateway-impl/src/main/scala/com/endowus/silver/gateway/impl/managers/bffs/MaaPageLoaderV2.scala; PR: [INV-1116] feat(advisory, invest.20): Recommended core portfolios

**Concern stated in the source:** `offering.performance.get` is not safe.

**Source-preserving request, proposal, or question:**

> We handled the performance fetch error in advisory, so it’s possible to have empty performance here. `offering.performance.get` is not safe.
> 
> We don’t need to constrict the map again here. We can just use `val maybePerformance = offering.performance` in the block below

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2665 · comment 373499791 · PR 5295 · 2023-02-28

Source path: `gateway-impl/src/main/scala/com/endowus/silver/gateway/impl/managers/bffs/MaaPageLoaderV2.scala`

## A3-0813 — InvestmentCommunicationV2EventProcessor.scala: No need to extract `instruments` here right? We can just traverse and map from sorted allocationTargets directly in L155?

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala; PR: [EN-761] feat(investment)(communication) migrate cpf srs investement in progress email v2

**Source-preserving request, proposal, or question:**

> No need to extract `instruments` here right? We can just traverse and map from sorted allocationTargets directly in L155?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2668 · comment 377738257 · PR 5484 · 2023-03-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2668 · comment 377738257 · PR 5484 · 2023-03-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +      for {
> +        goal <- goalService.getGoalById(ele.event.goalId).invoke()
> +        plan = goal.plans.find(_.planId == event.planId).get
> +        portfolio <- portfolioService
> +          .getPortfolioById(
> +            portfolioId = plan.targetAssetAllocation.modelPortfolioId,
> +            effectiveDate = Some(plan.targetAssetAllocation.effectiveDate.toString)

## A3-0814 — InvestmentCommunicationV2EventProcessor.scala: Why find again here? Isn’t it exactly `allocationTargetDto` now?

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala; PR: [EN-761] feat(investment)(communication) migrate cpf srs investement in progress email v2

**Source-preserving request, proposal, or question:**

> Why find again here? Isn’t it exactly `allocationTargetDto` now?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2669 · comment 377842375 · PR 5484 · 2023-03-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2669 · comment 377842375 · PR 5484 · 2023-03-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +          )
> +          .invoke()
> +        portfolioTaaView = createTaaEmailView(event.tradingAccountType, portfolio)
> +        _ <- emailTopicProducerDirect
> +          .publish(
> +            EmailRequest(
> +              customerId = ele.event.customerId,

## A3-0824 — InvestmentPlanEventProcessor.scala: also `.map(_.isValid)` here?

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentPlanEventProcessor.scala; PR: Resolve INV-1135: Send email for failed recurring investments with state change info

**Source-preserving request, proposal, or question:**

> Let’s also `.map(_.isValid)` here?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2681 · comment 374499709 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentPlanEventProcessor.scala`

**Evidence:** anon-2.jsonl:2681 · comment 374499709 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentPlanEventProcessor.scala`

**Explicit source context (hunk):**

> complianceChecker
>            .validateRecurringInvestmentRequest(customerId, complianceCheckRequest)
> +          .map(_.isValid)
>            .flatMap {
>              case true =>
>                recurringInvestmentHelper

## A3-0844 — HkNotificationManager.scala: Does it work with just `case Some(tuple) => tuple`?

**Source stance:** open-question

**Context:**

> customer-impl/src/main/scala/com/endowus/silver/customer/impl/logic/HkNotificationManager.scala; PR: Feat/INV-898 pi passport expiring emails

**Source-preserving request, proposal, or question:**

> Does it work with just `case Some(tuple) => tuple`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2702 · comment 372644426 · PR 5354 · 2023-02-24

Source path: `customer-impl/src/main/scala/com/endowus/silver/customer/impl/logic/HkNotificationManager.scala`

**Evidence:** anon-2.jsonl:2702 · comment 372644426 · PR 5354 · 2023-02-24

Source path: `customer-impl/src/main/scala/com/endowus/silver/customer/impl/logic/HkNotificationManager.scala`

**Explicit source context (hunk):**

> +            Future.successful(None)
> +        }
> +      }}
> +      .collect {
> +        case Some(piDataWithCustomer) => piDataWithCustomer
> +      }
> +

## A3-0850 — NotificationManager.scala: Looks like you don’t need for-comprehend block here

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala; PR: Resolve INV-896: Changes to publish email/platform notifs for upcoming customer vc warnings.

**Source-preserving request, proposal, or question:**

> Looks like you don’t need for-comprehend block here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2708 · comment 372348662 · PR 5329 · 2023-02-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

**Evidence:** anon-2.jsonl:2708 · comment 372348662 · PR 5329 · 2023-02-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

**Explicit source context (hunk):**

> +          case NonVulnerableCustomerProfile(_, RiskProfileStatus.Valid, _, _) =>
> +            for {
> +              craSimulationResult <- simulateCraWithVcCutOffAge(customerData.customerId)
> +
> +              filteredData <- craSimulationResult match {
> +                case _: VulnerableCustomerProfile =>
> +                  Future.successful(Some(customerData))

## A3-0853 — NotificationManager.scala: Can we just return `Some(customerData)` ?

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala; PR: Resolve INV-896: Changes to publish email/platform notifs for upcoming customer vc warnings.

**Source-preserving request, proposal, or question:**

> Can we just return `Some(customerData)` ?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2711 · comment 372608367 · PR 5329 · 2023-02-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

**Evidence:** anon-2.jsonl:2711 · comment 372608367 · PR 5329 · 2023-02-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

**Explicit source context (hunk):**

> +      }}
> +      .collect {
> +        case Some(customerData) => customerData
> +      }
> +
> +    def sendUpcomingCustomerVCNotifications(data: CustomerProjectionData): Future[UUID] = {
> +      for {

## A3-0854 — NotificationManager.scala: Then you can `.collect { case Some(customerData) => customerData }` to flatten the flow

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala; PR: Resolve INV-896: Changes to publish email/platform notifs for upcoming customer vc warnings.

**Source-preserving request, proposal, or question:**

> Then you can `.collect { case Some(customerData) => customerData }` to flatten the flow

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2712 · comment 372608592 · PR 5329 · 2023-02-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

**Evidence:** anon-2.jsonl:2712 · comment 372608592 · PR 5329 · 2023-02-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

**Explicit source context (hunk):**

> +      }}
> +      .collect {
> +        case Some(customerData) => customerData
> +      }
> +
> +    def sendUpcomingCustomerVCNotifications(data: CustomerProjectionData): Future[UUID] = {
> +      for {

## A3-0903 — CraManager.scala: Can we extract filters like this to a named method so that it’s easier to follow?

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Concern stated in the source:** Can we extract filters like this to a named method so that it’s easier to follow?

**Source-preserving request, proposal, or question:**

> Can we extract filters like this to a named method so that it’s easier to follow?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2762 · comment 366322821 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:2762 · comment 366322821 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +          .getOrElse({
> +            logger.warn(s"Customer ID ${customer.customerId} profile is not available on read-side, read-side might be lagging")
> +            true
> +          })
> +      }
> +      .map(_._1)
> +      .zipWithIndex

## A3-0914 — CraManager.scala: forall returns true if Option is empty… so if somehow, profile is missing, we will always trigger? Should we use exists instead?

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> forall returns true if Option is empty… so if somehow, profile is missing, we will always trigger? Should we use exists instead?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- forall(empty)=true concern is later clarified by2774's intentional warn-and-force-include policy for missing readside profile; preserve both.
- Related source rows 2773, 2774: Initial exists-versus-forall question is followed by deliberate missing-profile warn-and-force-inclusion policy.

**Evidence:** anon-2.jsonl:2773 · comment 367132218 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:2773 · comment 367132218 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        bornUpTo = executeDate.minusYears(minCutoffAge)
> +      )
> +      .filter{ case (customer, maybeProfile) =>
> +        maybeProfile.map(isCustomerProfileDueForReassessment(customer.dateOfBirth, _))
> +          .getOrElse({
> +            logger.warn(s"Customer ID ${customer.customerId} profile is not available on read-side, read-side might be lagging")
> +            true

## A3-0915 — Missing profile readside: warn and force inclusion, while expired stays until retake

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Yep CRA Expired stays there until customer retakes.
> 
> Alright we can make this logic a little clearer to explain the rationale please? For example
> 
> ```scala
> def isCustomerProfileDueForVcReassessment(profile: CustomerAdvisoryProfileData): Boolean = {
>   val isValid = ...
>   val isNotUpdatedSinceDobThisYear = ...
>   isValid && isNotUpdatedSinceDobThisYear
> }
> 
> repository.find(...).filter { case (customer, maybeProfile) =>
>   maybeProfile.map(isCustomerProfileDueForVcReassessment)
>     .getOrElse {
>     log.warn(<warn message explaining the force inclusion since profile is missing from readside>)
>     true
>     }
> }.map(_._1)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 2773, 2774: Initial exists-versus-forall question is followed by deliberate missing-profile warn-and-force-inclusion policy.

**Evidence:** anon-2.jsonl:2774 · comment 367134361 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

> Yep CRA Expired stays there until customer retakes.
> 
> Alright we can make this logic a little clearer to explain the rationale please? For example
> 
> ```scala
> def isCustomerProfileDueForVcReassessment(profile: CustomerAdvisoryProfileData): Boolean = {
>   val isValid = ...
>   val isNotUpdatedSinceDobThisYear = ...
>   isValid && isNotUpdatedSinceDobThisYear
> }
> 
> repository.find(...).filter { case (customer, maybeProfile) =>
>   maybeProfile.map(isCustomerProfileDueForVcReassessment)
>     .getOrElse {
>     log.warn(<warn message explaining the force inclusion since profile is missing from readside>)
>     true
>     }
> }.map(_._1)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2774 · comment 367134361 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        bornUpTo = executeDate.minusYears(minCutoffAge)
> +      )
> +      .filter{ case (customer, maybeProfile) =>
> +        maybeProfile.map(isCustomerProfileDueForReassessment(customer.dateOfBirth, _))
> +          .getOrElse({
> +            logger.warn(s"Customer ID ${customer.customerId} profile is not available on read-side, read-side might be lagging")
> +            true

## A3-0947 — PassportValidatorHelper.scala: Wanna extract this `customer.officialIdentificationDto.fold`?

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/passport/PassportValidatorHelper.scala; PR: Feat/INV-895 simulate VC

**Source-preserving request, proposal, or question:**

> Wanna extract this `customer.officialIdentificationDto.fold`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2807 · comment 358802733 · PR 4858 · 2023-01-10

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/passport/PassportValidatorHelper.scala`

**Evidence:** anon-2.jsonl:2807 · comment 358802733 · PR 4858 · 2023-01-10

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/passport/PassportValidatorHelper.scala`

**Explicit source context (hunk):**

> +  def getCustomerPassport(customer: HkCustomerDto): Option[Passport] = {
> +    customer.officialIdentificationDto.map {
> +      case _: NationalIdentityCard =>
> +        logger.warn(s"Customer not using passport as ID information. customerId : ${customer.customerId}")
> +        None
> +      case x: Passport => Some(x)
> +    }.getOrElse{

## A3-0968 — ServiceLogicImpl.scala: the scala idiomatic way would be ```scala configDetails.exists(cd => cd.fundSmartCma || cd.fundSmartGwa) ```

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImpl.scala; PR: Resolve INV-679: Added endpoint to pull PRR data from new wealth.

**Source-preserving request, proposal, or question:**

> Nit: the scala idiomatic way would be
> 
> ```scala
> configDetails.exists(cd => cd.fundSmartCma || cd.fundSmartGwa)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2828 · comment 359153836 · PR 5058 · 2023-01-11

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImpl.scala`

> Nit: the scala idiomatic way would be
> 
> ```scala
> configDetails.exists(cd => cd.fundSmartCma || cd.fundSmartGwa)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2828 · comment 359153836 · PR 5058 · 2023-01-11

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +  override def pullDataFromNewWealth(request: NewWealthDataPullRequest): Future[Done] = {
> +
> +    def isFundSmartInstrument(configDetails: Option[ConfigDetails]) =
> +      configDetails.exists(it => it.fundSmartGwa || it.fundSmartCma)
> +
> +    val instrumentIds = request.instrumentIds
> +    val instrumentSourceFut = if (instrumentIds.isEmpty) {

## A3-0970 — NewWealthDataFetcher.scala: How about this? ```scala fundList.map(fundDetail => fundDetail.ISIN -> fundDetail).toMap ```

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/newwealth/NewWealthDataFetcher.scala; PR: Resolve INV-679: Added endpoint to pull PRR data from new wealth.

**Source-preserving request, proposal, or question:**

> How about this?
> 
> ```scala
> fundList.map(fundDetail => fundDetail.ISIN -> fundDetail).toMap
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2830 · comment 359155185 · PR 5058 · 2023-01-11

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/newwealth/NewWealthDataFetcher.scala`

> How about this?
> 
> ```scala
> fundList.map(fundDetail => fundDetail.ISIN -> fundDetail).toMap
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2830 · comment 359155185 · PR 5058 · 2023-01-11

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/newwealth/NewWealthDataFetcher.scala`

**Explicit source context (hunk):**

> +
> +  def getNewWealthInstruments(): Future[Map[String, NewWealthFundDetails]] = {
> +    callNewWealth().map { fundList =>
> +      logInstrumentsInfo(fundList)
> +      fundList.map(fundDetail => fundDetail.ISIN -> fundDetail).toMap
> +    }
> +  }

## A3-0972 — ServiceLogicImpl.scala: we don’t actually need this for comprehend block here if it’s just one future

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [EN-674] feat(transaction) create an api to get transactions for a customer id with goal id and statuses filter

**Source-preserving request, proposal, or question:**

> Nit: we don’t actually need this for comprehend block here if it’s just one future

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2832 · comment 357769261 · PR 5028 · 2023-01-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2832 · comment 357769261 · PR 5028 · 2023-01-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +    maybeTransactionStatuses: Option[Set[TransactionStatus]]
> +  ): Future[TransactionListDto] = {
> +    val filters = List(
> +      Some(Filter("customerId", Op.Eq, customerId.toString)),
> +      mayBeGoalId.map(goalId => Filter("goalId", Op.Eq, goalId.toString)),
> +      maybeTransactionStatuses.map(transactionStatuses => Filter("status", Op.In, Json.toJson(transactionStatuses).toString))
> +    ).flatten

## A3-0987 — InvestmentCommunicationV2EventProcessor.scala: at this point, we already know assumedAt is defined… so this fallback logic is redundant and potentially confusing? same for the below confirmed metho

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala; PR: EN-120 Handle Investment Completed and Upcoming Recurring Investment emails using Comms V2

**Source-preserving request, proposal, or question:**

> nit: at this point, we already know assumedAt is defined… so this fallback logic is redundant and potentially confusing? same for the below confirmed method

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2847 · comment 355225779 · PR 4890 · 2022-12-21

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2847 · comment 355225779 · PR 4890 · 2022-12-21

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +          new EmailRequest(
> +            customerId = ele.event.customerId,
> +            communicationId = getInvestmentCompletedCommunicationId(planId = ele.event.planId, request = ele.event.request, localConfig.getSilverRegion),
> +            requestedAt = ele.event.request.assumedAt.get.toInstant,
> +            providerData = SendgridData(
> +              localeToTemplateId = Map(
> +                Locale.EN_HK -> "

**Evidence:** anon-2.jsonl:2847 · comment 355225779 · PR 4890 · 2022-12-21

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> ",

## A3-0990 — StatementDataGenerator.scala: What if `settledOrders` is now empty? Should we follow the logic in else clause which uses `transaction.settledDate`?

**Source stance:** open-question

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala; PR: [EN-647] feat(report): do not throw exp for order with no settlement date

**Source-preserving request, proposal, or question:**

> What if `settledOrders` is now empty? Should we follow the logic in else clause which uses `transaction.settledDate`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2850 · comment 354944213 · PR 4950 · 2022-12-20

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

> What if `settledOrders` is now empty? Should we follow the logic in else clause which uses `transaction.settledDate`?
> 
> ‌

**Evidence:** anon-2.jsonl:2850 · comment 354944213 · PR 4950 · 2022-12-20

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Explicit source context (hunk):**

> +              s"Customer ${transaction.customerId}'s transaction ${transaction.transactionId} is SETTLEMENT_CONFIRMED, but the order ${o.orderId}'s confirmedDate is empty!!"
>            )
>          )
> +
> +        if (settledOrders.isEmpty) {
> +          List(transaction.settledDate.getOrElse(TimeUtils.instantToLocalDate(instant = transaction.statusUpdatedDate, timeZoneId = dateTimeProvider.zoneId)))
> +        } else {

## A3-1011 — NewWealthDataUploader.scala: Not sure if we still need to group here

**Source stance:** open-question

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/newwealth/NewWealthDataUploader.scala; PR: New wealth script

**Source-preserving request, proposal, or question:**

> Not sure if we still need to group here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source row2873 sets this grouping question aside as a minor point (Nvm minor thing). It remains historical context, not an outstanding requested grouping change.

**Evidence:** anon-2.jsonl:2872 · comment 353851063 · PR 4893 · 2022-12-15

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/newwealth/NewWealthDataUploader.scala`

**Evidence:** anon-2.jsonl:2872 · comment 353851063 · PR 4893 · 2022-12-15

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/newwealth/NewWealthDataUploader.scala`

**Explicit source context (hunk):**

> +      implicit val b: Bearer = bearer
> +      (for {
> +        _ <- source
> +          .groupedWithin(n = batchSize, d = 1000.millis)
> +          .map(_.toList)
> +          .mapAsync(2) { instruments =>
> +            for {

**Evidence:** anon-2.jsonl:2873 · comment 353851252 · PR 4893 · 2022-12-15

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/newwealth/NewWealthDataUploader.scala`

> Nvm minor thing..

## A3-1027 — RedeemOnceEdgeLogic.scala: We can remove this match now

**Source stance:** requested-change

**Context:**

> redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/edge/RedeemOnceEdgeLogic.scala; PR: EN-569 Calculate units from amount for redemption request

**Source-preserving request, proposal, or question:**

> We can remove this match now

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2891 · comment 351322182 · PR 4851 · 2022-12-06

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/edge/RedeemOnceEdgeLogic.scala`

**Evidence:** anon-2.jsonl:2891 · comment 351322182 · PR 4851 · 2022-12-06

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/edge/RedeemOnceEdgeLogic.scala`

**Explicit source context (hunk):**

> plan <- goalService.findPlan(request.planId).invoke()
>        goal <- getGoal(request.customerId, plan.goalId)
>  
> -      _ <- request.requestedAmount match {
> -        case _ if request.isFullRedemption => checkNoAmountBasedRedemptionPending(request.customerId, plan.planId)
> -        case Some(requestedAmount)         => checkBelowThresholdIfAmountBasedRedemptionPending(request.customerId, plan.planCcy, plan, goal, requestedAmount)
> -        case _                             => Future.unit
> -      }
> +      _ <- if (request.isFullRedemption) checkNoAmountBasedRedemptionPending(request.customerId, plan.planId)
> +      else checkBelowThresholdIfAmountBasedRedemptionPending(request.customerId,

## A3-1044 — ServiceLogicImpl.scala: can write this as below? ``` _.tags .flatMap(allPossibleTagsMap.get) .flatMap(tag => getDisplaySectionOrdering(tag.section).map((tag.label, _))) .toLi

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImpl.scala; PR: Feat/INV-840 plan upsert confirmation

**Source-preserving request, proposal, or question:**

> Maybe can write this as below?
> 
> ```
> _.tags
>   .flatMap(allPossibleTagsMap.get)
>   .flatMap(tag => getDisplaySectionOrdering(tag.section).map((tag.label, _)))
>   .toList
>   .sortBy { case (_, displayOrder) => displayOrder }
>   .map { case (tagLabel, _) => tagLabel }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2908 · comment 349047396 · PR 4779 · 2022-11-28

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImpl.scala`

> Maybe can write this as below?
> 
> ```
> _.tags
>   .flatMap(allPossibleTagsMap.get)
>   .flatMap(tag => getDisplaySectionOrdering(tag.section).map((tag.label, _)))
>   .toList
>   .sortBy { case (_, displayOrder) => displayOrder }
>   .map { case (tagLabel, _) => tagLabel }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2908 · comment 349047396 · PR 4779 · 2022-11-28

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      instrument.configDetails
> +        .map(
> +          _.tags
> +            .flatMap(allPossibleTagsMap.get)
> +            .flatMap(tag => getDisplaySectionOrdering(tag.section).map((tag.label, _)))
> +            .toList
> +            .sortBy { case (_, displayOrder) => displayOrder }

## A3-1052 — TransactionEntity.scala: maybe easier to read if we match this first? ``` case t: InvestmentTransaction if transaction.statusDetails.transactionStatus == TransactionStatus.CRE

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionEntity.scala; PR: INV-869 fix(transaction): add requestedAmount to cancelling and cancel status

**Source-preserving request, proposal, or question:**

> Nit: maybe easier to read if we match this first?
> 
> ```
> case t: InvestmentTransaction if transaction.statusDetails.transactionStatus == TransactionStatus.CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2916 · comment 350434123 · PR 4824 · 2022-12-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionEntity.scala`

> Nit: maybe easier to read if we match this first?
> 
> ```
> case t: InvestmentTransaction if transaction.statusDetails.transactionStatus == TransactionStatus.CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2916 · comment 350434123 · PR 4824 · 2022-12-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionEntity.scala`

**Explicit source context (hunk):**

> +      case t: InvestmentTransaction if transaction.statusDetails.transactionStatus == TransactionStatus.CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION =>
> +        t.statusDetails match {
> +          case sd: RequestedAmountStatusDetails =>
> +            val updatedTransaction = t.copy(
> +              statusDetails = CancellingStatusDetails(
> +                requestedAmount = sd.requestedAmount,
> +                cancellingAt = dateTimeProvider.now,

## A3-1059 — CustomerAdvisoryProfileTopicSubscriber.scala: You can use Option#fold or Option#getOrElse. But yeah, most of methods in Option are following that pattern `if isEmpty foo else bar`

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/CustomerAdvisoryProfileTopicSubscriber.scala; PR: Feat/INV-736 remove acks state change

**Source-preserving request, proposal, or question:**

> Nit: You can use Option#fold or Option#getOrElse. But yeah, most of methods in Option are following that pattern `if isEmpty foo else bar`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2924 · comment 348729601 · PR 4770 · 2022-11-25

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/CustomerAdvisoryProfileTopicSubscriber.scala`

> Nit: You can use Option#fold or Option#getOrElse. But yeah, most of methods in Option are following that pattern `if isEmpty foo else bar`
> 
> ‌

**Evidence:** anon-2.jsonl:2924 · comment 348729601 · PR 4770 · 2022-11-25

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/CustomerAdvisoryProfileTopicSubscriber.scala`

**Explicit source context (hunk):**

> +      case x if x.riskLevel < riskLevel =>
> +        customerCraUpdatedLogic.handleCustomerRiskLevelUpgrade(x.customerId)(riskLevel, lastUpdated)
> +    }.getOrElse(Future.successful(Done))
> +  }
>  }
>  
>  object CustomerAdvisoryProfileTopicSubscriber {

## A3-1060 — CustomerAdvisoryProfileTopicSubscriber.scala: `persistedAcks.craCat2Ack.exists(_.isBefore())`

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/CustomerAdvisoryProfileTopicSubscriber.scala; PR: Feat/INV-736 remove acks state change

**Source-preserving request, proposal, or question:**

> Nit: `persistedAcks.craCat2Ack.exists(_.isBefore())`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2925 · comment 348733914 · PR 4770 · 2022-11-25

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/CustomerAdvisoryProfileTopicSubscriber.scala`

## A3-1061 — CraCategoryMatcher.scala: It’s better to match using type if we don’t care about underlying fields ``` case _: VulnerableCustomerProfileDto ``` Here the Dto has only 1 field, s

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cra/CraCategoryMatcher.scala; PR: [INV-852] Updated expired and vc flags

**Source-preserving request, proposal, or question:**

> It’s better to match using type if we don’t care about underlying fields
> 
> ```
> case _: VulnerableCustomerProfileDto
> ```
> 
> Here the Dto has only 1 field, so it’s ok

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2926 · comment 348710590 · PR 4780 · 2022-11-25

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cra/CraCategoryMatcher.scala`

**Evidence:** anon-2.jsonl:2926 · comment 348710590 · PR 4780 · 2022-11-25

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cra/CraCategoryMatcher.scala`

**Explicit source context (hunk):**

> +  def isVulnerable(advisoryProfile: AdvisoryProfileDto): Boolean = {
> +    advisoryProfile match {
> +      case _: VulnerableCustomerProfileDto => true
> +      case _ => false
> +    }
> +  }

## A3-1062 — CraCategoryMatcher.scala: You can match using ``` case NonVulnerableCustomerProfileDto(_, RiskProfileStatus.Expired, _, _) ```

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cra/CraCategoryMatcher.scala; PR: [INV-852] Updated expired and vc flags

**Source-preserving request, proposal, or question:**

> You can match using 
> 
> ```
> case NonVulnerableCustomerProfileDto(_, RiskProfileStatus.Expired, _, _)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2927 · comment 348710677 · PR 4780 · 2022-11-25

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cra/CraCategoryMatcher.scala`

> You can match using 
> 
> ```
> case NonVulnerableCustomerProfileDto(_, RiskProfileStatus.Expired, _, _)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2927 · comment 348710677 · PR 4780 · 2022-11-25

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cra/CraCategoryMatcher.scala`

**Explicit source context (hunk):**

> +
> +  def isCraExpired(advisoryProfile: AdvisoryProfileDto): Boolean = {
> +    advisoryProfile match {
> +      case NonVulnerableCustomerProfileDto(_, RiskProfileStatus.Expired, _, _) => true
> +      case _ => false
> +    }
> +  }

## A3-1063 — StatementDataGenerator.scala: Should we sort the pending transactions here too, to avoid unnecessary reprinting

**Source stance:** open-question

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/StatementDataGenerator.scala; PR: Feat/EN-373 statement add pending tx

**Source-preserving request, proposal, or question:**

> Should we sort the pending transactions here too, to avoid unnecessary reprinting

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2928 · comment 348669992 · PR 4744 · 2022-11-25

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/StatementDataGenerator.scala`

> Should we sort the pending transactions here too, to avoid unnecessary reprinting
> 
> ‌

**Evidence:** anon-2.jsonl:2928 · comment 348669992 · PR 4744 · 2022-11-25

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/StatementDataGenerator.scala`

**Explicit source context (hunk):**

> sameStatementDataExists = maybeStatement.exists { retrievedData: StatementInfoDto =>
>              retrievedData.statementData.fold(false) { retrievedStatementData =>
>                // Changing bank account details does NOT make the transaction different
> -              val retrievedTransactionSectionWithoutBankAccountDetails = retrievedStatementData.instrumentTransaction.map(_.copy(bankAccountDetails = None))
> -              val newTransactionSectionWithoutBankAccountDetails = statementData.instrumentTransaction.map(_.copy(bankAccountDetails = None))
> +              val retrievedTransactionSectionWithoutBankAccountDetails =

## A3-1096 — BaseServiceLogicImpl.scala: You can just use `=` if not returning a future.. It’s equivalent to `Future#map`

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; PR: [EN-231] feat(goal) create edge api for getting redeemable goals

**Source-preserving request, proposal, or question:**

> You can just use `=` if not returning a future.. It’s equivalent to `Future#map`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2962 · comment 344414078 · PR 4570 · 2022-11-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2962 · comment 344414078 · PR 4570 · 2022-11-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  private def isRedeemable(planIds: String): Future[Boolean] = {
> +    if (planIds.isEmpty) {
> +      Future.successful(false)
> +    } else {
> +      for {

## A3-1097 — BaseServiceLogicImpl.scala: There’s `mapValues` too

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; PR: [EN-231] feat(goal) create edge api for getting redeemable goals

**Source-preserving request, proposal, or question:**

> There’s `mapValues` too

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2963 · comment 344414406 · PR 4570 · 2022-11-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2963 · comment 344414406 · PR 4570 · 2022-11-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +        redemptionPlanRedeemableFlags <- redemptionService.getRedemptionPlanRedeemableStatusList(planIds).invoke()
> +      } yield redemptionPlanRedeemableFlags.exists(s => s.isRedeemable)
> +    }
> +  }
> +
> +  private def calculateAvailableMarketValueAtGoalLevel(
> +    isRedeemable: Boolean,

## A3-1098 — BaseServiceLogicImpl.scala: We can fold on map too

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; PR: [EN-231] feat(goal) create edge api for getting redeemable goals

**Source-preserving request, proposal, or question:**

> We can fold on map too

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2964 · comment 344414721 · PR 4570 · 2022-11-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2964 · comment 344414721 · PR 4570 · 2022-11-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      } yield redemptionPlanRedeemableFlags.exists(s => s.isRedeemable)
> +    }
> +  }
> +
> +  private def calculateAvailableMarketValueAtGoalLevel(
> +    isRedeemable: Boolean,
> +    ccy: CurrencyUnit,

## A3-1110 — ModifyPlanAcknowledgementsLogic.scala: Don’t need for-comprehension block if you have only one future

**Source stance:** requested-change

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/ModifyPlanAcknowledgementsLogic.scala; PR: [INV-675] Added modify acks with testcase

**Source-preserving request, proposal, or question:**

> Don’t need for-comprehension block if you have only one future

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2977 · comment 343433852 · PR 4605 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/ModifyPlanAcknowledgementsLogic.scala`

## A3-1111 — ModifyPlanAcknowledgementsLogic.scala: Hmm why need to pair these? Maybe use the usual trick with List\[Option\].flatten?

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/ModifyPlanAcknowledgementsLogic.scala; PR: [INV-675] Added modify acks with testcase

**Source-preserving request, proposal, or question:**

> Hmm why need to pair these? Maybe use the usual trick with List\[Option\].flatten?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2978 · comment 343541070 · PR 4605 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/ModifyPlanAcknowledgementsLogic.scala`

**Evidence:** anon-2.jsonl:2978 · comment 343541070 · PR 4605 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/ModifyPlanAcknowledgementsLogic.scala`

**Explicit source context (hunk):**

> +      }
> +      _ <- Future.traverse(ackCmds)(cmd => refProvider.getPlanAcknowledgementManagerEntity(planId).ask(cmd))
> +    } yield Done
> +  }
> +
> +  private def recurringPlanAcknowlegementCmds(plan: PlanDto): List[PlanAcknowledgementManagerCmd with ReplyType[_]] = {
> +    //TODO : We need to add recurring transfer ack, based on which transfer schedule

## A3-1124 — PI-only predicate is contains(PI) AND not contains(Retail)

**Source stance:** requested-change

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/util/InstrumentHelper.scala; PR: Feat/INV-732 PI check simulation confirm

**Source-preserving request, proposal, or question:**

> We want to check for PI only. So condition should be `contains(PI) AND not contains(Retail)`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2995 · comment 343544897 · PR 4619 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/util/InstrumentHelper.scala`

**Evidence:** anon-2.jsonl:2995 · comment 343544897 · PR 4619 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/util/InstrumentHelper.scala`

**Explicit source context (hunk):**

> throw ComplianceServiceException(ComplianceServiceErrorType.InternalError, s"Instrument [$instrumentId] does not have isComplex flag configured")
>              )
> -        } yield InstrumentProfile(instrumentId, ccy, riskLevel, isComplexProduct)
> +          isPIOnlyInstrument = instrument.allowedInvestorTypes.contains(InvestorType.HONGKONG_CASH_PROFESSIONAL_INVESTOR) &&
> +            !instrument.allowedInvestorTypes.contains(InvestorType.HONGKONG_CASH_RETAIL_INVESTOR)
> +        } yield InstrumentProfile(instrumentId, ccy, riskLevel, isComplexProduct, isPIOnlyInstrument)
>        }

## A3-1125 — InstrumentHelper.scala: Also can we move assign that as a field in the for block?

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/util/InstrumentHelper.scala; PR: Feat/INV-732 PI check simulation confirm

**Source-preserving request, proposal, or question:**

> Also can we move assign that as a field in the for block?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2996 · comment 343545053 · PR 4619 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/util/InstrumentHelper.scala`

**Evidence:** anon-2.jsonl:2996 · comment 343545053 · PR 4619 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/util/InstrumentHelper.scala`

**Explicit source context (hunk):**

> throw ComplianceServiceException(ComplianceServiceErrorType.InternalError, s"Instrument [$instrumentId] does not have isComplex flag configured")
>              )
> -        } yield InstrumentProfile(instrumentId, ccy, riskLevel, isComplexProduct)
> +          isPIOnlyInstrument = instrument.allowedInvestorTypes.contains(InvestorType.HONGKONG_CASH_PROFESSIONAL_INVESTOR) &&
> +            !instrument.allowedInvestorTypes.contains(InvestorType.HONGKONG_CASH_RETAIL_INVESTOR)
> +        } yield InstrumentProfile(instrumentId, ccy, riskLevel, isComplexProduct, isPIOnlyInstrument)
>        }

## A3-1127 — InstrumentHelper.scala: This flag should be isPiOnlyInstrument I think. And let’s check using contains PI and not contains Retail, so that if instrument has more investor typ

**Source stance:** requested-change

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/util/InstrumentHelper.scala; PR: Feat/INV-732 PI check simulation confirm

**Concern stated in the source:** And let’s check using contains PI and not contains Retail, so that if instrument has more investor types, we don’t need to check this logic

**Source-preserving request, proposal, or question:**

> This flag should be isPiOnlyInstrument I think. And let’s check using contains PI and not contains Retail, so that if instrument has more investor types, we don’t need to check this logic

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2998 · comment 343762795 · PR 4619 · 2022-11-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/util/InstrumentHelper.scala`

**Evidence:** anon-2.jsonl:2998 · comment 343762795 · PR 4619 · 2022-11-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/util/InstrumentHelper.scala`

**Explicit source context (hunk):**

> throw ComplianceServiceException(ComplianceServiceErrorType.InternalError, s"Instrument [$instrumentId] does not have isComplex flag configured")
>              )
> -        } yield InstrumentProfile(instrumentId, ccy, riskLevel, isComplexProduct)
> +          isPIOnlyInstrument = instrument.allowedInvestorTypes.contains(InvestorType.HONGKONG_CASH_PROFESSIONAL_INVESTOR) &&
> +            !instrument.allowedInvestorTypes.contains(InvestorType.HONGKONG_CASH_RETAIL_INVESTOR)
> +        } yield InstrumentProfile(instrumentId, ccy, riskLevel, isComplexProduct, isPIOnlyInstrument)
>        }

## A3-1136 — EdgeQueryTradingRestrictionLogic.scala: we want non-inactive. There is `LiveGoalStatusSet`

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala; PR: [INV-669] State change impacted plans

**Source-preserving request, proposal, or question:**

> I think we want non-inactive. There is `LiveGoalStatusSet`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3007 · comment 342247755 · PR 4577 · 2022-11-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala`

**Evidence:** anon-2.jsonl:3007 · comment 342247755 · PR 4577 · 2022-11-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> +
> +  override def queryCustomerPlansTradingRestriction(customerId: UUID): Future[PlanTradingRestrictionResponse] = {
> +    for {
> +      customerGoals <- goalService.getCustomerGoalsByStatus(customerId, status = None).invoke()
> +      customerCraDetails <- advisoryService.getCraDetails(customerId).invoke()
> +      craResult <- matchMultiplePlanCra(customerCraDetails.advisoryProfile, customerGoals.flatMap(s => s.plans))
> +      response <- constructResponse(craResult, customerGoals.map(goal => (goal.goalId, goal)).toMap)

## A3-1140 — EdgeQueryTradingRestrictionLogic.scala: This is a function so no need lazy?

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala; PR: [INV-669] State change impacted plans

**Source-preserving request, proposal, or question:**

> This is a function so no need lazy?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3011 · comment 342550163 · PR 4577 · 2022-11-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala`

**Evidence:** anon-2.jsonl:3011 · comment 342550163 · PR 4577 · 2022-11-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> +      }
> +    }
> +
> +    Source(plans)
> +      .mapAsyncUnordered(2) { plan => {
> +        for {
> +          targetAllocation <- extractTargetAllocation(plan)

## A3-1144 — EdgeQueryTradingRestrictionLogic.scala: There’s a `OptionUtils` , so we can write `Option.when(condition)(value)`

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala; PR: [INV-669] State change impacted plans

**Source-preserving request, proposal, or question:**

> There’s a `OptionUtils` , so we can write `Option.when(condition)(value)`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3015 · comment 342550973 · PR 4577 · 2022-11-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala`

**Evidence:** anon-2.jsonl:3015 · comment 342550973 · PR 4577 · 2022-11-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> +            ),
> +            s._2
> +          )
> +        })
> +
> +        PlanTradingRestrictionResponse(
> +          recurringPlansRequireAcks = impactedPlanDtoMap.filter(!_._2).keySet.toList,

## A3-1148 — EdgeQueryTradingRestrictionLogic.scala: It’s internal impl of this class to provide the goal map. Can just use `goalIdMap(plan.goalId)` directly I think

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala; PR: [INV-669] State change impacted plans

**Source-preserving request, proposal, or question:**

> It’s internal impl of this class to provide the goal map. Can just use `goalIdMap(plan.goalId)` directly I think

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3019 · comment 343434579 · PR 4577 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala`

## A3-1151 — EdgeQueryTradingRestrictionLogic.scala: Or don’t need to check and just call `goalIdMap(plan.goalId)` directly :stuck_out_tongue:

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala; PR: [INV-669] State change impacted plans

**Source-preserving request, proposal, or question:**

> Or don’t need to check and just call `goalIdMap(plan.goalId)` directly :stuck_out_tongue:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3022 · comment 343438284 · PR 4577 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala`

## A3-1171 — BaseServiceLogicImpl.scala: Hmmm the fields are Option but in the logic below, we filter for isDefined only..

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/BaseServiceLogicImpl.scala; PR: INV-652 Fund smart instruments API

**Source-preserving request, proposal, or question:**

> Hmmm the fields are Option but in the logic below, we filter for isDefined only..

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3044 · comment 341753867 · PR 4527 · 2022-10-31

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:3044 · comment 341753867 · PR 4527 · 2022-10-31

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> } yield Done
>    }
>  
> -  private def fetchPerformanceForInstruments(instrumentIds: List[String], ccy: CurrencyUnit): Future[Map[String, AnnualisedPerformanceMetricsDto]] = {
> +  protected def fetchPerformanceForInstruments(
> +    instruments: Seq[InstrumentInfoDto],

## A3-1172 — BaseServiceLogicImpl.scala: Something like this? Not sure how to handle 2 options… ``` ipDto => { ipDto.commonPeriodPerformanceMetrics .flatMap( metric => if (metric.annualisedPe

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/BaseServiceLogicImpl.scala; PR: INV-652 Fund smart instruments API

**Source-preserving request, proposal, or question:**

> Something like this? Not sure how to handle 2 options…
> 
> ```
> ipDto => {
>   ipDto.commonPeriodPerformanceMetrics
>     .flatMap(
>       metric =>
>         if (metric.annualisedPerformanceMetrics.isDefined && metric.oneYearRollingPerformanceMetrics.isDefined)
>           Some(PerformanceData(metric.annualisedPerformanceMetrics, metric.oneYearRollingPerformanceMetrics.map(_.worstAnnualisedReturn)))
>         else None
>     )
>     .map(ipDto.instrumentId -> _)
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3045 · comment 341754121 · PR 4527 · 2022-10-31

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/BaseServiceLogicImpl.scala`

> Something like this? Not sure how to handle 2 options…
> 
> ```
> ipDto => {
>   ipDto.commonPeriodPerformanceMetrics
>     .flatMap(
>       metric =>
>         if (metric.annualisedPerformanceMetrics.isDefined && metric.oneYearRollingPerformanceMetrics.isDefined)
>           Some(PerformanceData(metric.annualisedPerformanceMetrics, metric.oneYearRollingPerformanceMetrics.map(_.worstAnnualisedReturn)))
>         else None
>     )
>     .map(ipDto.instrumentId -> _)
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3045 · comment 341754121 · PR 4527 · 2022-10-31

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> _.flatMap(
> -            _.filter(ipDto => ipDto.commonPeriodPerformanceMetrics.isDefined && ipDto.commonPeriodPerformanceMetrics.get.annualisedPerformanceMetrics.isDefined)
> -              .map(ipDto => ipDto.instrumentId -> ipDto.commonPeriodPerformanceMetrics.get.annualisedPerformanceMetrics.get)
> +            _.filter(ipDto => {
> +              ipDto.commonPeriodPerformanceMetrics.isDefined
> +            }).filter(ipDto => {
> +                val commonPeriodPerformanceMetrics = ipDto.commonPeriodPerformanceMetrics.get

## A3-1173 — SgServiceLogicImpl.scala: Need `toList` meh?

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; PR: INV-652 Fund smart instruments API

**Source-preserving request, proposal, or question:**

> Need `toList` meh?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3046 · comment 341758872 · PR 4527 · 2022-10-31

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:3046 · comment 341758872 · PR 4527 · 2022-10-31

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  private def addDerivedTags(instruments: Seq[InstrumentInfoDto]): Seq[InstrumentInfoDto] = {
> +    addCommonDerivedTags(instruments)
> +      .flatMap(
> +        i =>
> +          i.configDetails.map(cd => {

## A3-1209 — TradingRestrictionLogic.scala: Minor: maybe we can write this as ``` s.craCat2Ack.map(_ => CraCat2Ack) s.recurringInvestmentAck.map(_ => RecurringTransactionAck).filter(_ => request

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala; PR: Feat/INV-560 recurring and ack persistence

**Source-preserving request, proposal, or question:**

> Minor: maybe we can write this as  
> 
> ```
> s.craCat2Ack.map(_ => CraCat2Ack)
> s.recurringInvestmentAck.map(_ => RecurringTransactionAck).filter(_ => request.isInstanceOf[RecurringInvestmentRestrictionRequest])
> ```
> 
>   
> But yeah, if else is ok too

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3083 · comment 338185257 · PR 4477 · 2022-10-17

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Evidence:** anon-2.jsonl:3083 · comment 338185257 · PR 4477 · 2022-10-17

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> +      acks <- if (request.isRecurringTransaction) {
> +        refProvider.getPlanAcknowledgementManagerEntity(planId).ask(GetPlanAcknowledgementsCmd)
> +          .map(s => {
> +            val maybeRecurringTransferAck = s.recurringTransferAck.map(_ => RecurringTransactionAck).filter(_ => request.isInstanceOf[RecurringTransferRestrictionRequest])
> +            val maybeRecurringInvestmentAck = s.recurringInvestmentAck.map(_ => RecurringTransactionAck).filter(_ => request.isInstanceOf[RecurringInvestmentRestrictionRequest])
> +            val maybeCraCat2Ack = s.craCat2Ack.map(_ => CraCat2Ack)
> +

## A3-1221 — MarketDataUploader.scala: Yeah, I can’t see the benefit of this being in separate for-comprehension block

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; PR: Feat/INV-613 add annual yield marketdata

**Source-preserving request, proposal, or question:**

> Yeah, I can’t see the benefit of this being in separate for-comprehension block

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3096 · comment 337782621 · PR 4486 · 2022-10-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:3096 · comment 337782621 · PR 4486 · 2022-10-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (hunk):**

> +    val mstarApiIdFut = getMstarApiId(instrumentId)
> +    val instrumentCcyFut = getInstrumentCcy(instrumentId)
> +
> +    val annualYieldInstrumentCcyFut: Future[(MstarAnnualYield, CurrencyUnit)] = for {
> +      id <- mstarApiIdFut
> +      instrumentCcy <- instrumentCcyFut
> +      annualYield <- mstarApiService.getAnnualYield(id, instrumentCcy)

## A3-1223 — InstrumentManager.scala: Wanna take this chance to refactor this into for-comprehension instead of async await?

**Source stance:** open-question

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/InstrumentManager.scala; PR: adds fund inception date/distribution status/is complex to instrument

**Source-preserving request, proposal, or question:**

> Wanna take this chance to refactor this into for-comprehension instead of async await?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3098 · comment 336600016 · PR 4455 · 2022-10-10

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/InstrumentManager.scala`

**Evidence:** anon-2.jsonl:3098 · comment 336600016 · PR 4455 · 2022-10-10

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/InstrumentManager.scala`

**Explicit source context (hunk):**

> createdInstrument
>    }
>  
> -  def createFundInstrument(request: UpsertFundInstrumentRequest): Future[InstrumentInfoDto] = async {
> -    val isin = request.id
> -    val mstarId = MstarApiId(isin, MstarApiIdType.ISIN)
> -    val isMstarCompatibleInstrument = request.isMstarCompatibleInstrument.getOrElse(true)
> -    val (name, idMap) = if (isMstarCompatibleInstrument) {
> -      val basicFundInfoFut = mstarApiService.getFundShareClassBasicInfo(mstarId)
> -      val fundBasicInfo = await(basicFundInfoFut)
> -      val idMap = Map(
> -        InstrumentIdType.MSTAR_ID -> fundBasicInfo.mstarId,
> -        InstrumentIdType.ISIN -> fundBasicInfo.isin
> +  def createFundInstrument(request: UpsertFundInstrumentRequ

## A3-1232 — CraManagerTest.scala: Use `None`

**Source stance:** requested-change

**Context:**

> advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/hk/CraManagerTest.scala; PR: Feat/INV-560 cra2 complex ack

**Source-preserving request, proposal, or question:**

> Use `None`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3108 · comment 336581844 · PR 4449 · 2022-10-10

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/hk/CraManagerTest.scala`

**Evidence:** anon-2.jsonl:3108 · comment 336581844 · PR 4449 · 2022-10-10

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/hk/CraManagerTest.scala`

**Explicit source context (hunk):**

> liquidNetWorth = vcRequest.liquidNetWorth,
> -            craQuestionnaire = vcRequest.craQuestionnaire
> +            craQuestionnaire = vcRequest.craQuestionnaire,
> +            complexProductKnowledgeAttestationDate = None
>            )
>          }
>        }

## A3-1240 — HkServiceLogicMockUtils.scala: Ok for test code, but a NIT still: it’s easier to follow if we assign val for `craResponse` based on the logic. I inline it previously because there w

**Source stance:** suggestion

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/utils/HkServiceLogicMockUtils.scala; PR: Feat/INV-560 cra2 complex ack

**Concern stated in the source:** I inline it previously because there was no logic

**Source-preserving request, proposal, or question:**

> Ok for test code, but a NIT still: it’s easier to follow if we assign val for `craResponse` based on the logic. I inline it previously because there was no logic

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3118 · comment 336784247 · PR 4449 · 2022-10-11

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/utils/HkServiceLogicMockUtils.scala`

**Evidence:** anon-2.jsonl:3118 · comment 336784247 · PR 4449 · 2022-10-11

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/utils/HkServiceLogicMockUtils.scala`

**Explicit source context (hunk):**

> val craProfileServiceCall = mock[ServiceCall[NotUsed, CraDetailsResponse]]
>      when(advisoryService.getCraDetails(customerId)).thenReturn(craProfileServiceCall)
> -    when(craProfileServiceCall.invoke()).thenReturn(Future.successful(BaseCraResponse.copy(advisoryProfile = advisoryProfile, liquidNetWorth = liquidNetWorth)))
> +    when(craProfileServiceCall.invoke()).thenReturn(Future.successful(BaseCraResponse.copy(advisoryProfile = advisoryProfile, liquidNetWorth = liquidNetWorth, complexProductKnowledgeAttestationDate = attestedDate)))
>    }
>  
>    def `setupGoalService / getCustomerGoals`(customerId: UUID, instrumentWeightsByPlan: Map[UUID, Map[String, BigDecimal]], overridingCcyByPlan: Map[UUID, CurrencyUnit]): Unit = {

## A3-1255 — HkInvestmentTopicSubscriber.scala: not worry about these for now. But you will need to provide a case for them, otherwise we would get a `MatchError`

**Source stance:** requested-change

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala; PR: Feat/INV-551 release earmark

**Concern stated in the source:** But you will need to provide a case for them, otherwise we would get a `MatchError`

**Source-preserving request, proposal, or question:**

> Let’s not worry about these for now. But you will need to provide a case for them, otherwise we would get a `MatchError`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3136 · comment 335025166 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:3136 · comment 335025166 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Explicit source context (hunk):**

> +      case RECURRING_INVESTMENT => Option.apply(SubsequentInvestmentEarmarkId(
> +        goalId = goalId, planId = planId, investmentRequestId = investmentRequestId
> +      ))
> +      //To prevent kafka offset block we just notify
> +      case INVESTMENT_TRANSFER =>
> +        logger.warn("Investment Transfer is not implemented yet")
> +        Option.empty

## A3-1260 — HkInvestmentTopicSubscriber.scala: Maybe use `Option#fold`?

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala; PR: Feat/INV-551 release earmark

**Source-preserving request, proposal, or question:**

> Nit: Maybe use `Option#fold`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3141 · comment 335044643 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:3141 · comment 335044643 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Explicit source context (hunk):**

> +    }
> +
> +    maybeBuyEarmarkId.fold[Future[Done]]{Future.successful(Done)} {
> +      earmarkId => serviceLogic.releaseEarmark(customerId)(earmarkId, reason, requestedBy)
> +    }
> +  }
> +}

## A3-1263 — HkInvestmentTopicSubscriber.scala: Return Option here instead of null..

**Source stance:** requested-change

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala; PR: Feat/INV-551 release earmark

**Source-preserving request, proposal, or question:**

> Return Option here instead of null..

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3144 · comment 335067347 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:3144 · comment 335067347 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Explicit source context (hunk):**

> +    reason: String,
> +    requestedBy: String
> +  ): Future[Done] = {
> +    val maybeBuyEarmarkId = investmentReason match {
> +      case INITIAL_INVESTMENT => Option.apply(InitialInvestmentEarmarkId (
> +        goalId = goalId, planId = planId
> +      ))

## A3-1265 — HkInvestmentTopicSubscriber.scala: Just notice this :rofl: It’s `Some` vs `None`, but yeah `Option.apply` vs `Option.empty` works too, just looks weird

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala; PR: Feat/INV-551 release earmark

**Source-preserving request, proposal, or question:**

> Just notice this :rofl: It’s `Some` vs `None`, but yeah `Option.apply` vs `Option.empty` works too, just looks weird

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3146 · comment 335701131 · PR 4377 · 2022-10-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:3146 · comment 335701131 · PR 4377 · 2022-10-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Explicit source context (hunk):**

> +      //To prevent kafka offset block we just notify
> +      case INVESTMENT_TRANSFER =>
> +        logger.warn("Investment Transfer is not implemented yet")
> +        Option.empty
> +      case DIVIDEND_REINVESTMENT =>
> +        logger.warn("Dividend Reinvestment is not implemented yet")
> +        Option.empty

## A3-1289 — InvestmentValueCalculator.scala: Oh you’re talking about the `#map` honouring the characteristic of the original collection.. well once I know it, it becomes normal to me :rofl: But y

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/InvestmentValueCalculator.scala; PR: [INV-552] feat(compliance): Handle MCCY when calculate customer's investment values

**Source-preserving request, proposal, or question:**

> Oh you’re talking about the `#map` honouring the characteristic of the original collection.. well once I know it, it becomes normal to me :rofl: 
> 
> But yes, in this case, I expect all instruments to be same ccy, so I actually want result to be a Set, except I can’t pattern match on a Set, hence that last `toList`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3171 · comment 334023446 · PR 4345 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/InvestmentValueCalculator.scala`

**Evidence:** anon-2.jsonl:3171 · comment 334023446 · PR 4345 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/InvestmentValueCalculator.scala`

**Explicit source context (hunk):**

> -      additionalInvestmentTaaPoRR <- calculatePoRR(additionalInvestmentTaa)
> -      intendedAdditionalInvestmentByRiskLevel = List(additionalInvestmentTaaPoRR -> additionalInvestmentAmount)
> +      instrumentProfileTaa <- instrumentHelper.lookupInstrumentProfiles(additionalInvestmentTaa)
> +      investmentCcy = instrumentProfileTaa.keySet.map(_.ccy).toList match {
> +        case ccy :: Nil => ccy
> +        case others =>
> +          throw ComplianceServiceException(

## A3-1303 — CustomerTradingEarmarkManagerEntity.scala: How about we refactor this a bit? Using pattern match on the find? ```scala state.buyEarmarks.find(_.id == cmd.buyEarmark.id) match { case Some(existi

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> How about we refactor this a bit? Using pattern match on the find?
> 
> ```scala
> state.buyEarmarks.find(_.id == cmd.buyEarmark.id) match {
>   case Some(existingEarmark) =>
>     if (existingEarmark.amount != cmd.buyEarmark.amount) {
>       // throw
>     } else {
>       // warn and reply done
>     }
>   case None =>
>     // emit event
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 3174, 3178, 3180, 3185, 3200, 3201: Keep currentVersion check, no-op duplicateID+amount, reject changed amount, new event only for new earmark;3200 question does not override3201 matrix.

**Evidence:** anon-2.jsonl:3185 · comment 334015485 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

> How about we refactor this a bit? Using pattern match on the find?
> 
> ```scala
> state.buyEarmarks.find(_.id == cmd.buyEarmark.id) match {
>   case Some(existingEarmark) =>
>     if (existingEarmark.amount != cmd.buyEarmark.amount) {
>       // throw
>     } else {
>       // warn and reply done
>     }
>   case None =>
>     // emit event
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3185 · comment 334015485 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +        )
> +      )
> +      ctx.done
> +    } else {
> +      state.buyEarmarks.find(_.id == cmd.buyEarmark.id) match {
> +        case Some(existingEarmark) =>
> +          if (existingEarmark.amount != cmd.buyEarmark.amount) {

## A3-1313 — CustomerTradingEarmarkManagerEntity.scala: Sorry I just notice this. We don’t actually care about ordering, so maybe let’s prepend instead of append, to some some peanut cost

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Sorry I just notice this. We don’t actually care about ordering, so maybe let’s prepend instead of append, to some some peanut cost

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3195 · comment 334025678 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Evidence:** anon-2.jsonl:3195 · comment 334025678 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +      }
> +
> +  private def handleEvents(): EventHandler = {
> +    case (evt: BuyEarmarkCreatedEvt, state) => state.copy(evt.buyEarmark +: state.buyEarmarks)
> +  }
> +
> +  private def handleCreateBuyEarmark(

## A3-1315 — CustomerTradingEarmarkManagerEntity.scala: In scala, we can use ==

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> In scala, we can use ==

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3197 · comment 334025824 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Evidence:** anon-2.jsonl:3197 · comment 334025824 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +      )
> +      ctx.done
> +    } else {
> +      state.buyEarmarks.find(_.id == cmd.buyEarmark.id) match {
> +        case Some(existingEarmark) =>
> +          if (existingEarmark.amount != cmd.buyEarmark.amount) {
> +            ctx.commandFailed(

## A3-1327 — HkServiceLogicImpl.scala: Hmm `Map[InstrumentProfile, BigDecimal]` already can be mapped to instrumentWeights?

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/impl/HkServiceLogicImpl.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Hmm `Map[InstrumentProfile, BigDecimal]` already can be mapped to instrumentWeights?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3209 · comment 333174233 · PR 4330 · 2022-09-26

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/impl/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:3209 · comment 333174233 · PR 4330 · 2022-09-26

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/impl/HkServiceLogicImpl.scala`

**Explicit source context (hunk):**

> -    def relaxRestrictionIfNoImmediateTradingImpact(responseFut: => Future[TradingRestrictionResponse]): Future[TradingRestrictionResponse] = {
> +    def relaxRestrictionIfNoImmediateTradingImpact(responseFut: => TradingRestrictionResponse): Future[TradingRestrictionResponse] = {
>        if (request.hasImmediateTradingImpact)
> -        responseFut
> +        Future.successful(responseFut)
>        else

## A3-1339 — package.scala: This needs to be a collection, cuz we will need multiple fxRates \(per date, per ccypair\)

**Source stance:** requested-change

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/package.scala; PR: INV-235 feat: Transaction types modelling

**Concern stated in the source:** This needs to be a collection, cuz we will need multiple fxRates \(per date, per ccypair\)

**Source-preserving request, proposal, or question:**

> This needs to be a collection, cuz we will need multiple fxRates \(per date, per ccypair\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3224 · comment 331131620 · PR 4256 · 2022-09-16

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/package.scala`

## A3-1377 — PortfolioMarketDataEntity.scala: Use `updatedPriceMap` below and check forAll\(contain\) ?

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/portfolio/PortfolioMarketDataEntity.scala; PR: wip

**Source-preserving request, proposal, or question:**

> Nit: Use `updatedPriceMap` below and check forAll\(contain\) ?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3266 · comment 319675677 · PR 3873 · 2022-07-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/portfolio/PortfolioMarketDataEntity.scala`

**Evidence:** anon-2.jsonl:3266 · comment 319675677 · PR 3873 · 2022-07-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/portfolio/PortfolioMarketDataEntity.scala`

**Explicit source context (hunk):**

> +
> +    val existingInstrumentPriceMap = state.marketData.filterNot(_.businessDate.isBefore(pricesAsOf)).map(_.instrumentPrices).getOrElse(Map())
> +
> +    val updatedPriceMap = existingInstrumentPriceMap ++ dailyPricesForLatestBusinessDate
> +
> +    val isCompleteData = state.instrumentWeights.keySet.subsetOf(updatedPriceMap.keySet)
> +

## A3-1381 — distributeAmountByWeight used to distribute weights with TotalWeights1

**Source stance:** explanation

**Context:**

> gateway-impl/src/main/scala/com/endowus/silver/gateway/impl/managers/bffs/RecommendedPortfolioChangePageLoader.scala; PR: IAO-379: Adjust actual weight from AAA in case sum != 1

**Source-preserving request, proposal, or question:**

> The `Calculator#distributeAmountByWeight` is intended to distribute amount via weights… but I’m distributing weights via weights… hence `totalAmount = TotalWeights (1)`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3271 · comment 322801867 · PR 4038 · 2022-08-11

Source path: `gateway-impl/src/main/scala/com/endowus/silver/gateway/impl/managers/bffs/RecommendedPortfolioChangePageLoader.scala`

**Evidence:** anon-2.jsonl:3271 · comment 322801867 · PR 4038 · 2022-08-11

Source path: `gateway-impl/src/main/scala/com/endowus/silver/gateway/impl/managers/bffs/RecommendedPortfolioChangePageLoader.scala`

**Explicit source context (hunk):**

> +            ratioScale = RatioScale,
> +            rounding = Rounding
> +          )(
> +            totalAmount = TotalWeights,
> +            weightedElements = composition.instrumentBreakdowns
> +              .filter(_.actualWeight > 0)
> +              .map { instrumentHoldingBreakdown =>

## A3-1389 — PlanUpsertSummaryBehaviour.scala: let’s do that. At least we can see the decision to calculate projection and to call maybeProjection.get in one place

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/PlanUpsertSummaryBehaviour.scala; PR: IAO-56 FundSmart ProductLine Plan Upsert

**Source-preserving request, proposal, or question:**

> Yeah let’s do that. At least we can see the decision to calculate projection and to call maybeProjection.get in one place

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3282 · comment 317748185 · PR 3859 · 2022-07-21

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/PlanUpsertSummaryBehaviour.scala`

**Evidence:** anon-2.jsonl:3282 · comment 317748185 · PR 3859 · 2022-07-21

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/PlanUpsertSummaryBehaviour.scala`

**Explicit source context (hunk):**

> portfolioComposition = baseSummary.portfolioComposition,
>            portfolioPerformance = baseSummary.portfolioPerformance,
> -          portfolioProjection = baseSummary.portfolioProjection
> +          portfolioProjection = baseSummary.portfolioProjection.get
>        )
>      )
>    }

## A3-1390 — PlanUpsertSummaryBehaviour.scala: Ah I mean, both of these at same one method scope \(aka product specific method\) * `calculateProjection = true` * `portfolioProjection = baseSummary.

**Source stance:** requested-change

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/PlanUpsertSummaryBehaviour.scala; PR: IAO-56 FundSmart ProductLine Plan Upsert

**Source-preserving request, proposal, or question:**

> Ah I mean, both of these at same one method scope \(aka product specific method\)
> 
> * `calculateProjection = true`
> * `portfolioProjection = baseSummary.mayBePortfolioProjection.get`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3283 · comment 317896568 · PR 3859 · 2022-07-21

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/PlanUpsertSummaryBehaviour.scala`

> Ah I mean, both of these at same one method scope \(aka product specific method\)
> 
> * `calculateProjection = true`
> * `portfolioProjection = baseSummary.mayBePortfolioProjection.get`
> 
> ‌

**Evidence:** anon-2.jsonl:3283 · comment 317896568 · PR 3859 · 2022-07-21

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/PlanUpsertSummaryBehaviour.scala`

**Explicit source context (hunk):**

> portfolioComposition = baseSummary.portfolioComposition,
>            portfolioPerformance = baseSummary.portfolioPerformance,
> -          portfolioProjection = baseSummary.portfolioProjection
> +          portfolioProjection = baseSummary.portfolioProjection.get
>        )
>      )
>    }

## A3-1404 — package.scala: use `Either`?

**Source stance:** open-question

**Context:**

> goal-api/src/main/scala/com/endowus/silver/goal/api/requests/package.scala; PR: Feat/IAO-157 cka checks

**Source-preserving request, proposal, or question:**

> Let’s use `Either`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3299 · comment 313791784 · PR 3760 · 2022-07-05

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/requests/package.scala`

**Evidence:** anon-2.jsonl:3299 · comment 313791784 · PR 3760 · 2022-07-05

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/requests/package.scala`

**Explicit source context (hunk):**

> +    implicit def toUpdateV2OrStop(
> +      request: UpdateRecurringInvestmentScheduleRequest
> +    ): (Option[UpdateRecurringInvestmentScheduleRequestV2], Option[StopRecurringInvestmentScheduleRequest]) = {
> +      if (request.stopRecurring.contains(true)) {
> +        (None, Some(StopRecurringInvestmentScheduleRequest(goalId = request.goalId, planId = request.planId)))
> +      } else {

## A3-1410 — MasApiService.scala: use `(Ordering[Long].reverse)` would be clearer to me. This `* -1` is not always very visible

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mas/MasApiService.scala; PR: fixes fx rate mas parsing issue and daily price fx conversion issue

**Source-preserving request, proposal, or question:**

> use `(Ordering[Long].reverse)` would be clearer to me. This `* -1` is not always very visible

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3305 · comment 314039471 · PR 3796 · 2022-07-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mas/MasApiService.scala`

**Evidence:** anon-2.jsonl:3305 · comment 314039471 · PR 3796 · 2022-07-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mas/MasApiService.scala`

**Explicit source context (hunk):**

> }
>            .runWith(Sink.seq)
> -      } yield fxRates.flatten.toList.map(s => s._1 -> s._2).toMap.toList.sortBy(_._1.toEpochDay).reverse
> +      } yield fxRates.flatten.toList.map(s => s._1 -> s._2).toMap.toList.sortBy(_._1.toEpochDay)(Ordering[Long].reverse)
>      }
>  
>      val fut = (baseCcy.getCode, quoteCcy.getCode) match {

## A3-1413 — Cross-FX old intersection behavior versus new all-base-rates-from-minDate calculation

**Source stance:** explanation

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mas/MasApiService.scala; PR: fixes fx rate mas parsing issue and daily price fx conversion issue

**Source-preserving request, proposal, or question:**

> Previous impl calculates only for intersection between 2 sets. It has logic to find last possible rate in `rateToMultiply`… but since it iterates `commonDates`, it should always find exact match.
> 
> Here we will calculate for all base rates from minDate

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 3304, 3306, 3308, 3311: Cross-FX latest-common-date question, existing getAll observation, intersection-versus-base-range behavior and display-only acceptance remain distinct.

**Evidence:** anon-2.jsonl:3308 · comment 314040502 · PR 3796 · 2022-07-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mas/MasApiService.scala`

> Previous impl calculates only for intersection between 2 sets. It has logic to find last possible rate in `rateToMultiply`… but since it iterates `commonDates`, it should always find exact match.
> 
> Here we will calculate for all base rates from minDate
> 
> ‌

**Evidence:** anon-2.jsonl:3308 · comment 314040502 · PR 3796 · 2022-07-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mas/MasApiService.scala`

**Explicit source context (hunk):**

> +          _ = { logger.info(s"found fx rates for [$baseCcy|$quoteCcy], starting from [$minDate] to [${baseCcyAgainstSgdMap.maxBy(_._1)}]]") }
> +          //ideally can be computed for all the dates from minDate to min (max date of baseCcyAgainstSgdMap, max date of sgdAgainstQuoteCcyMap)
> +          //but keeping the previous behaviour of driving the calculation using baseCcyAgainstSgp
> +          baseQuote = baseCcyAgainstSgdMap.keySet
> +            .filterNot(_.isBefore(minDate))
> +            .map { fxDate =>
> +              val fxRate = baseCcyAgainstSgdMap(fxDate)

## R-3316 — It doesn’t matter much, but I don’t want to change the ordering of submitted answers…

**Source stance:** requested-change

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/hk/cra/ScoreCalculator.scala; PR 3754: HK CRA changes

**Source-preserving request, proposal, or question:**

> It doesn’t matter much, but I don’t want to change the ordering of submitted answers…

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3316 · comment 315806767 · PR 3754 · 2022-07-13

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/hk/cra/ScoreCalculator.scala`

## R-3324 — Maybe just `Option.map().getOrElse()` is sufficient here?

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/goalcreate/GoalCreateValidationBehaviour.scala; PR 3721: Feat/IA productLine/FundSmartCreate

**Source-preserving request, proposal, or question:**

> Maybe just `Option.map().getOrElse()` is sufficient here?

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3324 · comment 313766010 · PR 3721 · 2022-07-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/goalcreate/GoalCreateValidationBehaviour.scala`

## R-3325 — Same for `employmentDetails` below

**Source stance:** requested-change

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/goalcreate/GoalCreateValidationBehaviour.scala; PR 3721: Feat/IA productLine/FundSmartCreate

**Source-preserving request, proposal, or question:**

> Same for `employmentDetails` below

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3325 · comment 313766044 · PR 3721 · 2022-07-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/goalcreate/GoalCreateValidationBehaviour.scala`

## R-3398 — We can use exists\(predicate\) again with configDetails right?

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/InstrumentServiceImpl.scala; PR 3398: Feat/IAO-93 block goal modification

**Source-preserving request, proposal, or question:**

> We can use exists\(predicate\) again with configDetails right?

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3398 · comment 295777425 · PR 3398 · 2022-04-20

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/InstrumentServiceImpl.scala`

## R-3406 — Unit is like void, hence everything it mappable to Unit. And by extension, every Future\[Blah\] to mappable to Future\[Unit\]. We normally return Future\[a

**Source stance:** explanation

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/brokerAccount/processors/BrokerAccountDividendsJdbcEventProcessor.scala; PR 3299: changes to use cassandra read side

**Source-preserving request, proposal, or question:**

> Unit is like void, hence everything it mappable to Unit. And by extension, every Future\[Blah\] to mappable to Future\[Unit\].
> 
> We normally return Future\[akka.Done\] if we just want to indicate the future completes, but does not return any value.
> 
> If you still want to return nothing \(aka Unit\), then use `yield ()`. Unit is a type that has only one valid value, which is `()`

**Evidence:** anon-2.jsonl:3406 · comment 293158203 · PR 3299 · 2022-04-07

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/brokerAccount/processors/BrokerAccountDividendsJdbcEventProcessor.scala`

## R-3447 — Looks like this customerSource can be just customerId instead of full DTO?

**Source stance:** suggestion

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpStatementGenerator.scala; PR 3217: moves to generate metadata separately

**Source-preserving request, proposal, or question:**

> Looks like this customerSource can be just customerId instead of full DTO?

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3447 · comment 286840320 · PR 3217 · 2022-03-11

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpStatementGenerator.scala`

## R-3448 — So we have unlisted SIP and listed SIP \(or just SIP\)? Should we name this method and its filter `isUnlistedSip`?

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/db/jdbc/InstrumentJdbcRepository.scala; PR 3144: [SILVER-12528] feat(instrument): Add sip and eip filters for JDBC repo

**Source-preserving request, proposal, or question:**

> So we have unlisted SIP and listed SIP \(or just SIP\)? Should we name this method and its filter `isUnlistedSip`?

**Evidence:** anon-2.jsonl:3448 · comment 284124623 · PR 3144 · 2022-02-28

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/db/jdbc/InstrumentJdbcRepository.scala`

## R-3449 — This already returns `Future[Done]` so we don’t need this for comprehend at all? Also for timing, would you like to give `TimeUtils.TimedLogger` a try? You

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala; PR 3155: Feat/projection svc multiccy batch manager

**Source-preserving request, proposal, or question:**

> This already returns `Future[Done]` so we don’t need this for comprehend at all?
> 
> Also for timing, would you like to give `TimeUtils.TimedLogger` a try?
> 
> You can use it like this
> 
> ```scala
> logger.logTime("renewProjectionForAllV2") {
>   multiCcySimulationBatchManager.renewProjectionsForAll
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3449 · comment 284843163 · PR 3155 · 2022-03-03

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala`

## R-3489 — Would `filter().result.headOption` be enough?

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/plan/PlanProfileDaoJdbc.scala; PR 3059: Feat/SILVER-11759 jdbc readside plan mv

**Source-preserving request, proposal, or question:**

> Would `filter().result.headOption` be enough?

**Conditions and limits:**

- The result.headOption suggestion is followed by recognition that take(1) remains in the query and becomes LIMIT 1; the later response prefers the existing take(1) approach. Source rows: anon-2.jsonl:3489, anon-2.jsonl:3490.
- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3489 · comment 280645232 · PR 3059 · 2022-02-17

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/plan/PlanProfileDaoJdbc.scala`

## R-3490 — take(1) translates to LIMIT 1, correcting the earlier result.headOption suggestion

**Source stance:** reported-verification

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/plan/PlanProfileDaoJdbc.scala; PR 3059: Feat/SILVER-11759 jdbc readside plan mv

**Source-preserving request, proposal, or question:**

> [incidental identifier omitted] Ah ok I was confused. `take(1)` is still query API, so it would translate to `LIMIT 1` in actual query. So this is better :thumbsup: 

**Conditions and limits:**

- The result.headOption suggestion is followed by recognition that take(1) remains in the query and becomes LIMIT 1; the later response prefers the existing take(1) approach. Source rows: anon-2.jsonl:3489, anon-2.jsonl:3490.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3490 · comment 280661395 · PR 3059 · 2022-02-17

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/plan/PlanProfileDaoJdbc.scala`

>  Ah ok I was confused. `take(1)` is still query API, so it would translate to `LIMIT 1` in actual query. So this is better :thumbsup: 

## R-3505 — We have 2 somewhat generic helper functions for now ``` def findProductPortfolio(advisoryTag: AdvisoryTag, targetStockRatio: BigDecimal, tradingAccountType

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/GoalModifySummaryBehaviour.scala; PR 3019: SILVER-11923: Factors goal modify summary/confirmation

**Source-preserving request, proposal, or question:**

> We have 2 somewhat generic helper functions for now
> 
> ```
> def findProductPortfolio(advisoryTag: AdvisoryTag, targetStockRatio: BigDecimal, tradingAccountType: TradingAccountType): Future[ProductPortfolio]
> def findProductPortfolio(advisoryTag: AdvisoryTag, targetStockRatio: BigDecimal): Future[Seq[ProductPortfolio]]
> ```
> 
> ‌
> 
> During add goal, it’s single trading account. During modify goal, it’s multiple trading accounts.
> 
> I keep them not product specific to avoid API explosion in the helper class. I guess we can revisit this when we see more use cases for next product.

**Evidence:** anon-2.jsonl:3505 · comment 279066281 · PR 3019 · 2022-02-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/GoalModifySummaryBehaviour.scala`

## R-3508 — I prefer scaladoc over comments. But one could argue you can name things better to explain yourself. For example, ```scala private def getDividendTransacti

**Source stance:** suggestion

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/CalculateTransactionData.scala; PR 2932: Fix/SILVER-11625 dividend details txn date update

**Source-preserving request, proposal, or question:**

> I prefer scaladoc over comments.
> 
> But one could argue you can name things better to explain yourself.
> 
> For example,
> 
> ```scala
> private def getDividendTransactionDate(transaction: TransactionDto, dateIfReinvestedByUOHKB: LocalDate, dateIfReinvestedByEndowus: LocalDate): LocalDate = {
>   def isDividendReinvestedByUOBKH = transaction.orders.isEmpty
>   if (isDividendReinvestedByUOBKH) {
>     dateIfReinvestedByUOHKB
>   } else {
>     dateIfReinvestedByEndowus
>   }
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3508 · comment 277310006 · PR 2932 · 2022-02-04

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/CalculateTransactionData.scala`

## R-3558 — Portfolio stats exact-ID lookup and filter lookup both produce a List response

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala; PR 2807: Feat/projection svc portfolio stats jdbc

**Source-preserving request, proposal, or question:**

> Maybe something like this?
> 
> ```scala
> for {
>   stats <- (portfolioId, effectiveDate, statsCcy) match {
>     case (Some(pid), Some(date), Some(ccy)) => portfolioStatsJdbcRepository.findById(pid, date, ccy).map(_.toSeq)
>     case _ => portfolioStatsJdbcRepository.findByFilter(portfolioId, effectiveDate, statsCcy)
>   }
> } yield stats.map(PortfolioStats.toDto).toList
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3558 · comment 270161114 · PR 2807 · 2021-12-30

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala`

## R-3569 — Existing monthly-change sort is found; originalMonthlyChanges input still questioned

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/InstrumentMonthlyChangeJdbcBasedFxConverter.scala; PR 2790: Feat/SILVER-10779 multiccy monthly changes

**Source-preserving request, proposal, or question:**

> ~~Do we sort anywhere? Better not to assume the ordering I think…~~
> 
> Found the sort.. but maybe we should still sort the provided input `originalMonthlyChanges` if any

**Evidence:** anon-2.jsonl:3569 · comment 269769051 · PR 2790 · 2021-12-28

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/InstrumentMonthlyChangeJdbcBasedFxConverter.scala`

## R-3571 — Can we rely on fxRate to take care of inverting the rate already? e.g. it’s EURUSD but USDJPY

**Source stance:** open-question

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala; PR 2790: Feat/SILVER-10779 multiccy monthly changes

**Source-preserving request, proposal, or question:**

> Can we rely on fxRate to take care of inverting the rate already? e.g. it’s EURUSD but USDJPY

**Evidence:** anon-2.jsonl:3571 · comment 269770314 · PR 2790 · 2021-12-28

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala`

## R-3572 — Nit: Can we rename these two as `prevMonthConvertedNav` and `currMonthConvertedNav`?

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala; PR 2790: Feat/SILVER-10779 multiccy monthly changes

**Source-preserving request, proposal, or question:**

> Nit: Can we rename these two as `prevMonthConvertedNav` and `currMonthConvertedNav`?

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3572 · comment 269770527 · PR 2790 · 2021-12-28

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MonthlyChangeGenerator.scala`

## R-3574 — Maybe we should sort here, instead of trusting the caller

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/MarketDataServiceImpl.scala; PR 2791: feat(marketdata):SILVER-11030 monthly changes IMPORT api

**Source-preserving request, proposal, or question:**

> Maybe we should sort here, instead of trusting the caller

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3574 · comment 269629853 · PR 2791 · 2021-12-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/MarketDataServiceImpl.scala`

## R-3583 — I think we should make this method returns the instrumentIds only - and let its caller invoke instrumentService. It will make it simpler to write test too.

**Source stance:** suggestion

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/StatementDataGenerator.scala; PR 2739: include instruments from transactions as well to build cache

**Source-preserving request, proposal, or question:**

> I think we should make this method returns the instrumentIds only - and let its caller invoke instrumentService. It will make it simpler to write test too. No need to mock

**Evidence:** anon-2.jsonl:3583 · comment 267447941 · PR 2739 · 2021-12-15

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/StatementDataGenerator.scala`

## R-3595 — I think I like iterator better :stuck_out_tongue:

**Source stance:** suggestion

**Context:**

> advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala; PR 2643: SILVER-10408: Minor rename/refactor ProductLine implementation to better express the design pattern. Implement ExistingGoalDetail for Income

**Source-preserving request, proposal, or question:**

> I think I like iterator better :stuck_out_tongue: 

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3595 · comment 264685663 · PR 2643 · 2021-12-02

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala`

## R-3610 — FX daily-price conversion separates missing prior rate from mapping outcome and uses HALF_EVEN scale 2

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessorForMultiCcy.scala; PR 2600: removes failing when fx rate is not present for instrument price calculation in another ccy

**Source-preserving request, proposal, or question:**

> Nit: This log doesn’t feel right, cuz now we club the case when fxRateToUse is None, and then case when `.map(fxRateToUse => { blah } `produces None. I know it’s not possible for that map to produce None, but still :stuck_out_tongue: 
> 
> ‌
> 
> Maybe like this is better?
> 
> ```
> convertedDailyPrices = sortedDailyPrices.flatMap { dailyPrice =>
>   fxRates
>     .filterNot(_._1.isAfter(dailyPrice.priceDate))
>     .sortBy(_._1.toEpochDay)
>     .lastOption match {
>       case None =>
>         log.error(s"unable to find the fx rate [$instrumentCcy|$targetCcy] for the date [${dailyPrice.priceDate}], skipping for the date")
>         None
> 
>       case Some(fxRateToUse) =>
>         val convertedPrice = (dailyPrice.value * fxRateToUse._2).setScale(2, RoundingMode.HALF_EVEN)
>         Some(DailyPrice(businessDate = dailyPrice.businessDate, priceDate = dailyPrice.priceDate, priceCcy = targetCcy, value = convertedPrice))
>     }
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3610 · comment 263760481 · PR 2600 · 2021-11-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessorForMultiCcy.scala`

