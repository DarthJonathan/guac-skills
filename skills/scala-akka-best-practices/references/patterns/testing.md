# Test contracts, fixtures, serialization matrices, and observed results

350 source-specific cases. Statements retain their historical scope and source stance. Read related PR cases for corrections or alternatives.

## Cases

- A1-0005 — Manual broker endpoints need settlement date support
- A1-0024 — Review-pattern comparison on first commit before and after update
- A1-0042 — Do not expose TradabilityRestrictionError val and assert exact error types
- A1-0052 — Verify actual errors and validationResult for every failure-notification test and add multiple failures
- A1-0227 — Instrument retrieval test already covers DB-only data without instrument-service mock
- A1-0262 — Add instrument retrieval V2 test for MIC conversion
- A1-0275 — Test-data fluent methods mix set and with naming
- A1-0313 — Test all two-cache interactions in InstrumentDailyPerformanceCache
- A1-0314 — Add metrics-cache-missing or evicted test
- A1-0317 — Verify calculateInstrumentDailyPerformanceBatch once and no more interactions
- A1-0318 — Verify getCachedInstrumentPerformancesMetrics returns without remote call
- A1-0319 — Change sampleMetricsDto returnEnd and verify refreshed metric data
- A1-0320 — Metric-only cache case differs from out-of-sync two-cache case
- A1-0321 — Use theSameElementsAs assertion
- A1-0322 — Do not remock unchanged behavior
- A1-0323 — Verify result2 has same data as result1
- A1-0485 — Update test name
- A1-0556 — Test B2B displayCcy update after FA enables auto-rebalance
- A1-0579 — Caller provides date via injectable DateTimeProvider
- A1-0623 — Test auto-retry with stitch false
- A1-0689 — Update HK email test date and decimal formatters
- A1-0816 — Add PortfolioRepositoryTest filter coverage
- A1-0817 — Test empty inSetBind returning false
- A1-0864 — Update InstrumentInfoDtoTest for derived standalone
- A1-0884 — Write fetched old data to separate file for per-entry comparison
- A1-0887 — Old writer only needs comparison data, not extra output
- A1-0931 — Option generic type check erased and gives false assurance
- A1-0932 — Only assert Some wildcard because generic type erased
- A1-0948 — simulateOnly should log merged result or return it without persistence
- A1-1238 — Extract slug helper for test without service setup
- A1-1239 — Expected slug should be literal or slugify helper, not production service logic
- A1-1240 — Translation allocation mocks should not be None
- A1-1243 — Test Scaffeine behavior in ScaffeineCacheSpec
- A1-1247 — Include requested Int in test key instead of ignoring it
- A1-1251 — Call cache twice explicitly in test
- A1-1252 — Test multiple variants fetched but only requested keys returned
- A1-1269 — All cash-only redemption usages verified for urgent release
- A1-1303 — Test derived area/perimeter JSON cannot influence deserialization
- A1-1358 — Revert translation-filter commit because tests unresolved
- A1-1380 — Take current date from dateTimeProvider
- A1-1409 — Test duplicate dates while range has both from and to
- A1-1419 — Add thorough approval identifier test scenarios
- A1-1528 — Voucher test fix reported ready for rebase
- A1-1575 — Test factual price exactly on common-start date
- A1-1633 — Unit tests plus dynamic manual tests across tenants
- A1-1655 — Eight services deployed to d38 and started; full E2E still planned
- A1-1691 — Removed-marketvalue-message test verifies nothing and still passes
- A1-1701 — Background reconciliation makes test flaky if return precedes completion
- A1-1714 — One region test enough if no region-specific behavior
- A1-1730 — Test throws NotFound synchronously instead of Future.failed
- A1-1765 — Hardcoded ExploreData list mapped by id must have no duplicates
- A1-1779 — Validate hardcoded Explore data in tests instead of runtime
- A1-1810 — Portfolio startup tested with no CPU limit and300m
- A1-1830 — Move client to bff-api test scope
- A1-1886 — Test access needs only private[managers]
- A1-1928 — Test empty priceSource entry
- A1-1940 — Test plus-one-hour crosses next date after11pm and query empties
- A1-1941 — succeed returns before inner future and leaks mock invocation into next test
- A1-1996 — Advisory-to-customer named exception gains CUSTOMER_DOES_NOT_EXIST
- A1-1997 — BFF instrument client error gains INVALID_DOCUMENT_ID
- A1-1998 — BFF unhandled instrument actor error becomes generic server response
- A1-2043 — Flaky Circle tests stopped before proposed AsyncWordSpec change merged
- A1-2044 — Custom operation-name interpreter cross-reference and full server/Kamon E2E test added
- A1-2045 — Operation-name change deployed SG/HK staging services successfully
- A1-2046 — Rebased split commit had empty diff and still worked staging
- A1-2074 — SG CoreEnhanced offering/summary performance starts Oct2020 liquid-alts inception
- A1-2076 — SG single-fund FundSmart displays factual but common w12m for risk
- A1-2077 — SG multifund liquid-alts custom display with common risk w12m
- A1-2078 — SG normal multifund uses common performance for display and risk
- A1-2079 — HK liquid-alts model uses custom; analysis custom display and common risk
- A1-2081 — customPeriodStartingMonth aligns factual/representative display matrix
- A1-2096 — Swagger authenticated lock versus public icon and JWT authorization verified
- A1-2097 — Swagger endpoint grouping/sorting verified
- A1-2098 — Swagger guards displayed correctly
- A1-2106 — Dividend distribution succeeds with confirmed holdings and double-unit file
- A1-2107 — Dividend distribution rejects assumedMV versus confirmedMV mismatch
- A1-2108 — Dividend reprocess rejects changed split amount before processing second plan
- A1-2109 — Delete/retry dividend: source DistributedCashBalance versus JSON DistributeCashBalance;19.28 each
- A1-2162 — Retest pending recurring task at submit even if workflowId supposedly protects
- A1-2186 — Unified BFF has no scheme/prefix in Swagger
- A1-2267 — Goal performance metrics tested d56; screenshot only
- A1-2297 — Assert total count when not checking every multicurrency entry
- A1-2299 — Cluster-sharding eager init works in test; prior cause unclear
- A1-2338 — Eager init reduces AskTimeout during restarts but coordinator deletion still causes some
- A1-2339 — All services started SG staging and smoke tests passed
- A1-2340 — CHINA_FI-to-FundSmart script: goal before, after, and ordered event relationships
- A1-2341 — CHINA_FI-to-FundSmart script: rebalance before, after, and ordered event relationships
- A1-2342 — CHINA_FI-to-FundSmart script: trading before, after, and ordered event relationships
- A1-2343 — CHINA_FI-to-FundSmart script: charge before, after, and ordered event relationships
- A1-2397 — Add employee document and task ownership guard unit tests
- A2-0041 — SgB2bRedemptionCommunicationManager: There’s no A&B in advisor portal? At least not without a ref to specific customerId?
- A2-0054 — SgWorkflowEngineE4s: Confirm that this should assigneeRole, and it should be optional. For our use case, we dont want to specify assigneeRole
- A2-0056 — Review: `advisory` currently already validates the input fees in both investment-summary & validation behaviours. So adding this extra logic in `charge` feels a bit redundant, e...
- A2-0093 — InstrumentTransferHelper: Existing code would match by specified brokerAccountId too.
- A2-0095 — InstrumentTransferService: Do we need to specify brokerAccountId in this cmd? Since it’s possible to have multiple broker accounts?
- A2-0104 — package: We cannot use DTO, especially other services' DTO in our domain event. It can feel clumsy at times, but always better and safer to redefine the model.
- A2-0107 — BaseServiceLogicImpl: Take context in request payload as well. No need to make this endpoint specific for invest once
- A2-0117 — SgComplianceChecker: Unfortunately tenant service is not deployed in prod/staging yet. So we will need to make this dependent on env in order to not break existing flow
- A2-0200 — InitiateCancellationFlowCmdHandler: This `INVALID_CANCEL_ATTEMPT` is mapped to NotFound right now. It seems not used, so maybe change it to BadRequest instead?
- A2-0209 — BffServiceE4s: `withAccessControl` is extension method of `AuthenticatedEndpoint`. When we reuse existing BE endpoint, we can wrap them with `authenticated`, and optionally add ...
- A2-0232 — GuardsTest: Same for this one
- A2-0233 — GuardsTest: Can we break this test into 2, one with `managerId = None` and another with `managerId = Some(random)`
- A2-0260 — Authorizer: [person] I’m trying to make the test works, but I swap the 2 logs here, it seems it was a typo. We don’t want error log on EFFECT\_DENY, and we want error log if the...
- A2-0279 — PlanFeeInstructionEvents: It’s easier to track & inspect if the event capture the individual change \(potentially with context, e.g. requestedBy/reason\), rather than updating w...
- A2-0299 — Review: Reported config-endpoint verification: cassandra-query-journal/events-by-tag/eventual-consistency-delay returned 20s before the environment override and 7s afterward. Po...
- A2-0305 — package: Maybe we make specific event for this. This `InvestmentPlanUpdatedEvt` is very generic. This event supposed to not introduce any change, while `InvestmentPlanUpdatedEvt...
- A2-0371 — InstrumentBalanceRepository: ```
- A2-0375 — package: Let’s include the `SubscriptionAmountRegulation` fields too? I suppose that would be useful information, especially if we anticipate the FA will use at least our liquid...
- A2-0397 — BaseAdvisoryServiceE4s: Similar to the fund selection APIs, we can group these into
- A2-0399 — BaseAdvisoryServiceE4s: Ok nvm about proxy endpoint with customerId/employeeId context propagation for now. In theory, it is possible to set them onto TracingContext, but will n...
- A2-0400 — SgFundDetailsManager: Let’s structure these as
- A2-0414 — BaseAdvisoryServiceE4s: Should we create another API object for all these tenant specific endpoints? Their logic should extract the tenant from tracing context, and use it for c...
- A2-0419 — TenantAwareInstrumentBuilderTest: Maybe add option to set these providers in `SgAdvisoryServiceMockUtils#getService` instead of casting like this
- A2-0422 — TenantAwareInstrumentBuilderTest: Let’s add another test for SRS or CPF. That would have failed with this PR
- A2-0425 — SgInstrumentFilterManager: The logic in this manager is not SG specific AFAICS. Better we move it out to `managers` package instead of `managers.sg`
- A2-0430 — TenantAwareInstrumentBuilder: Only need customerService as we are overriding its type to SG, otherwise we don’t need to specify these ruleService/instrumentCaches again
- A2-0432 — TenantAwareInstrumentBuilderTest: I was thinking to provide easier way to override this when we create the `*ServiceLogicImpl` instead of forced changing it like this.
- A2-0469 — BffServiceImpl: In on-behalf operations:
- A2-0472 — Guards: The intention is since we will have the endpoints specifically for each FE application, these guards are there to allow us to validate correct endpoint is called \(espec...
- A2-0479 — Review: Tested e2e flow bff swagger → bff → advisory and verified the contexts are propagated correct [<url> data-inline-card='' } 
- A2-0490 — InstrumentInfoData: Also can we make one instrument having 3 asset class types, instead of both having 2 same types
- A2-0492 — InstrumentInfoData: Can add dependency `` `instrument-api` % "test->test"``, and use `InstrumentV2TestData` instead
- A2-0493 — InstrumentV2TestData: Let’s keep this very simple, and add `withAssetClassAllocation` in `InstrumentV2TestDataExt` instead
- A2-0494 — SgAdvisedPortfolioOfferingsManager: After you’re done with e2e testing, let’s put a cache here, similar to `AdvisedPortfolioPerformanceCache`
- A2-0512 — SgPlanUpsertPortfolioSummaryBehaviourTest: check not empty instead?
- A2-0534 — HkFeeManagerEntityTest: We don’t need this test cuz there is no split logic at entity level?
- A2-0537 — HkFeeManagerEntityTest: There is no logical change in the entity/cmd handler. It’s better to have the waiver bit injected, and keep the existing test in tact. Then you can unit ...
- A2-0542 — HkEstimateFeeGoalModifyBehaviourTest: This test was expecting to return tier 2 of 0.0035…. so either we update the test name to “ranked fee 3”, or we update the existing MV so t...
- A2-0553 — ProductPortfolioHelper: We should log `specified style` instead of `specified risk tolerance` here
- A2-0567 — GoalCreateBehaviourHelpers: Ok to throw for now. We can either make this specific to B2C, or make it generic and default some values for B2B
- A2-0568 — productline: All of these private conversion should be specific type
- A2-0570 — package: Maybe we don’t add this yet, cuz as of now, we would only return the specific B2B/B2C type to FE \(since they have separate apps\)
- A2-0599 — BaseBffServiceImplCorsTest: Oops I missed this. Can you help me fix in this PR too, just need to explicitly set it for the test
- A2-0613 — Review: Local testing
- A2-0614 — Review: D56 testing
- A2-0626 — AkkaHttpAuthRecipesTest: Which executionContext is this? We should probably use the one from AsyncWordSpec right?
- A2-0627 — GuardsTest: This should be enough
- A2-0674 — deploy_config: Actually I’m not sure why we need this requires… why does deployment to dev needs to be after deployment to staging? Isn’t it backward?
- A2-0683 — D56 CORS matrix: valid/local origins, rejected origins, and no Origin header
- A2-0712 — PortfolioMonthlyChangesHelper: 1. Let’s not persist dummy values \(empty or last value\) on failure
- A2-0730 — InstrumentMonthlyChangesJdbcRepository: Move filter up, and select specific columns
- A2-0783 — SgRecommendedInvestmentManager: Best if we can refactor to avoid make unnecessary calls
- A2-0785 — SgRecommendedInvestmentManagerTest: These brackets are extra here, causing all the below tests to be outside of `"getRecommendedInvestmentAmount" should {`
- A2-0818 — ServiceClientExceptionSerializerTest: Let’s add a positive test too?
- A2-0819 — application: This should be moved to `test/resources`
- A2-0820 — ServiceClientExceptionSerializerTest: Shouldn’t it be `implicit val system: ActorSystem`
- A2-0836 — CustomerStatusHelper: Can we make this change for HK too
- A2-0851 — Terms: Since all non-alts product use same terms for this, let’s just name this group `InvestmentAlignmentTerms` I think, i.e. we don’t have product specific terms like FlagshipDpm
- A2-0857 — build: Let’s add `% Test`?
- A2-0865 — PerformanceCalculatorTest: Let’s also assert on the peak and trough’s yearmonth at least
- A2-0866 — PerformanceCalculatorTest: `performanceMetrics1` already covers the case when peak->trough is the first drop, let’s make this case returning 2nd drop
- A2-0877 — PerformanceCalculator: Prev condition is `count < 2`, so this should just be `case Nil | _ :: Nil`. Actually we should add a test case with just 2 mc as well
- A2-0878 — PerformanceCalculator: No no I mean there’s no tests for exactly 2 mc - which would have failed. There is only tests for 1 mc and >=3 mc as of now
- A2-0889 — HkServiceLogicImpl: Looking at `StatementDataGenerator.createStatementDataAndGeneratePdf`, looks like it’s better to use `statementPeriod = END_OF_MONTH` and `monthPeriod = Some...
- A2-0908 — Review: Can you help to test a few cases, just in case…
- A2-0953 — package: This should be a List, so that IO/Product can control the ordering. And we will need another field to specify which benchmark to highlight
- A2-1024 — CorporateProductRuleInterpreterTest: Let’s add more tests to verify multiple `SpecificInstrumentAccessRule` can compose correctly
- A2-1025 — CorporateProfile: Let’s add tests for this `CorporateProfile.validate` method.
- A2-1044 — PlanCommunicationV2EventProcessor: [person] [person] Unlike emails, if customer changes preferred language, the existing platform notifications would have to switch display acco...
- A2-1045 — PlanCommunicationV2EventProcessor: In anticipation for more custom interpolations in future, we can change this a little to below \(similar to locale specific one\)
- A2-1059 — PageDataGenerator: Actually we have too many region pattern matching in this method. Maybe consolidate it a bit
- A2-1061 — GoalBasedStatementInfoDbDto: Yea so I think adding these new fields to `*DbDto` can cause confusion for existing data if we don’t retrospectively update them.
- A2-1062 — StatementPdfGeneratorTest: I suppose this assertion at best can only verify the html templates don’t throw error, and that some pdf file is generated.
- A2-1064 — package: [person] after checking the usage of this class again, I’m convinced that
- A2-1069 — Review: Without the mock timeout header, Route tests' log would be flooded with these WARN entries from `TimeoutDirectives`
- A2-1072 — InvestmentCommunicationV2EventProcessor: Hmm this assumes the “problems” are specific to plan account is it? I guess we can revisit these templates again….
- A2-1080 — DpmStatusLogic: [person] [person] this kind of validation in logic \+ blind update in entity is actually not safe against race condition / concurrent modification. Specialized c...
- A2-1092 — HkGoalCreateValidationBehaviour: Can we add test to capture this case please
- A2-1100 — Review: Did we test recurring investment flow in staging this time?
- A2-1126 — DetectUpcomingRecurringInvestmentCmdHandler: Does this amount needs to be “correct” amount here? Maybe just make it as deprecated, and only use if old events
- A2-1136 — CassandraProjectionManager: Due to this issue, currently all of these spans completes almost instantly \(~0.005s as per current metrics in both prod and staging env\)
- A2-1171 — Review: Tested in SG staging with `charge` svc
- A2-1189 — BaseInvestmentCommunicationEventProcessor: This doesn’t look like it’s specific about direct debit isn’t it?
- A2-1202 — HttpServerStartup: Oh we definitely want to set `rejectionHandler` for all services, especially when we extract this to common code. And in order to use a custom rejection handl...
- A2-1210 — ThresholdBreachedRebalanceRestrictionSpec: permitted
- A2-1211 — ThresholdBreachedRebalanceRestrictionSpec: Can we also add more tests that:
- A2-1221 — ThresholdBreachedRebalanceRestrictionSpec: Not matching scenario description
- A2-1228 — ComplianceHelper: This we can remove, and just `RegionSpecific` for impl
- A2-1240 — package: No need to say `PlanAccount` again I think. How about these names?
- A2-1243 — package: [person] I’m ok with this too :see_no_evil: 
- A2-1261 — HkGoalCreateSimulationSummaryBehaviour: This method should be generic to support all types of portfolioId-specific request \(as opposed to TAA-specific request for FundSmart\)
- A2-1307 — Wrongly deleted fee-redemption recovery: first order stays deleted, second assumption restores, confirmations complete
- A2-1310 — D56 abort rejected withdrawal dividend: 187.44 switches to cash balance; 12.56 reinvestment remains unchanged
- A2-1317 — SgTradabilityCheckerTest: Can we rename these 2 methods, maybe initGoal vs initPlan?
- A2-1345 — package: Many fields of same type next to each other makes this very easy to mess sth up during refactoring if we are not careful. Let’s just use this syntax instead
- A2-1354 — package: Let’s support specific instrumentIds too, so that we can run for a few for adhoc check purpose
- A2-1359 — MarketDataUploader: I think no need to log this, or just debug for testing. This will generate a lot of logs we don’t need
- A2-1372 — MarketDataUploaderTest: Hmm both of tests are not really asserting anything, cuz the logic can only be observed via logs.
- A2-1392 — GoalModificationRestrictionSpec: blocked
- A2-1393 — GoalModificationWithPortfolioSimulationRestrictionSpec: Can we split the test cases, similar to `GoalCreationFromPortfolioSimulationRestrictionSpec` and `GoalCreationFromPortfol...
- A2-1395 — GoalModificationWithPortfolioSimulationRestrictionDpmSpec: Feels like lots of duplicated tests in here, while missing some other cases specific to DPM
- A2-1396 — GoalModificationWithPortfolioSimulationRestrictionDpmSpec: ineligible
- A2-1470 — PlanUpsertSimulationRestrictionSpec: This doesnt seem to match the test. Expired CRA? But the setup is valid conservative
- A2-1471 — HkServiceLogicMockUtils: Did you mean to use FlagshipDpm? Otherwise maybe default to FundSmart?
- A2-1472 — GoalCreationFromPortfolioSimulationRestrictionSpec: goal creation from portfolio
- A2-1473 — GoalCreationFromPortfolioSimulationRestrictionSpec: I’m thinking this test is quite big. Should we consider split into 2 files?
- A2-1477 — GoalCreationFromPortfolioSimulationRestrictionDpmSpec: Let’s add blocked-on-CAT2 here. Also permitted-for-complex-aggressive
- A2-1478 — PlanUpsertSimulationRestrictionSpec: Ok let’s update the scenario description then..
- A2-1479 — GoalCreationFromPortfolioSimulationRestrictionDpmSpec: This riskTolerance should be low value to prove that we skip aggressive-complex check right? i.e. if you flip `isDiscretio...
- A2-1481 — GoalCreationRestrictionSpec: Is this same as 
- A2-1502 — UpdateTradeFxConversionRequestIdCmdHandler: Are you planning to use same cmd handler for future cases of `fundingInstructions`?
- A2-1524 — SgGoalCreateValidationBehaviour: [person] I asked [person] to call `getAdvisoryQuestionnaire` again here and cross check that specified response from FE is actually one of the r...
- A2-1530 — SgGoalCreateSummaryBehaviour: I think this one doesn’t have to be productline, cuz it’s very specific to single fund FundSmart. Maybe just put a simple helper trait and extends ...
- A2-1533 — FundSmartHelper: fee <- `estimateAccessFee`
- A2-1558 — FxWalletQuotationServiceImplSpec: It’s more about scaffeine behaviour, but I think it’s useful to capture this in a test
- A2-1574 — D56 redemption threshold tests: 97% full flag and 10% MV tolerance; final example has inconsistent request flag
- A2-1580 — RebateDistributionRequestJdbcRepositoryTest: Is it duplicate test? It’s not mockDb btw, it’s real embedded pg
- A2-1581 — RebateDistributionCommunicationsManagerTest: I haven’t figured out exactly why yet, but this extra whitespace here gonna mess with the test run
- A2-1582 — RebateDistributionCommunicationsManagerTest: I’m not sure about this test, cuz this in fact would trigger the `require` guard to fail.
- A2-1590 — package: As in we should only serdes the individual case class via the trait `FundingInstructionsDto` only. No one should serdes `SpecifiedAccountFundingInstructionsDto` directl...
- A2-1641 — AdvisoryDataTranslationManagerSpec: We prefer to keep the fake translated value, e.g. `Translated Template Description` so that tests are readable. Translation is actually just ...
- A2-1643 — UpdateTemplateDisplayName: You can do sth like this
- A2-1660 — enums: Maybe ask [person] and [person], but if unsure, I’d name them closer to the specs, e.g. TransactionClassification or sth.. at least people have been discussing about clas...
- A2-1668 — AdvisoryServiceE4s: Don’t use this one. Locale has special formatter, so we want to use the implicit one in `ParameterSerializersE4s`
- A2-1676 — AdvisoryDataTranslationManagerSpec: Maybe put the one needed for the test only. Now that we have the cache to mock, for readability, maybe use English instead :rofl: 
- A2-1679 — RedemptionRequestTopicSubscriberV3: Let’s make this specific to fee redemption only, and move the `request.feeChargeDetails.isDefined` to require clause
- A2-1682 — RedemptionRequestTopicSubscriberV3: Right, sorry I missed that… somehow I thought we only call only for fee \(and hence even suggest making it specific with require clause :see_...
- A2-1697 — BaseRedemptionCommunicationV2Projection: [person] can you check with [person] on how this TAA field is used? Feels very wasteful to lookup portfolio service here, while `planDto...
- A2-1708 — CustomerMigrationProcessorTest: Below we call plusDays\(2\) and plusDays\(3\) make 28Dec onwards crossing to next year
- A2-1715 — AuroraJdbcSchema: Ah yes, creating them as empty is ok. My previous comment was in context of either the repository or the dbHandler having injected database.
- A2-1733 — SgFundSmartManagerV3: Yeah `performanceMap` already contains only that specific period type \(if any\)
- A2-1756 — ServiceLogicImpl: Existing impl doesn’t require ccy. If not specified, use default ccy of marketdata. Maybe we use the ccy of returned monthly changes instead to follow previous...
- A2-1769 — CalculationMatrix: Ah ok, for alts we still need a specifc impl, cuz we need score \+ aggressive answer flag
- A3-0013 — InstrumentServiceImplTest.scala: We have replacement for these tests in v2 already right?
- A3-0026 — InstrumentV2JdbcDbHandler.scala: We don’t really need transaction for readside so we can inject db here, and return Future… it’s easier to use and mock in test if needed
- A3-0048 — Compliance retry test: trust FutureUtils or override backoff for short unit tests
- A3-0058 — DividendTopicSubscriberV3.scala: The problem with this is it’s a bit harder to unit test just the logic, cuz you will need to mock the topic.subscriber chain We can potentially add a 
- A3-0064 — DividendTopicSubscriberV3.scala: but you will need to mock the whole chain… doable but just boiler plate ``` dividendService .dividendTopic .subscribe .withGroupId(groupId) .atLeastOn
- A3-0077 — InstrumentV2EntityTest.scala: add a test case to cover that we merge/override existing map correctly with data from request for these update idMap/urlMap
- A3-0078 — InstrumentV2EntityTest.scala: I don’t know exactly why yet, just these whitespace can cause the test not running if you try to run it individually
- A3-0079 — InstrumentDataUpdateManagerV2Test.scala: We don’t need to keep recreating these every test right?
- A3-0096 — d56 RPC verification: goal modification, threshold breach, acceptance and race outcomes
- A3-0103 — TransactionTypes.scala: Can we add tests for this too :pray:
- A3-0147 — : Examples from d56 * `HARRYSFRIEND` is absolute percentage, applicable for all accounts * `HARRYCHEAP` is $10 fixed amount for SGD cash only \(fully ut
- A3-0151 — : Updated simplified response model ``` { "planFees": [ { "customerId": "", "goalId": "", "planId": "", "tradingAccountType": "SINGAPORE_CPF_OA_ACCOUNT"
- A3-0187 — CustomerTransactionMigrationEventProcessor.scala: I guess if you already dry run everything, then maybe it’s ok
- A3-0218 — Lagom/removed-Lagom error-serdes, shared breaker, whitelist and request-timeout verification matrix
- A3-0221 — InstrumentDailyReturnIndexDaoJdbc.scala: Change this so that we actually test the clause limit in test
- A3-0222 — randomizeLocalDate within10years clashes make clause-limit test flaky
- A3-0251 — BaseChargePgTest.scala: I default to Sg for now, cuz all our tests are for SG. In here, multiple methods we also use Sg classes directly
- A3-0252 — TwilioSvcManagerV2.scala: cover all these cases in `TwilioSvcManagerV2Spec` otherwise it’s impossible to remember all these combinations in SG vs HK
- A3-0259 — : Can we add tests too please, for both processor and repository
- A3-0280 — RegionalDataTest.scala: just assert on this field instead of printing and succeeded
- A3-0283 — SgRegionalData singleton SilverRegion.Sg.type makes wrong-region construction compile-time safe
- A3-0300 — PlanCommunicationV2EventProcessorTest.scala: Can we put exact expected string these? Otherwise we’re just repeating the impl but not testing the values. Let’s also cover at least weekly/biweekly 
- A3-0301 — PlanCommunicationV2EventProcessorTest.scala: Or have separate unit test for `RecurringInvestmentFrequencyDetailUtil` that cover more cases
- A3-0304 — RecurringInvestmentFrequencyDetailUtilTest.scala: No future so you can just use AnyWordSpec
- A3-0385 — InvestmentScheduleActivePeriod.scala: I’m surprised this works in your testing as `recurringInterval` is an option….
- A3-0404 — TransactionQueryLogic.scala: HK Web query all and then filter in FE. This was spotted in e2e tests
- A3-0431 — : WIP: * tested the backfill endpoint itself → works * pending: * wait for new version of readside → update query to filter * in prod it’s huge amount o
- A3-0463 — StatementDataGenerator.scala: We would need to remove the absorbed tax details at transaction level in this method `calculateIfSameStatementDataExists` to avoid reprinting old stat
- A3-0491 — RebalanceMsgLogicImpl.scala: Also let’s capture this logic in test
- A3-0493 — RebalanceMsgLogicImpl.scala: And let’s capture this behaviour in tests, if not already there
- A3-0502 — RebalancePlanEntityTest.scala: check exactly new new TAA matches what provided in cmd? Also let’s verify the emitted events contain only the TAA updated evt, and nothing else. Do yo
- A3-0505 — d56 fee-withdrawal deletion test: error-before,200-after, reservation/events/DELETED checks
- A3-0506 — : The cash balance is a bit messed up due to testing in d56, but it did try to recalculate the balance. The warning in transaction svc about missing fee
- A3-0520 — SgServiceLogicImpl.scala: I’ll test this backfilling logic a bit with existing fee charge request in d56, then will drop this nested field
- A3-0523 — SgTaxCalculator.scala: This is tested as part of the SgFeeManagerProjectionSpec and BackfillAbsorbedTaxDetailsLogicSpec.
- A3-0575 — InvestmentPlanEntityTest.scala: please name this test
- A3-0576 — Alts cashOnlyFee test:1.5M holding,10K pending,5K cash,12381.46 fee waits for funding
- A3-0577 — CashSmartUSD cashOnlyFee=false test:173.74 fee eagerly reserves cash and completes
- A3-0578 — 15K top-up funds Alts fee before earlier investment;12381.46 fee completes
- A3-0600 — BrokerAccountTopicSubscriberTest.scala: Name should `BrokerAccountTopicSubscriberCommunicationLogic`Test/Spec
- A3-0625 — Alts/non-Alts/SRS fee tiers stay separate when Alts goal added
- A3-0626 — : ## Fee estimate in goal creation Alts MV does not interfere with non-Alts * 5000 amt → same tier → 0.005 * 500000 amt → cross to next tier → 0.0035 If
- A3-0627 — : ## Charge for Alts ``` POST <url> { "year": 2023, "quarter": "Q1", "reason": "QUARTERLY_SCHEDULED_FEE_CHARGE", "simulateOnly": true } ``` ### Explicit
- A3-0628 — : ## Charge for non-Alts ``` POST <url> { "year": 2023, "quarter": "Q1", "reason": "QUARTERLY_SCHEDULED_FEE_CHARGE" } ``` Fee charge request * Fee amt r
- A3-0629 — : Tested triggering charge via admin too. The service queries and start the charge process for all applicable plans
- A3-0631 — : Tested in d34. ### Invest manually with one instrument in an existing plan with 2 instruments 50-50 After investment settles, MV is updated and thresh
- A3-0632 — : Trigger the endpoint to accept all threshold breach requests And settle the rebalance trade ``` { "rebalanceRequestId": "", "status": "REBALANCING_COM
- A3-0633 — : Retested the advised template after correcting the datetime formatter \+ latest template being active [<url> data-inline-card='' } ![](<url>
- A3-0638 — EmailDataFactory.scala: makes sense. I realized this when testing for rebalance communication too. I ported the same into FormatterUtils
- A3-0659 — : Triggered in d56 \(many instruments would have missing DistributionStatus, but that’s ok\) ![](<url>
- A3-0693 — : Reprocess already-processed distribution with same file name will error ![](<url>
- A3-0694 — : Reprocess already-processed distribution with different file name and no force flag will also error ![](<url> ![](<url>
- A3-0695 — : Reprocess already-processed distribution with different file name and force flag will go thru \(assuming POps knows what they are doing\) ![](<url> Sa
- A3-0705 — PreRpcValidation.scala: Ah yeah I just need to sort based on something so that the ordering is same when I run multiple times
- A3-0727 — services.list: Not sure but definitely didn’t work in d34 :sweat_drops:
- A3-0734 — SellOrderGeneratorTest.scala: This is the new test. The rest is just moving the code to companion object
- A3-0803 — SftpMetadataChecker.scala: Why don’t we just diff always, in case the count is same but ids mismatch?
- A3-0805 — SftpMetadataChecker.scala: it’s good to separate these 2 list * One is missing in metadata file but pdf exists → less critical, can be checked if customer is deactivated etc * O
- A3-0834 — : can we put unit test for serdes to make sure the default logic is doing what we expect it to do? Especially if someone explicitly set the field to nul
- A3-0835 — : the test, if any, is more like a feature discovery of play json serdes haha. I guess so far we didn’t think about this as we expect no one would send 
- A3-0885 — : You’ll need services.list… I suppose you’ll need to test this in some of the dynamic env too
- A3-0921 — CraManagerTest.scala: assert `vcStateChangeDailyTriggerTopicProducerDirect` not called?
- A3-0973 — TransactionJdbcRepositoryV2Test.scala: We typically keep these in companion object. You can extend it with `TestData` which provides some handy helpers to randomize data. Essentially, we ju
- A3-0974 — TransactionJdbcRepositoryV2Test.scala: Good idea to truncate the table at the end. Save yourself some head scratching when you add the next test
- A3-0993 — : can we also make sure the subscriber for new model doesn’t have the same bug? Then we can add services.list and release :thumbsup:
- A3-1002 — StateUpdatedSpec.scala: This will be in UTC. Depending on when the test runs, it might be flaky
- A3-1012 — Error-contract tests: missing CRA, concurrent invest retry, instrument-down propagation
- A3-1023 — RedeemOnceEdgeLogic.scala: Can we add test for these cases? * unit-based request should use the provided units as is * amount-based request should calculate and call the BE API 
- A3-1054 — TransactionEntityTest.scala: Can just new `SingaporeDateTimeProvider` I think.. we don’t need to control time in this test right?
- A3-1055 — TransactionEntityTest.scala: ok but this is as good as just use the real provider right? :stuck_out_tongue: ``` val date = ZonedDateTime.now() when(dtp.now).thenReturn(date) ```
- A3-1167 — ConcentrationRiskValidator.scala: Yeah, either works I guess. We didn’t throw here, so we still can test the CR validation logic without locking down earmark prematurely.
- A3-1212 — RecurringInvestmentRestrictionSpec.scala: Can we add a test case that fails CR for this flow?
- A3-1216 — CPF investor mismatch rejected at goal admission before compliance after fix
- A3-1228 — LocalConfig.scala: Added for testing in d34 only. Will remove after region split
- A3-1240 — HkServiceLogicMockUtils.scala: Ok for test code, but a NIT still: it’s easier to follow if we assign val for `craResponse` based on the logic. I inline it previously because there w
- A3-1245 — GoalCreationRestrictionSpec.scala: The GWT blocks are free text, and needs to be updated manually if anything is change - they are bounded to glue code, like Cucumber
- A3-1257 — ReleaseEarmarkSpec.scala: Should we add another assertion checking the earmark state? Otherwise, we would always get a Done as result - whether the earmark is found or not
- A3-1258 — Earmark-release e2e: simulate failure, release, simulate success
- A3-1259 — ReleaseEarmarkSpec.scala: it’s up to us really. The e2e test is really to do scenario testing, so I don’t think it’s too big - the test should run fairly fast anyway.
- A3-1276 — Json.format still requires acknowledgements array; WithDefaultValues is discouraged here
- A3-1308 — CustomerTradingEarmarkEntityTest.scala: I think test is a bit clearer if we do this step 1 as state setup instead. Can use `withCustomizedEntitySetup`
- A3-1310 — GoalCreationRestrictionSpec.scala: Just curious why we need this setup if customer is VC? I know skipping setup because we know it won’t be checked is a little white-box… but I purposel
- A3-1311 — GoalCreationRestrictionSpec.scala: The comments don’t seem to fit the actual setup? 0.1 of TLNW is not “large”?
- A3-1344 — TransactionTypes.scala: Can we add a simple json serialization test to ensure that serdes would work? E.g. create an instance of `DepositTransactionDto` and see if the json m
- A3-1383 — application.conf: this was to test the config update only that should only change the last layer. I’ll remove the circleci config.yml hacks too
- A3-1384 — d10 Docker layer/label/env/build-info smoke verification
- A3-1391 — EstimateAccessFeeGoalCreateBehaviourTest.scala: Can we add case for single fund \+ CMA goal? Similarly, single fund \+ CPF/SRS
- A3-1392 — EstimateFeeGoalModifyBehaviourTest.scala: Should we add another goal here, to ensure that the rank is checked across all cash plans?
- R-3337 — safeRenewProjectionForCustomer is started with a value binding and not awaited
- R-3341 — Yeah it works… I probably should have added the test cases… But I did test it with these, and it works.. No comments about looking odd though :grimacing: `
- R-3367 — Withdrawn EXPLAIN result for instrument_holdings_v1 SUM/MIN join
- R-3368 — Historical allocation/time comparison: in-memory versus DB holding aggregation at parallelism 4
- R-3369 — Corrected holdings EXPLAIN uses two roughly seven-second parallel sequential scans
- R-3370 — Holdings index use differs between all-plan grouped and specific-plan queries
- R-3371 — October and January date ranges lead PostgreSQL to choose different scan plans
- R-3374 — Oops my bad: * Red and green box is approach in [<url> data-inline-card='' } , triggered with fromDate = 2021-10-01 \(not so much holding data\) and 2021-0
- R-3387 — Transaction override simulation returns diff without changing state or persisting events
- R-3388 — Real transaction override changes state and persists CustomerTransactionOverriddenEvt
- R-3389 — Override rejects identical state and missing customer/transaction with distinct errors
- R-3392 — Updated expectedExistingTransaction/targetTransaction request and stale-state BadRequest
- R-3400 — I guess you mean to remove this empty test?
- R-3414 — Trigger `POST /api/v2/report/monthly-statements` for 2022-03 in Staging [<url> ~16K active customers and ~11.5K sftp upload task, all completed in ~1.25hrs
- R-3415 — Delete the directory in SFTP server, and trigger `POST /api/v1/report/upload-document-sftp` for 2022-03 in Staging [<url> ‌ Result is consistent with previ
- R-3416 — Example of hard failure cannot be cured with retry ``` c.l.l.s.a.t.TransportException: com.lightbend.lagom.scaladsl.persistence.PersistentEntity$InvalidCom
- R-3417 — Example of transient failure that was retried automatically ``` java.io.IOException: Connection reset by peer ``` ![](<url> ‌
- R-3418 — Report service was healthy in terms heap / gc / container’s memory utilization [<url> ![](<url> ‌
- R-3458 — ```shell > echo "feat/SILVER-12505-multi-ccy-bugbe-simulation-" | sed 's/[^a-zA-Z0-9]/-/g' | cut -c -63 | sed 's/-$//' feat-SILVER-12505-multi-ccy-bugbe-si
- R-3459 — ```shell > echo "feat/---" | sed 's/[^a-zA-Z0-9]/-/g' | cut -c -63 | sed 's/-*$//' feat > echo "feat/SILVER-12505-multi-ccy-bugbe-simulation-@-?----" | sed
- R-3463 — Dummy task to test serdes if we publish multiple tasks to the topic
- R-3484 — Tested this change with marketdata \+ instrument service in dev - both work fine. This PR doesn’t improve any speed, just move back to using non-root user,
- R-3485 — Tested with gateway too. It comes up alright and dev env is functional
- R-3486 — Tested `document` service in dev too. Able to create new customer \+ upload some documents \+ view them in adminUI.
- R-3504 — Goal modify summary has soft validation; confirmation has hard validation under the FE contract
- R-3514 — Deployed to `staging` together with actual Factors changes. Created new goal / modified goal / invested new funding source, and observe no serdes error \(r
- R-3515 — Historical question about TestContainers versus EmbeddedPostgres and in-memory tests
- R-3517 — Added `Deleted` to the cases in `deleteRelatedTransaction` I see `DeleteCmd` is already handled correctly by the entity if in `Deleted` state
- R-3529 — I’m not what’s wrong, but after I switch to use random, the test becomes flaky. I will raise separate PR to follow up on this later, if that’s ok :pray:
- R-3534 — Yeah it’s weird. If I revert, the test consistently passing. If I use random, it’s very flaky - fail very frequently locally
- R-3583 — I think we should make this method returns the instrumentIds only - and let its caller invoke instrumentService. It will make it simpler to write test too.
- R-3587 — Goal modify futures are constructed sequentially and tested as three dependent steps
- R-3594 — As chatted, I’ll check how we can write svcImplTest with real entity \(and hopefully without too much saga about mock entity > test driver > real entity :f
- R-3595 — I think I like iterator better :stuck_out_tongue:
- R-3596 — This is a dump from Technology satellite portfolio with a few manual edits. Will sync again after we have the Income portfolio created in Staging. ‌ Also w
- R-3597 — I generally prefer e2e tests over mock tests… but haven’t figured out how to write them effectively yet. The below seems to be the pattern we follow in oth
- R-3603 — Yes it’s a dump \(from Satellite - Technology\) for now, since I don’t care about its content. Will review once we impl goal create/modify - hopefully can 
- R-3604 — ServiceImplTest mocks client boundaries; EntityTest checks command, state, events and response
- R-3605 — Historical e2e exploration from ServiceImpl avoids committing to flaky EmbeddedCassandra

## Full source cases

## A1-0005 — Manual broker endpoints need settlement date support

**Source stance:** open-question

**Context:**

> component: broker-impl/src/main/scala/com/endowus/silver/broker/impl/logic/service/BaseBrokerServiceLogicImpl.scala; operation: [INV-5640] feat(broker, trading, investment, transaction): add settlement date; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Missing support would make testing troublesome

**Source-preserving request, proposal, or question:**

> Don’t we need to add support for this field in these manual endpoints? Otherwise it would be troublesome to test?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:5 · comment 823459463 · PR 13813 · 2026-07-08

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/logic/service/BaseBrokerServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5640] feat(broker, trading, investment, transaction): add settlement date

## A1-0024 — Review-pattern comparison on first commit before and after update

**Source stance:** reported-verification

**Context:**

> component: None; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> When reviewing the 1st commit alone:
> 
> ‌
> 
> Before the updated review patterns:
> 
> * wrongly flag not-switch repositories
> * didn’t not flag the event replay risk for history projection
> […incidental material or intervening source omitted…]
> ‌
> 
> After the updated review patterns \(tested 2 times\):

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Before text reports wrongly flagged not-switch repositories and literal double-negative replay-risk wording; after tested twice shown only in unavailable screenshots, so no textual success outcome inferred.

**Evidence:** anon-1.jsonl:26 · comment 823348080 · PR 14228 · 2026-07-08

> When reviewing the 1st commit alone:
> 
> ‌
> 
> Before the updated review patterns:
> 
> * wrongly flag not-switch repositories
> * didn’t not flag the event replay risk for history projection

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:26 · comment 823348080 · PR 14228 · 2026-07-08

> ‌
> 
> After the updated review patterns \(tested 2 times\):

## A1-0042 — Do not expose TradabilityRestrictionError val and assert exact error types

**Source stance:** requested-change

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/TradabilityRestrictionError.scala; operation: [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Types give better assertions than message strings

**Source-preserving request, proposal, or question:**

> Let’s not expose val unless we need to.
> 
> For assertion in test, now it’s much better to verify by exact type instead of strings

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:44 · comment 822521924 · PR 14066 · 2026-07-07

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/TradabilityRestrictionError.scala`

**Explicit source context (pr_title):**

> [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification

## A1-0052 — Verify actual errors and validationResult for every failure-notification test and add multiple failures

**Source stance:** requested-change

**Context:**

> component: investment-impl/src/test/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessorTest.scala; operation: [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Existing tests use any() and cover only single failures

**Source-preserving request, proposal, or question:**

> Can we make sure to verify these calls with actual expected values for the errors/validationResult instead of `any()`
> 
> Add this verify for every test that should involve sending failure to customer.
> 
> Also add test case that involves multiple failures as well - existing ones are one failure only

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:54 · comment 822677448 · PR 14066 · 2026-07-07

Source path: `investment-impl/src/test/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessorTest.scala`

**Explicit source context (pr_title):**

> [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification

## A1-0227 — Instrument retrieval test already covers DB-only data without instrument-service mock

**Source stance:** reported-verification

**Context:**

> component: trading-impl/src/test/scala/com/endowus/silver/trading/impl/utils/InstrumentInfoRetrieverTest.scala; operation: [INV-5873] feat(advisory)(dividend)(goal)(investment)(rebalance)(trading): Harden investor types validation for all buy trade flows; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This is covered in the test above when we do not mock the instrument svc call, and data is returned from DB only

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:234 · comment 814231380 · PR 14118 · 2026-06-18

Source path: `trading-impl/src/test/scala/com/endowus/silver/trading/impl/utils/InstrumentInfoRetrieverTest.scala`

**Explicit source context (pr_title):**

> [INV-5873] feat(advisory)(dividend)(goal)(investment)(rebalance)(trading): Harden investor types validation for all buy trade flows

## A1-0262 — Add instrument retrieval V2 test for MIC conversion

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala; operation: [INV-5597] feat(instrument): add mic in instrument; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can we add some test for verify this in `InstrumentRetrievalManagerV2Test`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:269 · comment 809593964 · PR 13945 · 2026-06-11

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala`

**Explicit source context (pr_title):**

> [INV-5597] feat(instrument): add mic in instrument

**Evidence:** anon-1.jsonl:269 · comment 809593964 · PR 13945 · 2026-06-11

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala`

**Explicit source context (hunk):**

> fundDocuments = returnedDocuments.map(FundDocumentV2.toDto),
> -      totalAum = data.totalAum
> +      totalAum = data.totalAum,
> +      mic = data.mic,
> +      exchangeName = data.mic.map(MicAndExchangeNameMapping.getName),
>      )
>    }

## A1-0275 — Test-data fluent methods mix set and with naming

**Source stance:** open-question

**Context:**

> component: report-impl/src/test/scala/com/endowus/silver/report/impl/statementv3/testdata/StatementDataTestData.scala; operation: [INV-5784] Feat/transaction mapping; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> It doesn’t matter but how come these methods are `set` but the others are `with`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:282 · comment 798880464 · PR 13849 · 2026-05-20

Source path: `report-impl/src/test/scala/com/endowus/silver/report/impl/statementv3/testdata/StatementDataTestData.scala`

**Explicit source context (pr_title):**

> [INV-5784] Feat/transaction mapping

**Evidence:** anon-1.jsonl:282 · comment 798880464 · PR 13849 · 2026-05-20

Source path: `report-impl/src/test/scala/com/endowus/silver/report/impl/statementv3/testdata/StatementDataTestData.scala`

**Explicit source context (hunk):**

> )
>  
> -  implicit class CompletedOrderOps(val order: CompletedOrder) extends AnyVal {
> +  implicit class CompletedOrderOps(val order: CompletedOrder) {
> +    def setOrderId(id: UUID): CompletedOrder = order.copy(orderId = id)
> +    def setInstrumentId(id: String): CompletedOrder = order.copy(instrumentId = id)
> +    def setUnits(u: BigDecimal): CompletedOrder = order.copy(units = u)
> +    def setAmount(a: BigDecimal): CompletedOrder = order.copy(amount = a)
> +    def setPrice(p: BigDecimal): CompletedOrder = order.copy(price = p)

## A1-0313 — Test all two-cache interactions in InstrumentDailyPerformanceCache

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCache.scala; operation: [INV-5558] feat(advisory): add performance based on daily market data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add test for `InstrumentDailyPerformanceCache` to verify the behaviour of various combinations of the 2 cache interactions

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:320 · comment 796350175 · PR 13698 · 2026-05-13

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCache.scala`

**Explicit source context (pr_title):**

> [INV-5558] feat(advisory): add performance based on daily market data

## A1-0314 — Add metrics-cache-missing or evicted test

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala; operation: [INV-5558] feat(advisory): add performance based on daily market data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> add another test but with metricsCache having no entry \(e.g. evicted\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:321 · comment 797319938 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (pr_title):**

> [INV-5558] feat(advisory): add performance based on daily market data

**Evidence:** anon-1.jsonl:321 · comment 797319938 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (hunk):**

> +        for {
> +          _ <- cache.getCachedInstrumentPerformance(instrumentId1)
> +          _ = cache.metricsDataCache
> +            .synchronous()
> +            .put(
> +              instrumentId1,
> +              InstrumentDailyPerformanceCache.MetricsData(
> +                sampleMetricsDto.copy(returnEnd = version2.returnEnd),
> +                version2

## A1-0317 — Verify calculateInstrumentDailyPerformanceBatch once and no more interactions

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala; operation: [INV-5558] feat(advisory): add performance based on daily market data; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** No mock reset needed; include details-fetch interactions and other tests

**Source-preserving request, proposal, or question:**

> We don’t need to reset mock? I think we can just verify that `calculateInstrumentDailyPerformanceBatch` was called only once? You can additionally check `verifyNoMoreInteractions` as well, to ensure the mock is not engaged with other calls \(e.g. the details fetch\). Can update for other test cases as well

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:324 · comment 797311849 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (pr_title):**

> [INV-5558] feat(advisory): add performance based on daily market data

## A1-0318 — Verify getCachedInstrumentPerformancesMetrics returns without remote call

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala; operation: [INV-5558] feat(advisory): add performance based on daily market data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> let’s verify `getCachedInstrumentPerformancesMetrics` also return without remote call

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:325 · comment 797313538 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (pr_title):**

> [INV-5558] feat(advisory): add performance based on daily market data

**Evidence:** anon-1.jsonl:325 · comment 797313538 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (hunk):**

> +        when(performanceServiceMock.calculateInstrumentDailyPerformance(any()))
> +          .thenReturn(Future.successful(fullRemoteResponse))
> +
> +        for {
> +          _ <- cache.getCachedInstrumentPerformance(instrumentId1) // warm both caches
> +          fullResponseResult <- cache.getCachedInstrumentPerformance(instrumentId1)
> +          metricResult <- cache.getCachedInstrumentPerformancesMetrics(Seq(instrumentId1))
> +        } yield {
> +          verify(performanceServiceMock, times(1)).calculateInstrumentDailyPerformance(any())

## A1-0319 — Change sampleMetricsDto returnEnd and verify refreshed metric data

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala; operation: [INV-5558] feat(advisory): add performance based on daily market data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> change the `sampleMetricsDto` 's returnEnd too, and verify the result to have refreshed metrics data

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:326 · comment 797319146 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (pr_title):**

> [INV-5558] feat(advisory): add performance based on daily market data

## A1-0320 — Metric-only cache case differs from out-of-sync two-cache case

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala; operation: [INV-5558] feat(advisory): add performance based on daily market data; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Chart fetch should update metrics cache

**Source-preserving request, proposal, or question:**

> It’s different right? the other test is both caches exist but out of sync, this test is only metric cache has data. And we want to verify remote fetch on chart cache will update metrics cache as well

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:327 · comment 797345721 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (pr_title):**

> [INV-5558] feat(advisory): add performance based on daily market data

## A1-0321 — Use theSameElementsAs assertion

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala; operation: [INV-5558] feat(advisory): add performance based on daily market data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> theSameElementsAs right?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:328 · comment 797370329 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (pr_title):**

> [INV-5558] feat(advisory): add performance based on daily market data

**Evidence:** anon-1.jsonl:328 · comment 797370329 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (hunk):**

> +          )
> +
> +        getCache.getCachedInstrumentPerformancesMetrics(Seq(instrumentId1, instrumentId2)).map { result =>
> +          verify(performanceServiceMock, times(1)).calculateInstrumentDailyPerformanceBatch(any())
> +          result.size shouldBe 2
> +          result.keySet should contain theSameElementsAs Set(instrumentId1, instrumentId2)
> +        }
> +      }
> +    }

## A1-0322 — Do not remock unchanged behavior

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala; operation: [INV-5558] feat(advisory): add performance based on daily market data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No change so we dont need to mock again right?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:329 · comment 797371023 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (pr_title):**

> [INV-5558] feat(advisory): add performance based on daily market data

**Evidence:** anon-1.jsonl:329 · comment 797371023 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (hunk):**

> +                sampleMetricsDto.copy(returnEnd = version2.returnEnd),
> +                version2
> +              )
> +            )
> +
> +          refreshed <- cache.getCachedInstrumentPerformance(instrumentId1)
> +          metrics <- cache.getCachedInstrumentPerformancesMetrics(Seq(instrumentId1))
> +        } yield {
> +          verify(performanceServiceMock, times(2)).calculateInstrumentDailyPerformance(any())

## A1-0323 — Verify result2 has same data as result1

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala; operation: [INV-5558] feat(advisory): add performance based on daily market data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> verify result2 gives same data as result1

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:330 · comment 797369438 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (pr_title):**

> [INV-5558] feat(advisory): add performance based on daily market data

**Evidence:** anon-1.jsonl:330 · comment 797369438 · PR 13698 · 2026-05-15

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyPerformanceCacheSpec.scala`

**Explicit source context (hunk):**

> +            .calculateInstrumentDailyPerformanceBatch(any())
> +
> +          verifyNoMoreInteractions(performanceServiceMock)
> +          result1 should contain key instrumentId1
> +          result2 should contain key instrumentId1
> +          result1 shouldBe result2
> +        }
> +      }
> +

## A1-0485 — Update test name

**Source stance:** requested-change

**Context:**

> component: bff-impl/src/test/scala/com/endowus/silver/bff/impl/routes/guards/GuardsTest.scala; operation: [INV-5664] fix(bff): update add goal flow endpoints to allow reviewed with deficiency customers and streamlined acl customer statuses; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> update this test name

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:492 · comment 790255618 · PR 13782 · 2026-04-29

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/routes/guards/GuardsTest.scala`

**Explicit source context (pr_title):**

> [INV-5664] fix(bff): update add goal flow endpoints to allow reviewed with deficiency customers and streamlined acl customer statuses

**Evidence:** anon-1.jsonl:492 · comment 790255618 · PR 13782 · 2026-04-29

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/routes/guards/GuardsTest.scala`

**Explicit source context (hunk):**

> }
>  
> -      "succeed when SUSPENDED customer uses defaultAllowedCustomerStatusesIncludingSuspended" in {
> -        import com.endowus.silver.bff.api.guarddef.GuardDef.defaultAllowedCustomerStatusesIncludingSuspended
> +      "succeed when SUSPENDED customer uses activeOrSuspendedCustomerStatuses" in {
> +        import com.endowus.silver.bff.api.guarddef.GuardDef.activeOrSuspendedCustomerStatuses
>          val request: UUID = customerId
>          `customerService / getRegionalCustomerStatus`(customerId)(Future.successful(CustomerStatus.SUSPENDED))
>          allowedCustomerStatus(

## A1-0556 — Test B2B displayCcy update after FA enables auto-rebalance

**Source stance:** requested-change

**Context:**

> component: customer-impl/src/main/scala/com/endowus/silver/customer/impl/logic/ServiceLogicImpl.scala; operation: BB-3188 auto rebalncing toggle; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** updateCustomerPreferences only permits displayCcy for B2B

**Source-preserving request, proposal, or question:**

> The existing `updateCustomerPreferences` explicitly checks that B2B customers can only update displayCcy, and nothing else in the preferences.
> 
> Just make sure we test the scenario after FA enables auto-rebalance, it doesn’t break the displayCcy update flow

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:563 · comment 775853518 · PR 13477 · 2026-03-31

Source path: `customer-impl/src/main/scala/com/endowus/silver/customer/impl/logic/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> BB-3188 auto rebalncing toggle

## A1-0579 — Caller provides date via injectable DateTimeProvider

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/calculators/IncomeProjectionCalculator.scala; operation: [PG-1948] feat(advisory) Income projection; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Default date loses timezone control

**Source-preserving request, proposal, or question:**

> Don’t default like this, you lose the ability to control timezone.
> 
> Just expect caller to provide the date - which they can inject DateTimeProvider themselves

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:586 · comment 775460093 · PR 13581 · 2026-03-30

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/calculators/IncomeProjectionCalculator.scala`

**Explicit source context (pr_title):**

> [PG-1948] feat(advisory) Income projection

## A1-0623 — Test auto-retry with stitch false

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: Feat/INV-5489 update stitch details endpoint; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Test would catch wrong exception handling

**Source-preserving request, proposal, or question:**

> Can we add a test case for the auto-retry with stitch = false behaviour too, that test would have failed here?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:630 · comment 774419557 · PR 13571 · 2026-03-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> Feat/INV-5489 update stitch details endpoint

## A1-0689 — Update HK email test date and decimal formatters

**Source stance:** requested-change

**Context:**

> component: communication-api/src/test/scala/localization/LocalizationSupportTest.scala; operation: [INV-5271] feat(communication, investment, rebalance, redemption): Send fund order transaction details into HK emails; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> It doesn’t matter but we should also update this test to follow the new formatter for dates & decimals?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:699 · comment 758035069 · PR 13316 · 2026-02-23

Source path: `communication-api/src/test/scala/localization/LocalizationSupportTest.scala`

**Explicit source context (pr_title):**

> [INV-5271] feat(communication, investment, rebalance, redemption): Send fund order transaction details into HK emails

## A1-0816 — Add PortfolioRepositoryTest filter coverage

**Source stance:** requested-change

**Context:**

> component: None; operation: Feat/BB-2959 portfolio filters enhancement; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add some coverage to verify the change in `PortfolioRepositoryTest`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:828 · comment 743471653 · PR 12884 · 2026-01-23

**Explicit source context (pr_title):**

> Feat/BB-2959 portfolio filters enhancement

## A1-0817 — Test empty inSetBind returning false

**Source stance:** requested-change

**Context:**

> component: silver-commons-jdbc/src/main/scala/com/endowus/silver/commons/jdbc/Filters.scala; operation: Feat/BB-2959 portfolio filters enhancement; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Slick implementation already checks seq.isEmpty

**Source-preserving request, proposal, or question:**

> ```
>   def inSet[R](seq: scala.collection.Iterable[B1])(implicit om: o#to[Boolean, R]) =
>     if(seq.isEmpty) om(LiteralColumn(false))
>     else om.column(Library.In, n, ProductNode(ConstArray.from(seq.map{ v => LiteralNode(implicitly[TypedType[B1]], v) })))
>   def inSetBind[R](seq: scala.collection.Iterable[B1])(implicit om: o#to[Boolean, R]) =
>     if(seq.isEmpty) om(LiteralColumn(false))
>     else om.column(Library.In, n, ProductNode(ConstArray.from(seq.map(v => LiteralNode(implicitly[TypedType[B1]], v, vol = true)))))
> ```
> 
> We can add a test for empty too to verify this

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:829 · comment 743515609 · PR 12884 · 2026-01-23

Source path: `silver-commons-jdbc/src/main/scala/com/endowus/silver/commons/jdbc/Filters.scala`

**Explicit source context (pr_title):**

> Feat/BB-2959 portfolio filters enhancement

## A1-0864 — Update InstrumentInfoDtoTest for derived standalone

**Source stance:** requested-change

**Context:**

> component: instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/v2/models.scala; operation: [INV-4869] feat(bff, advisory, instrument, portfolio): Add a flag for instruments which are marked as Standalone-only and add amount restriction in fund-smart invest flow summary; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s update this test as well `InstrumentInfoDtoTest`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:876 · comment 737971070 · PR 13163 · 2026-01-13

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/v2/models.scala`

**Explicit source context (pr_title):**

> [INV-4869] feat(bff, advisory, instrument, portfolio): Add a flag for instruments which are marked as Standalone-only and add amount restriction in fund-smart invest flow summary

**Evidence:** anon-1.jsonl:876 · comment 737971070 · PR 13163 · 2026-01-13

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/v2/models.scala`

**Explicit source context (hunk):**

> +      val hasSubscriptionRestriction = instrument.subscriptionDetails.exists { s => hasNonDailySchedule(s.dealingSchedule) || hasNonDailySchedule(s.tradingExportSchedule) || hasLotSize(s.regulation) }
>        val isIlliquidAlts = instrument.isIlliquidAlts
>        val isNotOpenForSubscription = instrument.isOpenOnlyForInterestRegistration
> -      !(isIlliquidAlts || hasLotRestriction || isNotOpenForSubscription)
> +      val isForcedToBeStandalone = instrument.endowusDetails.isForcedToBeStandalone.contains(true)
> +      !(isForcedToBeStandalone || isIlliquidAlts || hasRedemptionRestriction || hasSubscriptionRestriction || isNotOpenForSubscription)
>      }
>  
> +    private def hasNonDailySchedule(schedule: Option[DealingScheduleDto]): Boolean = schedule.exists(_.dealingFrequency != DealingFrequency.Daily)

## A1-0884 — Write fetched old data to separate file for per-entry comparison

**Source stance:** suggestion

**Context:**

> component: amend-scripts/src/main/scala/report/AuditSupportHoldingByGoal.scala; operation: [INV-5205] feat(report): add isin to response; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Old data need no ISIN

**Source-preserving request, proposal, or question:**

> Since we already fetch, I’m wondering if we should just write to another file using old data. This way we can compare individual entries too if needed. This old data file doesnt need isin , as we just want to cross check

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:897 · comment 738898353 · PR 13194 · 2026-01-15

Source path: `amend-scripts/src/main/scala/report/AuditSupportHoldingByGoal.scala`

**Explicit source context (pr_title):**

> [INV-5205] feat(report): add isin to response

## A1-0887 — Old writer only needs comparison data, not extra output

**Source stance:** explanation

**Context:**

> component: amend-scripts/src/main/scala/report/AuditSupportHoldingByGoal.scala; operation: [INV-5205] feat(report): add isin to response; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I guess we dont need to write this to old writer, since we only need old data for comparison

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:900 · comment 738903369 · PR 13194 · 2026-01-15

Source path: `amend-scripts/src/main/scala/report/AuditSupportHoldingByGoal.scala`

**Explicit source context (pr_title):**

> [INV-5205] feat(report): add isin to response

**Evidence:** anon-1.jsonl:900 · comment 738903369 · PR 13194 · 2026-01-15

Source path: `amend-scripts/src/main/scala/report/AuditSupportHoldingByGoal.scala`

**Explicit source context (hunk):**

> +                .map(_.asInstanceOf[GoalBasedStatementInfoDto].statementData)
> +                .recoverWith {
> +                  case e: NotFound =>
> +                    val output = OutputFormat(customerId, customerStatus, "", "", "", "", "", "")
> +                    outputWriter.write(
> +                      output.customerId + ";" + output.status + ";" + output.goalName + ";" + output.isin + ";" + output.fundName ++ ";" + output.source + ";" + output.unit + ";" + output.mv + System.lineSeparator
> +                    )
> +                    outputWriter.flush()
> +                    Future.successful(emptyDummyStatement)

## A1-0931 — Option generic type check erased and gives false assurance

**Source stance:** observed-defect

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala; operation: Fatal compiler warnings; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Type erasure for Option. These gives false sense of assurance

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:944 · comment 730845938 · PR 13132 · 2025-12-23

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (pr_title):**

> Fatal compiler warnings

## A1-0932 — Only assert Some wildcard because generic type erased

**Source stance:** requested-change

**Context:**

> component: charge-impl/src/test/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriberSpec.scala; operation: Fatal compiler warnings; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> At most we can only check `shouldBe a[Some[_]]` since the generic type is erased

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:945 · comment 730844478 · PR 13132 · 2025-12-23

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriberSpec.scala`

**Explicit source context (pr_title):**

> Fatal compiler warnings

## A1-0948 — simulateOnly should log merged result or return it without persistence

**Source stance:** suggestion

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: [INV-4722] feat(marketdata): support single monthly change update; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Hmm this `simulateOnly` flag is pretty useless isn’t it? If we want to keep it, let’s put a log of the merge result or return that in response \(without persisting\)?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:963 · comment 680628306 · PR 12533 · 2025-09-09

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-4722] feat(marketdata): support single monthly change update

## A1-1238 — Extract slug helper for test without service setup

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala; operation: Feat/INV-4886 slugs for instrument details; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Extract this to utils method, so that you can test it well without having to deal with the service logic setup\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1253 · comment 719907891 · PR 12965 · 2025-12-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> Feat/INV-4886 slugs for instrument details

## A1-1239 — Expected slug should be literal or slugify helper, not production service logic

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/FundSmartCollectionManagerTest.scala; operation: Feat/INV-4886 slugs for instrument details; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Doesn’t look right to have test code calling prod code. Either put the actual resolved string here, or at most call the utils slugify here

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1254 · comment 719908040 · PR 12965 · 2025-12-01

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/FundSmartCollectionManagerTest.scala`

**Explicit source context (pr_title):**

> Feat/INV-4886 slugs for instrument details

## A1-1240 — Translation allocation mocks should not be None

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManagerV3Test.scala; operation: Feat/INV-4917 translation allocations; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Are these mocks wrong? It shouldn’t be None?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1255 · comment 718323888 · PR 12954 · 2025-11-26

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManagerV3Test.scala`

**Explicit source context (pr_title):**

> Feat/INV-4917 translation allocations

**Evidence:** anon-1.jsonl:1255 · comment 718323888 · PR 12954 · 2025-11-26

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManagerV3Test.scala`

**Explicit source context (hunk):**

> })
>  
>  
> -    when(compositionService.getInstrumentData(anyString)).thenReturn(
> +    when(compositionService.getInstrumentData(anyString, any)).thenReturn(
>        Future.successful(InstrumentDataDto(instrumentId = "someId", marketExposure = Some(marketExposure), sectorAllocation = Some(sectorAllocation)))
>      )
>    }

## A1-1243 — Test Scaffeine behavior in ScaffeineCacheSpec

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/LocaleAwareInstrumentCache.scala; operation: Feat/INV-4922 consolidate advisory duplicate caches; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can we also put a test for this? Ideally in `ScaffeineCacheSpec` to capture the fact that scaffeine support this feature?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1258 · comment 717288931 · PR 12908 · 2025-11-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/LocaleAwareInstrumentCache.scala`

**Explicit source context (pr_title):**

> Feat/INV-4922 consolidate advisory duplicate caches

## A1-1247 — Include requested Int in test key instead of ignoring it

**Source stance:** suggestion

**Context:**

> component: silver-commons/src/test/scala/com/endowus/silver/commons/spike/ScaffeineCacheSpec.scala; operation: Feat/INV-4922 consolidate advisory duplicate caches; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Probably better to add `i` in the requested Int in the key, instead of ignoring the provided Int completely

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1262 · comment 718772501 · PR 12908 · 2025-11-27

Source path: `silver-commons/src/test/scala/com/endowus/silver/commons/spike/ScaffeineCacheSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-4922 consolidate advisory duplicate caches

## A1-1251 — Call cache twice explicitly in test

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/BaseServiceLogicImpl.scala; operation: Feat/INV-4922 consolidate advisory duplicate caches; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Just call the thing twice :sweat_smile:

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1266 · comment 718772806 · PR 12908 · 2025-11-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-4922 consolidate advisory duplicate caches

**Evidence:** anon-1.jsonl:1266 · comment 718772806 · PR 12908 · 2025-11-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> override def invalidateInstrumentCache(instrumentIds: Iterable[String]): Future[Done] = {
> -    cacheManagementPublisher.triggerInvalidateCacheEntries(InstrumentCacheKeys(instrumentIds))
>      Locale.getSupportedLocales(localConfig.getSilverRegion).foreach { locale =>
> -      cacheManagementPublisher.triggerInvalidateCacheEntries(LocaleAwareInstrumentCacheKeys(instrumentIds.map((_, locale))))
> +      cacheManagementPublisher.triggerInvalidateCacheEntries(LocaleAwareInstrumentCacheKeys(instrumentIds.map((_, locale, true))))
> +      cacheManagementPublisher.triggerInvalidateCacheEntries(LocaleAwareInstrumentCacheKeys(instrumentIds.map((_, locale, false))))
>      }
>      Future.successful(Done)
>    }

## A1-1252 — Test multiple variants fetched but only requested keys returned

**Source stance:** requested-change

**Context:**

> component: silver-commons/src/test/scala/com/endowus/silver/commons/spike/ScaffeineCacheSpec.scala; operation: Feat/INV-4922 consolidate advisory duplicate caches; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add that “should call for multiple variance but return only requested keys”

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1267 · comment 718772638 · PR 12908 · 2025-11-27

Source path: `silver-commons/src/test/scala/com/endowus/silver/commons/spike/ScaffeineCacheSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-4922 consolidate advisory duplicate caches

**Evidence:** anon-1.jsonl:1267 · comment 718772638 · PR 12908 · 2025-11-27

Source path: `silver-commons/src/test/scala/com/endowus/silver/commons/spike/ScaffeineCacheSpec.scala`

**Explicit source context (hunk):**

> +
> +        _ <- awaitForEntryAvailability(("keyX", 0), cache)
> +        successfulGet3 <- cache.get(("keyX", 0))
> +      } yield {
> +        verify(valueProvider, times(1)).fetchValue(("keyX", 0))
> +        verify(valueProvider, times(1)).fetchValue(("keyX", 1))
> +
> +        // 1st get is illegal cache usage
> +        errorGet1 shouldBe a[UnsupportedOperationException]

## A1-1269 — All cash-only redemption usages verified for urgent release

**Source stance:** reported-verification

**Context:**

> component: redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/logic/util/RedemptionHelper.scala; operation: [INV-5052] fix(redemption): Exclude cash only fee for hasPendingAmountBasedRedemption; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Later extract predicates into RedemptionRequestDto def/lazy val for isolated tests

**Source-preserving request, proposal, or question:**

> I think we can release to unblock prod for today. I have already verified all the usages of this.
> 
> In the cleanup/refactor PR, these conditions should be extracted in def/lazy val of RedemptionRequestDto itself, so that the unit tests can be isolated

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1284 · comment 716139331 · PR 12913 · 2025-11-20

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/logic/util/RedemptionHelper.scala`

**Explicit source context (pr_title):**

> [INV-5052] fix(redemption): Exclude cash only fee for hasPendingAmountBasedRedemption

## A1-1303 — Test derived area/perimeter JSON cannot influence deserialization

**Source stance:** requested-change

**Context:**

> component: silver-commons/src/test/scala/com/endowus/silver/commons/endpoints4s/JsonSchemaPlayJsonTest.scala; operation: adds derived fields to json schema and play json; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can we also add another test in which we purposely mess up the data for area/perimeter, but still it shouldn’t affect deser

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1318 · comment 708831874 · PR 12857 · 2025-11-04

Source path: `silver-commons/src/test/scala/com/endowus/silver/commons/endpoints4s/JsonSchemaPlayJsonTest.scala`

**Explicit source context (pr_title):**

> adds derived fields to json schema and play json

## A1-1358 — Revert translation-filter commit because tests unresolved

**Source stance:** reported-verification

**Context:**

> component: None; operation: Revert "Merged in feat/INV-4945-be-fix-to-translation-the-filte (pull request #12802)"; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Original commit has unresolved test failures. Reverting for now
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1373 · comment 705758277 · PR 12838 · 2025-10-28

**Explicit source context (pr_title):**

> Revert "Merged in feat/INV-4945-be-fix-to-translation-the-filte (pull request #12802)"

## A1-1380 — Take current date from dateTimeProvider

**Source stance:** open-question

**Context:**

> component: redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/logic/service/BaseServiceLogicImpl.scala; operation: [INV-4563] feat(bff, goal, redemption, trading): Add full redemption threshold endpoint; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Don’t we need to take from dateTimeProvider?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1396 · comment 702911106 · PR 12525 · 2025-10-22

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/logic/service/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4563] feat(bff, goal, redemption, trading): Add full redemption threshold endpoint

**Evidence:** anon-1.jsonl:1396 · comment 702911106 · PR 12525 · 2025-10-22

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/logic/service/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +
> +  override def getPlanRedeemableValue(planId: UUID): Future[PlanRedeemableValueResponse] = {
> +    val endDate = dateTimeProvider.localDateNow
> +    val (currentQuarterYear, currentQuarter) = QuarterUtils.deriveYearAndQuarter(endDate)
> +    val (previousQuarterYear, previousQuarter) = QuarterUtils.previousQuarter(year = currentQuarterYear, quarter = currentQuarter)
> +
> +    for {
> +      liveMv <- redemptionHelper.calculateLiveMarketValue(planId)
> +      _ = logger.info(s"Live market value for plan [$planId]: $liveMv")

## A1-1409 — Test duplicate dates while range has both from and to

**Source stance:** requested-change

**Context:**

> component: silver-commons/src/test/scala/com/endowus/silver/commons/utils/RangingUtilsTest.scala; operation: [NE-353] (timeseries) log dates in compact form using range coding; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add one more test case just for completeness, i,e. duplicate item when having both from & to:
> 
> `case (head :: Nil, Some(from), Some((span, to)))`
> 
> `case (head :: (tail @ (_ :: _)), Some(from), Some((span, to)))`
> 
> ```scala
> mk(List("2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05", "2025-01-05")) shouldBe "2025-01-01 .. 2025-01-05"
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1425 · comment 703421263 · PR 12819 · 2025-10-23

Source path: `silver-commons/src/test/scala/com/endowus/silver/commons/utils/RangingUtilsTest.scala`

**Explicit source context (pr_title):**

> [NE-353] (timeseries) log dates in compact form using range coding

## A1-1419 — Add thorough approval identifier test scenarios

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertSubmitForApprovalBehaviour.scala; operation: [BB-2974][BB-2975]: Fix issue related to missing approval identifier; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add good set of test cases for this

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1435 · comment 691274928 · PR 12684 · 2025-09-30

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertSubmitForApprovalBehaviour.scala`

**Explicit source context (pr_title):**

> [BB-2974][BB-2975]: Fix issue related to missing approval identifier

**Evidence:** anon-1.jsonl:1435 · comment 691274928 · PR 12684 · 2025-09-30

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertSubmitForApprovalBehaviour.scala`

**Explicit source context (hunk):**

> for {
>        _ <- doTenantAwareValidations(product, request, goal, input.context)
> -      res <- submitForApproval(input.context.tenantId, input.context.employeeId, goal.customerId, goal.name, request)
> +      approvalIdentifier = getTypeOfAdvisedPortfolioInvestmentRequest(goal, request)
> +      res <- submitForApproval(input.context.tenantId, input.context.employeeId, goal.customerId, goal.name, approvalIdentifier, request)
>      } yield res
>    }

## A1-1528 — Voucher test fix reported ready for rebase

**Source stance:** reported-verification

**Context:**

> component: None; operation: [PLATFORM-1845] Remove kafka lib; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> It’s a test in voucher svc.
> […incidental material or intervening source omitted…]
> has fixed it, you can rebase

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No test output in comment; do not infer complete validation.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1545 · comment 691909127 · PR 12699 · 2025-10-01

> It’s a test in voucher svc.

**Explicit source context (pr_title):**

> [PLATFORM-1845] Remove kafka lib

**Evidence:** anon-1.jsonl:1545 · comment 691909127 · PR 12699 · 2025-10-01

> has fixed it, you can rebase

## A1-1575 — Test factual price exactly on common-start date

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyNavCacheSpec.scala; operation: [INV-4822] feat(advisory, marketdata): Filter out daily index before inception date; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add another case in which we use from common, and factual price data has entry on that exact date as well

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1592 · comment 690791957 · PR 12653 · 2025-09-29

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/cache/InstrumentDailyNavCacheSpec.scala`

**Explicit source context (pr_title):**

> [INV-4822] feat(advisory, marketdata): Filter out daily index before inception date

## A1-1633 — Unit tests plus dynamic manual tests across tenants

**Source stance:** requested-change

**Context:**

> component: None; operation: [BB-2784] feat(bff)(workflow): exposing task by status api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add some unit tests \+ manual tests in dynamic with multiple tenants :pray:

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1649 · comment 684369737 · PR 12434 · 2025-09-16

**Explicit source context (pr_title):**

> [BB-2784] feat(bff)(workflow): exposing task by status api

## A1-1655 — Eight services deployed to d38 and started; full E2E still planned

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4466] feat(common): Front load heavy application init before joining Cluster; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Deployed these services to d38 and all came up fine. Will test for all services against e2e test as well
> 
> ```
> charge customer iam performance portfolio projection report timeseries
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1671 · comment 646542903 · PR 12081 · 2025-06-18

**Explicit source context (pr_title):**

> [INV-4466] feat(common): Front load heavy application init before joining Cluster

## A1-1691 — Removed-marketvalue-message test verifies nothing and still passes

**Source stance:** observed-defect

**Context:**

> component: rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/subscribers/PlanTimeSeriesTopicSubscriberTest.scala; operation: [INV-4468] feat(charge)(rebate): Stop handling LatestPlanMarketValueUpdatedMsg in charge/rebate as already processing PlanMarketValuesUpdatedMsg/PlanMarketValuesRemovedMsg; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This test doesn’t verify anything, so actually it would still pass :rofl:

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1709 · comment 647321822 · PR 12096 · 2025-06-20

Source path: `rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/subscribers/PlanTimeSeriesTopicSubscriberTest.scala`

**Explicit source context (pr_title):**

> [INV-4468] feat(charge)(rebate): Stop handling LatestPlanMarketValueUpdatedMsg in charge/rebate as already processing PlanMarketValuesUpdatedMsg/PlanMarketValuesRemovedMsg

## A1-1701 — Background reconciliation makes test flaky if return precedes completion

**Source stance:** open-question

**Context:**

> component: instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogicSpec.scala; operation: Resolve INV-4629: Add back filter stream from db; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Won’t this be flaky cuz we are running the recon in background and not waiting for it to complete before returing?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1719 · comment 684272522 · PR 12614 · 2025-09-16

Source path: `instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogicSpec.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Add back filter stream from db

## A1-1714 — One region test enough if no region-specific behavior

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/test/scala/com/endowus/silver/rebalance/impl/logic/HkThresholdBreachRebalanceLogicTest.scala; operation: [INV-4653] feat(advisory, charge, goal, instrument, investment, rebalance, redemption, trading): freeze principal funds; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> If we don't have any test specific to region, I think it’s fine to select either in existing test, no need to create both

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1732 · comment 680671375 · PR 12566 · 2025-09-09

Source path: `rebalance-impl/src/test/scala/com/endowus/silver/rebalance/impl/logic/HkThresholdBreachRebalanceLogicTest.scala`

**Explicit source context (pr_title):**

> [INV-4653] feat(advisory, charge, goal, instrument, investment, rebalance, redemption, trading): freeze principal funds

## A1-1730 — Test throws NotFound synchronously instead of Future.failed

**Source stance:** observed-defect

**Context:**

> component: fxwallet-impl/src/test/scala/com/endowus/silver/fxwallet/impl/logic/service/FxWalletConversionServiceImplSpec.scala; operation: [NE-337] remove lagom transport exception usages; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Expected production wrapper FxWalletSvcException should be verified, not changed to satisfy test

**Source-preserving request, proposal, or question:**

> I guess you’re changing the prod code to catch NotFound explicitly because of this test?
> 
> But looks like this test itself should be change, since it throws NotFound directly via thenThrow instead of Future.failed… since by right, it should have verified that the exception is the wrapped FxWalletSvcException?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1748 · comment 680175622 · PR 12555 · 2025-09-08

Source path: `fxwallet-impl/src/test/scala/com/endowus/silver/fxwallet/impl/logic/service/FxWalletConversionServiceImplSpec.scala`

**Explicit source context (pr_title):**

> [NE-337] remove lagom transport exception usages

## A1-1765 — Hardcoded ExploreData list mapped by id must have no duplicates

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/explore/db/ExploreRepository.scala; operation: [INV-4379] feat(advisory): create models for explore 2.0; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> `SgInfoComponents` → List\[ExploreData\]….
> 
> val data = .map\(data => [data.id](
> […incidental material or intervening source omitted…]
> → data\).toMap
> 
> ‌
> 
> add test to assert no ExploreData in the concatenated list with duplicated id

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1784 · comment 638259311 · PR 11919 · 2025-05-28

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/explore/db/ExploreRepository.scala`

> `SgInfoComponents` → List\[ExploreData\]….
> 
> val data = .map\(data => [data.id](

**Explicit source context (pr_title):**

> [INV-4379] feat(advisory): create models for explore 2.0

**Evidence:** anon-1.jsonl:1784 · comment 638259311 · PR 11919 · 2025-05-28

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/explore/db/ExploreRepository.scala`

> → data\).toMap
> 
> ‌
> 
> add test to assert no ExploreData in the concatenated list with duplicated id

## A1-1779 — Validate hardcoded Explore data in tests instead of runtime

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/db/explore/ExploreDataRepository.scala; operation: [INV-4379] feat(advisory): create models for explore 2.0; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Since these are hardcoded, let’s make it accessible in test, and move this validation there, instead of runtime so that we can catch data issue earlier
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1798 · comment 641844972 · PR 11919 · 2025-06-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/db/explore/ExploreDataRepository.scala`

**Explicit source context (pr_title):**

> [INV-4379] feat(advisory): create models for explore 2.0

## A1-1810 — Portfolio startup tested with no CPU limit and300m

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4417] feat(common): Akka Cluster startup sequence; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Throttle severe delay before app init; schema dominant, HTTP quick

**Source-preserving request, proposal, or question:**

> Tested in d38 with portfolio svc
> 
> * Deploy both develop \(with some minor extra loggings\) \+ this feature branch
> * Run without cpu limit \(normal setup\) \+ with 300m cpu limit \(typically portfolio svc in prod gets this much, and we can observe the long startup\)
> 
> ### Container CPU
> […incidental material or intervening source omitted…]
> * Not sure why it only uses upto 250m when 300m cpu limit is enforced. But we know it definitely needs more, cuz we can observe the cpu throttle metrics having non-zero value
> * When no cpu limit is set, it takes ~350m during startup phase. This is regardless of the branch being deployed \(indeed, the change here doesn’t affect total cpu usage, only shift the init priority\)
> 
> ### Startup logs of develop branch
> 
> |  | **Without CPU limit** | **With CPU limit = 300m** |
> | --- | --- | --- |
> | Develop branch |
> […incidental material or intervening source omitted…]
> | This branch |
> […incidental material or intervening source omitted…]
> * When CPU is limited, the degradation is very severe, if even actual cpu it needs is not significantly higher \(limit of 300m VS actual usage when no limit of ~400-500m\)
> * Slowness can be observed even before application init, during Kamon init / Remoting init / Cluster init and akka management init
> * DB schema setup takes majority of the application init time \(with or without cpu limit\), even though we know it shouldn’t do anything cuz all the tables & indices already exist. Might be sth to take a deeper look when time allows \(?\)
> * After the http routes are initialized, the http server startup is very fast \(with or without cpu limit / with or without this change\)
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Change shifts init priority, not total CPU; usage approximate350m/400-500m.

**Evidence:** anon-1.jsonl:1829 · comment 637771014 · PR 11901 · 2025-05-27

> Tested in d38 with portfolio svc
> 
> * Deploy both develop \(with some minor extra loggings\) \+ this feature branch
> * Run without cpu limit \(normal setup\) \+ with 300m cpu limit \(typically portfolio svc in prod gets this much, and we can observe the long startup\)
> 
> ### Container CPU

**Explicit source context (pr_title):**

> [INV-4417] feat(common): Akka Cluster startup sequence

**Evidence:** anon-1.jsonl:1829 · comment 637771014 · PR 11901 · 2025-05-27

> * Not sure why it only uses upto 250m when 300m cpu limit is enforced. But we know it definitely needs more, cuz we can observe the cpu throttle metrics having non-zero value
> * When no cpu limit is set, it takes ~350m during startup phase. This is regardless of the branch being deployed \(indeed, the change here doesn’t affect total cpu usage, only shift the init priority\)
> 
> ### Startup logs of develop branch
> 
> |  | **Without CPU limit** | **With CPU limit = 300m** |
> | --- | --- | --- |
> | Develop branch |

**Evidence:** anon-1.jsonl:1829 · comment 637771014 · PR 11901 · 2025-05-27

> | This branch |

**Evidence:** anon-1.jsonl:1829 · comment 637771014 · PR 11901 · 2025-05-27

> * When CPU is limited, the degradation is very severe, if even actual cpu it needs is not significantly higher \(limit of 300m VS actual usage when no limit of ~400-500m\)
> * Slowness can be observed even before application init, during Kamon init / Remoting init / Cluster init and akka management init
> * DB schema setup takes majority of the application init time \(with or without cpu limit\), even though we know it shouldn’t do anything cuz all the tables & indices already exist. Might be sth to take a deeper look when time allows \(?\)
> * After the http routes are initialized, the http server startup is very fast \(with or without cpu limit / with or without this change\)
> 
> ‌

## A1-1830 — Move client to bff-api test scope

**Source stance:** suggestion

**Context:**

> component: bff-api/src/main/scala/com/endowus/silver/bff/api/BffSilverClients.scala; operation: Feat/bff e4s client; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Should be already safe, but maybe we can move this to test scope of bff-api?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1850 · comment 634490774 · PR 11855 · 2025-05-19

Source path: `bff-api/src/main/scala/com/endowus/silver/bff/api/BffSilverClients.scala`

**Explicit source context (pr_title):**

> Feat/bff e4s client

**Evidence:** anon-1.jsonl:1850 · comment 634490774 · PR 11855 · 2025-05-19

Source path: `bff-api/src/main/scala/com/endowus/silver/bff/api/BffSilverClients.scala`

**Explicit source context (hunk):**

> +    with BffBaseTradingServiceE4s
> +    with BffTransactionServiceEdgeE4s
> +    with AuthServiceE4
> +
> +abstract class BffServiceClient[S <: ServiceException](
> +  override val serviceName: String,
> +  serviceExceptionFactory: ServiceExceptionFactory[S],
> +)(implicit system: ActorSystem, mat: Materializer, executionContext: ExecutionContext)
> +    extends JsonSchemaServiceClient[S](serviceName, serviceExceptionFactory) { this: BffEndpointBuilderE4s with ServiceErrorCompat.Schema =>

## A1-1886 — Test access needs only private[managers]

**Source stance:** suggestion

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioManager.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This is to add test? maybe private package is sufficient `private[managers]`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1906 · comment 632761938 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioManager.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

**Evidence:** anon-1.jsonl:1906 · comment 632761938 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioManager.scala`

**Explicit source context (hunk):**

> +        .getModelPortfolioEntityRef(portfolioId)
> +        .ask(createCmd)
> +      portfolioDto <- toDto(portfolio)
> +    } yield portfolioDto
>    }
>  
> -  private def mkPortfolioId(
> + private[managers] def mkPortfolioId(
>      portfolioType: ModelPortfolioType,

## A1-1928 — Test empty priceSource entry

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/test/scala/com/endowus/silver/marketdata/impl/db/InstrumentDailyPricesJdbcTest.scala; operation: [INV-4569] feat(marketdata): support source of price update; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add another entry with empty priceSource

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1948 · comment 667146120 · PR 12355 · 2025-08-07

Source path: `marketdata-impl/src/test/scala/com/endowus/silver/marketdata/impl/db/InstrumentDailyPricesJdbcTest.scala`

**Explicit source context (pr_title):**

> [INV-4569] feat(marketdata): support source of price update

**Evidence:** anon-1.jsonl:1948 · comment 667146120 · PR 12355 · 2025-08-07

Source path: `marketdata-impl/src/test/scala/com/endowus/silver/marketdata/impl/db/InstrumentDailyPricesJdbcTest.scala`

**Explicit source context (hunk):**

> +
> +      for {
> +        _ <- dao.createTableIfNotExists
> +        _ <- dao.upsert(data1.copy(dailyPrice = data1.dailyPrice.copy(priceSource = Some(Mstar))))
> +        _ <- dao.upsert(data12.copy(dailyPrice = data12.dailyPrice.copy(priceSource = Some(Manual))))
> +        _ <- dao.upsert(data13.copy(dailyPrice = data13.dailyPrice.copy(priceSource = None)))
> +        result <- repo.retrievePricesHavingManualPriceSource(instrument1, priceCcy)
> +        _ <- truncateTable(db)
> +      } yield {

## A1-1940 — Test plus-one-hour crosses next date after11pm and query empties

**Source stance:** observed-defect

**Context:**

> component: compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/dpm/database/DpmStatusRepositoryImplTest.scala; operation: [PG-172] feat(compliance)(customer): Fix flaky tests in SgCustomerCommunicationV2ProjectionTest and DpmStatusRepositoryImplTest; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> When run after 11pm, \+1hr will go to next date, causing the query to return empty

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1961 · comment 627678283 · PR 11745 · 2025-05-02

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/dpm/database/DpmStatusRepositoryImplTest.scala`

**Explicit source context (pr_title):**

> [PG-172] feat(compliance)(customer): Fix flaky tests in SgCustomerCommunicationV2ProjectionTest and DpmStatusRepositoryImplTest

**Evidence:** anon-1.jsonl:1961 · comment 627678283 · PR 11745 · 2025-05-02

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/dpm/database/DpmStatusRepositoryImplTest.scala`

**Explicit source context (hunk):**

> for {
>          _ <- db.run(DpmStatusRepositoryImpl.createTableIfNotExists)
>          _ <- db.run(repo.upsert(validDpmRecord))
> -        result <- repo.streamEligibleDpmStatus(createdAtStartOfDay.plusHours(1L), "RENEWAL_SUCCESS").runWith(Sink.seq)
> +        cutOffTime = List(createdAt.plusHours(1L), createdAt.toLocalDate.atTime(LocalTime.MAX).atZone(createdAt.getZone)).min
> +        result <- repo.streamEligibleDpmStatus(cutOffTime, "RENEWAL_SUCCESS").runWith(Sink.seq)
>        } yield {
>          result should contain theSameElementsAs List(
>            dpmStatusRecord(customerId = customerId, dpmStatus = validDpm)

## A1-1941 — succeed returns before inner future and leaks mock invocation into next test

**Source stance:** observed-defect

**Context:**

> component: customer-impl/src/test/scala/com/endowus/silver/customer/impl/customer/processor/SgCustomerCommunicationV2EventProcessorTest.scala; operation: [PG-172] feat(compliance)(customer): Fix flaky tests in SgCustomerCommunicationV2ProjectionTest and DpmStatusRepositoryImplTest; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This `succeed` will make the test returns successfully, without waiting for the inner future.
> 
> When next test runs, it will count towards the total invocation on brokerService mock

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1962 · comment 627678447 · PR 11745 · 2025-05-02

Source path: `customer-impl/src/test/scala/com/endowus/silver/customer/impl/customer/processor/SgCustomerCommunicationV2EventProcessorTest.scala`

**Explicit source context (pr_title):**

> [PG-172] feat(compliance)(customer): Fix flaky tests in SgCustomerCommunicationV2ProjectionTest and DpmStatusRepositoryImplTest

## A1-1996 — Advisory-to-customer named exception gains CUSTOMER_DOES_NOT_EXIST

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4275] feat(common): ServiceException propagation revisit; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ### Advisory → Customer
> 
> ```
> GET
> […incidental material or intervening source omitted…]
> ```
> 
> Before
> 
> ```
> {
>   "name" : "com.endowus.silver.customer.api.exceptions.CustomerSvcException",
>   "detail" : "Customer NotFound customerId:
> […incidental material or intervening source omitted…]
> ",
>   "error_code" : null
> }
> ```
> 
> After
> 
> ```
> {
>   "name" : "com.endowus.silver.customer.api.exceptions.CustomerSvcException",
>   "detail" : "Customer NotFound customerId:
> […incidental material or intervening source omitted…]
> ",
>   "error_code" : "CUSTOMER_DOES_NOT_EXIST"
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Customer missing gains CUSTOMER_DOES_NOT_EXIST; instrument client gains INVALID_DOCUMENT_ID; unhandled actor error becomes generic500 with correlation code.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:2017 · comment 625869319 · PR 11663 · 2025-04-28

> ### Advisory → Customer
> 
> ```
> GET

**Explicit source context (pr_title):**

> [INV-4275] feat(common): ServiceException propagation revisit

**Evidence:** anon-1.jsonl:2017 · comment 625869319 · PR 11663 · 2025-04-28

> ```
> 
> Before
> 
> ```
> {
>   "name" : "com.endowus.silver.customer.api.exceptions.CustomerSvcException",
>   "detail" : "Customer NotFound customerId:

**Evidence:** anon-1.jsonl:2017 · comment 625869319 · PR 11663 · 2025-04-28

> ",
>   "error_code" : null
> }
> ```
> 
> After
> 
> ```
> {
>   "name" : "com.endowus.silver.customer.api.exceptions.CustomerSvcException",
>   "detail" : "Customer NotFound customerId:

**Evidence:** anon-1.jsonl:2017 · comment 625869319 · PR 11663 · 2025-04-28

> ",
>   "error_code" : "CUSTOMER_DOES_NOT_EXIST"
> }
> ```
> 
> ‌

## A1-1997 — BFF instrument client error gains INVALID_DOCUMENT_ID

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4275] feat(common): ServiceException propagation revisit; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ### BFF → Instrument with client error
> 
> ```
> GET
> […incidental material or intervening source omitted…]
> ```
> 
> Before
> 
> ```
> {
>   "name" : "com.endowus.silver.instrument.api.exceptions.InstrumentSvcException",
>   "detail" : "Not allowed to download fund document with instrumentId IE00BKYBHH48 and document with Id
> […incidental material or intervening source omitted…]
> !",
>   "error_code" : null
> }
> ```
> 
> After
> 
> ```
> {
>   "name" : "com.endowus.silver.instrument.api.exceptions.InstrumentSvcException",
>   "detail" : "Not allowed to download fund document with instrumentId IE00BKYBHH48 and document with Id
> […incidental material or intervening source omitted…]
> !",
>   "error_code" : "INVALID_DOCUMENT_ID"
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Customer missing gains CUSTOMER_DOES_NOT_EXIST; instrument client gains INVALID_DOCUMENT_ID; unhandled actor error becomes generic500 with correlation code.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:2017 · comment 625869319 · PR 11663 · 2025-04-28

> ### BFF → Instrument with client error
> 
> ```
> GET

**Explicit source context (pr_title):**

> [INV-4275] feat(common): ServiceException propagation revisit

**Evidence:** anon-1.jsonl:2017 · comment 625869319 · PR 11663 · 2025-04-28

> ```
> 
> Before
> 
> ```
> {
>   "name" : "com.endowus.silver.instrument.api.exceptions.InstrumentSvcException",
>   "detail" : "Not allowed to download fund document with instrumentId IE00BKYBHH48 and document with Id

**Evidence:** anon-1.jsonl:2017 · comment 625869319 · PR 11663 · 2025-04-28

> !",
>   "error_code" : null
> }
> ```
> 
> After
> 
> ```
> {
>   "name" : "com.endowus.silver.instrument.api.exceptions.InstrumentSvcException",
>   "detail" : "Not allowed to download fund document with instrumentId IE00BKYBHH48 and document with Id

**Evidence:** anon-1.jsonl:2017 · comment 625869319 · PR 11663 · 2025-04-28

> !",
>   "error_code" : "INVALID_DOCUMENT_ID"
> }
> ```
> 
> ‌

## A1-1998 — BFF unhandled instrument actor error becomes generic server response

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4275] feat(common): ServiceException propagation revisit; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ### BFF → Instrument with server error
> 
> ```
> GET
> […incidental material or intervening source omitted…]
> ```
> 
> Instrument svc currently throws 5xx for this \(exception thrown from cmd handler, without any handling\). It’s sth we should fix, but not in scope of this PR
> 
> Before
> 
> ```
> {
>   "name" : "akka.pattern.StatusReply$ErrorMessage: Unable to perform GetInstrumentCmd, A does not exist!",
>   "detail" : "Unable to perform GetInstrumentCmd, A does not exist!\n",
>   "error_code" : null
> }
> ```
> 
> After
> 
> ```
> {
>   "name" : "Internal Server Error",
>   "detail" : "The server was unable to complete your request. Please try again later.",
>   "error_code" : "

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Customer missing gains CUSTOMER_DOES_NOT_EXIST; instrument client gains INVALID_DOCUMENT_ID; unhandled actor error becomes generic500 with correlation code.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:2017 · comment 625869319 · PR 11663 · 2025-04-28

> ### BFF → Instrument with server error
> 
> ```
> GET

**Explicit source context (pr_title):**

> [INV-4275] feat(common): ServiceException propagation revisit

**Evidence:** anon-1.jsonl:2017 · comment 625869319 · PR 11663 · 2025-04-28

> ```
> 
> Instrument svc currently throws 5xx for this \(exception thrown from cmd handler, without any handling\). It’s sth we should fix, but not in scope of this PR
> 
> Before
> 
> ```
> {
>   "name" : "akka.pattern.StatusReply$ErrorMessage: Unable to perform GetInstrumentCmd, A does not exist!",
>   "detail" : "Unable to perform GetInstrumentCmd, A does not exist!\n",
>   "error_code" : null
> }
> ```
> 
> After
> 
> ```
> {
>   "name" : "Internal Server Error",
>   "detail" : "The server was unable to complete your request. Please try again later.",
>   "error_code" : "

## A1-2043 — Flaky Circle tests stopped before proposed AsyncWordSpec change merged

**Source stance:** reported-verification

**Context:**

> component: None; operation: Use correct AsyncWordSpec in HongKongDepositAcceptedTopicSubscriberTest; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** No causal success claim supported

**Source-preserving request, proposal, or question:**

> Somehow the tests stop being flaky in Circle, even tho we haven’t merged :see_no_evil:

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:2063 · comment 657143728 · PR 12213 · 2025-07-15

**Explicit source context (pr_title):**

> Use correct AsyncWordSpec in HongKongDepositAcceptedTopicSubscriberTest

## A1-2044 — Custom operation-name interpreter cross-reference and full server/Kamon E2E test added

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4567] feat(common): Support setting endpoint's operationName; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I pushed commit [
> […incidental material or intervening source omitted…]
> to cross-ref this custom interpreter in the endpoints4s server version \+ added a e2e test case \(Kamon \+ endpoints4s \+ akka http server\) to capture this behaviour.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2064 · comment 657163041 · PR 12200 · 2025-07-15

> I pushed commit [

**Explicit source context (pr_title):**

> [INV-4567] feat(common): Support setting endpoint's operationName

**Evidence:** anon-1.jsonl:2064 · comment 657163041 · PR 12200 · 2025-07-15

> to cross-ref this custom interpreter in the endpoints4s server version \+ added a e2e test case \(Kamon \+ endpoints4s \+ akka http server\) to capture this behaviour.

## A1-2045 — Operation-name change deployed SG/HK staging services successfully

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4567] feat(common): Support setting endpoint's operationName; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Deployed various services to sg & hk staging. All are working fine. One example from trading svc

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2065 · comment 657520178 · PR 12200 · 2025-07-16

**Explicit source context (pr_title):**

> [INV-4567] feat(common): Support setting endpoint's operationName

## A1-2046 — Rebased split commit had empty diff and still worked staging

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4567] feat(common): Support setting endpoint's operationName; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Rebased and split the 1st commit. Verified git diff was empty vs origin before I push. Deployed to staging again, and change is still working as expected

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2066 · comment 658519380 · PR 12200 · 2025-07-18

**Explicit source context (pr_title):**

> [INV-4567] feat(common): Support setting endpoint's operationName

## A1-2074 — SG CoreEnhanced offering/summary performance starts Oct2020 liquid-alts inception

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-3962] feat(advisory)(compliance): Use factual performance for display if contains instruments with unreliable stitched data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ### SG CoreEnhanced
> 
> Portfolio offerings & portfolio summary both show performance from Oct2020 \(max inception of LiquidAlts\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2094 · comment 617419057 · PR 11505 · 2025-04-08

**Explicit source context (pr_title):**

> [INV-3962] feat(advisory)(compliance): Use factual performance for display if contains instruments with unreliable stitched data

## A1-2076 — SG single-fund FundSmart displays factual but common w12m for risk

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-3962] feat(advisory)(compliance): Use factual performance for display if contains instruments with unreliable stitched data; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Reported common-18% versus factual0.59%

**Source-preserving request, proposal, or question:**

> ### SG FundSmart - SingleFund
> 
> Display factual performance and use common w12m for risk tolerance
> […incidental material or intervening source omitted…]
> ‌
> 
> Here common w12m is -18% while factual w12m is 0.59%

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2096 · comment 617420692 · PR 11505 · 2025-04-08

> ### SG FundSmart - SingleFund
> 
> Display factual performance and use common w12m for risk tolerance

**Explicit source context (pr_title):**

> [INV-3962] feat(advisory)(compliance): Use factual performance for display if contains instruments with unreliable stitched data

**Evidence:** anon-1.jsonl:2096 · comment 617420692 · PR 11505 · 2025-04-08

> ‌
> 
> Here common w12m is -18% while factual w12m is 0.59%

## A1-2077 — SG multifund liquid-alts custom display with common risk w12m

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-3962] feat(advisory)(compliance): Use factual performance for display if contains instruments with unreliable stitched data; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Reported common-20.1% display4.73%; Amundi2022 stitched keeps representative; removal factual

**Source-preserving request, proposal, or question:**

> ### SG FundSmart - MultiFund with Liquid Alts
> 
> Display custom performance \(using maxInceptionDate of liquid alts\) and use common w12m for risk tolerance
> […incidental material or intervening source omitted…]
> Here common w12m is -20.1% while display w12m is 4.73%. Display performance is still representative since we are using stitched data for Amundi fund \(incepted in 2022\)
> 
> Remove Amundi fund will result in factual display performance

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2097 · comment 617422783 · PR 11505 · 2025-04-08

> ### SG FundSmart - MultiFund with Liquid Alts
> 
> Display custom performance \(using maxInceptionDate of liquid alts\) and use common w12m for risk tolerance

**Explicit source context (pr_title):**

> [INV-3962] feat(advisory)(compliance): Use factual performance for display if contains instruments with unreliable stitched data

**Evidence:** anon-1.jsonl:2097 · comment 617422783 · PR 11505 · 2025-04-08

> Here common w12m is -20.1% while display w12m is 4.73%. Display performance is still representative since we are using stitched data for Amundi fund \(incepted in 2022\)
> 
> Remove Amundi fund will result in factual display performance

## A1-2078 — SG normal multifund uses common performance for display and risk

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-3962] feat(advisory)(compliance): Use factual performance for display if contains instruments with unreliable stitched data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ### SG FundSmart - MultiFund with normal funds
> 
> Use common performance for both display and risk tolerance

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2098 · comment 617423741 · PR 11505 · 2025-04-08

**Explicit source context (pr_title):**

> [INV-3962] feat(advisory)(compliance): Use factual performance for display if contains instruments with unreliable stitched data

## A1-2079 — HK liquid-alts model uses custom; analysis custom display and common risk

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-3962] feat(advisory)(compliance): Use factual performance for display if contains instruments with unreliable stitched data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ### HK FundSmart - MultiFund with Liquid Alts
> 
> Model portfolio use custom performance
> […incidental material or intervening source omitted…]
> ‌
> 
> Portfolio analysis use custom performance for display, but common w12m for risk tolerance

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2099 · comment 617425013 · PR 11505 · 2025-04-08

> ### HK FundSmart - MultiFund with Liquid Alts
> 
> Model portfolio use custom performance

**Explicit source context (pr_title):**

> [INV-3962] feat(advisory)(compliance): Use factual performance for display if contains instruments with unreliable stitched data

**Evidence:** anon-1.jsonl:2099 · comment 617425013 · PR 11505 · 2025-04-08

> ‌
> 
> Portfolio analysis use custom performance for display, but common w12m for risk tolerance

## A1-2081 — customPeriodStartingMonth aligns factual/representative display matrix

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-3962] feat(advisory)(compliance): Use factual performance for display if contains instruments with unreliable stitched data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> After new change for `customPeriodStartingMonth`, all performance are aligned now
> 
> ‌
> 
> Single LiquidAlts \(incepted May2020\): 
> 
> | **Scenario** | **Performance** | **Screenshot** |
> | --- | --- | --- |
> | Single LiquidAlts \(incepted May2020\) | Factual performance from Jun2020 |
> […incidental material or intervening source omitted…]
> | Multi LiquidAlts \(incepted May2020\) \+ Normal Fund \(incepted before that\) | Factual performance from Jun2020 |
> […incidental material or intervening source omitted…]
> | Multi LiquidAlts \(incepted May2020\) \+ Normal Fund \(incepted after that\) | Representative performance from Jun2020 |
> […incidental material or intervening source omitted…]
> | Multi Normal Funds only | Representative performance from common |
> […incidental material or intervening source omitted…]
> | Single Normal Fund \(incepted Mar2022\) | Factual performance from Apr2022 |

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Preserve May2020→Jun2020 liquid alts and Mar2022→Apr2022 normal fund; later-incepted stitched normal fund changes representative flag.

**Evidence:** anon-1.jsonl:2101 · comment 617787202 · PR 11505 · 2025-04-09

> After new change for `customPeriodStartingMonth`, all performance are aligned now
> 
> ‌
> 
> Single LiquidAlts \(incepted May2020\): 
> 
> | **Scenario** | **Performance** | **Screenshot** |
> | --- | --- | --- |
> | Single LiquidAlts \(incepted May2020\) | Factual performance from Jun2020 |

**Explicit source context (pr_title):**

> [INV-3962] feat(advisory)(compliance): Use factual performance for display if contains instruments with unreliable stitched data

**Evidence:** anon-1.jsonl:2101 · comment 617787202 · PR 11505 · 2025-04-09

> | Multi LiquidAlts \(incepted May2020\) \+ Normal Fund \(incepted before that\) | Factual performance from Jun2020 |

**Evidence:** anon-1.jsonl:2101 · comment 617787202 · PR 11505 · 2025-04-09

> | Multi LiquidAlts \(incepted May2020\) \+ Normal Fund \(incepted after that\) | Representative performance from Jun2020 |

**Evidence:** anon-1.jsonl:2101 · comment 617787202 · PR 11505 · 2025-04-09

> | Multi Normal Funds only | Representative performance from common |

**Evidence:** anon-1.jsonl:2101 · comment 617787202 · PR 11505 · 2025-04-09

> | Single Normal Fund \(incepted Mar2022\) | Factual performance from Apr2022 |

## A1-2096 — Swagger authenticated lock versus public icon and JWT authorization verified

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4185] feat(bff): Unify BFF endpoints without assumption on which FE client app it's serving; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> In Swagger, can distinguish between authenticated \(with lock icon\) and public \(no lock\) endpoints. Clicking `Authorize` or individual locks only show the jwt

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2116 · comment 616103395 · PR 11559 · 2025-04-03

**Explicit source context (pr_title):**

> [INV-4185] feat(bff): Unify BFF endpoints without assumption on which FE client app it's serving

## A1-2097 — Swagger endpoint grouping/sorting verified

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4185] feat(bff): Unify BFF endpoints without assumption on which FE client app it's serving; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Endpoints are grouped and sorted

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:2117 · comment 616104081 · PR 11559 · 2025-04-03

**Explicit source context (pr_title):**

> [INV-4185] feat(bff): Unify BFF endpoints without assumption on which FE client app it's serving

## A1-2098 — Swagger guards displayed correctly

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4185] feat(bff): Unify BFF endpoints without assumption on which FE client app it's serving; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Guards are displayed correctly

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:2118 · comment 616104704 · PR 11559 · 2025-04-03

**Explicit source context (pr_title):**

> [INV-4185] feat(bff): Unify BFF endpoints without assumption on which FE client app it's serving

## A1-2106 — Dividend distribution succeeds with confirmed holdings and double-unit file

**Source stance:** reported-verification

**Context:**

> component: None; operation: feat(dividend): Additional validation for dividend to minimize impact of race condition with trade settlement; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ### Verify normal distribution works as usual
> 
> Create goal 1 with 100% `LU1128926307`. Settle investment on 2025-01-02. Distribute dividend with entitlement date on 2025-01-31
> […incidental material or intervening source omitted…]
> settlementConfirmedPriceDate = 2025-01-02
> […incidental material or intervening source omitted…]
> settlementConfirmedUnits = 385.604
> […incidental material or intervening source omitted…]
> settlementConfirmedPrice = 7.78
> […incidental material or intervening source omitted…]
> settlementConfirmedAmount = 3000
> […incidental material or intervening source omitted…]
> ‌
> 
> Dividend distribution file purposely contains double the unit, however we don’t validate this and purely split the dividend amount
> […incidental material or intervening source omitted…]
> ,LU1128926307,CASH,CASH,HKD,20250205,20250131,0.05,771.208,38.56,20250205,
> […incidental material or intervening source omitted…]
> ‌
> 
> Distribution is successful
> […incidental material or intervening source omitted…]
> "successfulBrokerAccountCount": 1
> […incidental material or intervening source omitted…]
> "payoutAmount": 38.56,
> […incidental material or intervening source omitted…]
> "distributionPreference": "DistributeCashBalance",

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Full raw logs not needed; preserve selected exact scenario predicates, amounts, dates, instrument and exception messages without account/customer IDs.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.
- The source prose calls the deletion preference DistributedCashBalance, while its JSON discriminator is distributionPreference=DistributeCashBalance. Both spellings are retained; no silent normalization or guaranteed outcome beyond the reported test is inferred.

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> ### Verify normal distribution works as usual
> 
> Create goal 1 with 100% `LU1128926307`. Settle investment on 2025-01-02. Distribute dividend with entitlement date on 2025-01-31

**Explicit source context (pr_title):**

> feat(dividend): Additional validation for dividend to minimize impact of race condition with trade settlement

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> settlementConfirmedPriceDate = 2025-01-02

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> settlementConfirmedUnits = 385.604

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> settlementConfirmedPrice = 7.78

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> settlementConfirmedAmount = 3000

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> ‌
> 
> Dividend distribution file purposely contains double the unit, however we don’t validate this and purely split the dividend amount

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> ,LU1128926307,CASH,CASH,HKD,20250205,20250131,0.05,771.208,38.56,20250205,

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> ‌
> 
> Distribution is successful

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "successfulBrokerAccountCount": 1

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "payoutAmount": 38.56,

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "distributionPreference": "DistributeCashBalance",

## A1-2107 — Dividend distribution rejects assumedMV versus confirmedMV mismatch

**Source stance:** reported-verification

**Context:**

> component: None; operation: feat(dividend): Additional validation for dividend to minimize impact of race condition with trade settlement; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ### Verify distribution would be blocked if assumedMV != confirmedMV
> 
> Create goal 2. However only assumed the investment on 2025-01-02
> […incidental material or intervening source omitted…]
> settlementAssumedPriceDate = 2025-01-02
> […incidental material or intervening source omitted…]
> settlementAssumedUnits = 385.604
> […incidental material or intervening source omitted…]
> settlementAssumedPrice = 7.78
> […incidental material or intervening source omitted…]
> settlementAssumedAmount = 3000
> […incidental material or intervening source omitted…]
> ‌
> 
> Distribute the same file again leads to expected error complaining about assumedMV != confirmedMV
> […incidental material or intervening source omitted…]
> c.e.s.d.i.e.d.e.DividendDistributionCalculationException: Failed to calculate dividend distribution because some plans have mismatched values between assumedMV and confirmedMV: List(
> […incidental material or intervening source omitted…]
> "successfulBrokerAccountCount": 0,
> […incidental material or intervening source omitted…]
> "payoutAmount": 38.56,
> […incidental material or intervening source omitted…]
> "distributionPreference": "DistributeCashBalance",

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Full raw logs not needed; preserve selected exact scenario predicates, amounts, dates, instrument and exception messages without account/customer IDs.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.
- The source prose calls the deletion preference DistributedCashBalance, while its JSON discriminator is distributionPreference=DistributeCashBalance. Both spellings are retained; no silent normalization or guaranteed outcome beyond the reported test is inferred.

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> ### Verify distribution would be blocked if assumedMV != confirmedMV
> 
> Create goal 2. However only assumed the investment on 2025-01-02

**Explicit source context (pr_title):**

> feat(dividend): Additional validation for dividend to minimize impact of race condition with trade settlement

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> settlementAssumedPriceDate = 2025-01-02

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> settlementAssumedUnits = 385.604

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> settlementAssumedPrice = 7.78

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> settlementAssumedAmount = 3000

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> ‌
> 
> Distribute the same file again leads to expected error complaining about assumedMV != confirmedMV

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> c.e.s.d.i.e.d.e.DividendDistributionCalculationException: Failed to calculate dividend distribution because some plans have mismatched values between assumedMV and confirmedMV: List(

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "successfulBrokerAccountCount": 0,

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "payoutAmount": 38.56,

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "distributionPreference": "DistributeCashBalance",

## A1-2108 — Dividend reprocess rejects changed split amount before processing second plan

**Source stance:** reported-verification

**Context:**

> component: None; operation: feat(dividend): Additional validation for dividend to minimize impact of race condition with trade settlement; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ### Verify distribution would be blocked if reprocess results in different amount
> 
> Confirmed settle the above settlement, and retry the processing
> 
> MV validation now passes, however distribution should continue to be blocked due to mismatched dividend amount on plan 1. Plan 2 should not proceed at all
> […incidental material or intervening source omitted…]
> c.e.s.d.i.e.d.e.DividendDistributionCalculationException: Unable to proceed with dividend distribution because the dividend amount has drifted from initial distributed amount: List(
> […incidental material or intervening source omitted…]
> "successfulBrokerAccountCount": 0,
> […incidental material or intervening source omitted…]
> "payoutAmount": 38.56,
> […incidental material or intervening source omitted…]
> "distributionPreference": "DistributeCashBalance",

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Full raw logs not needed; preserve selected exact scenario predicates, amounts, dates, instrument and exception messages without account/customer IDs.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.
- The source prose calls the deletion preference DistributedCashBalance, while its JSON discriminator is distributionPreference=DistributeCashBalance. Both spellings are retained; no silent normalization or guaranteed outcome beyond the reported test is inferred.

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> ### Verify distribution would be blocked if reprocess results in different amount
> 
> Confirmed settle the above settlement, and retry the processing
> 
> MV validation now passes, however distribution should continue to be blocked due to mismatched dividend amount on plan 1. Plan 2 should not proceed at all

**Explicit source context (pr_title):**

> feat(dividend): Additional validation for dividend to minimize impact of race condition with trade settlement

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> c.e.s.d.i.e.d.e.DividendDistributionCalculationException: Unable to proceed with dividend distribution because the dividend amount has drifted from initial distributed amount: List(

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "successfulBrokerAccountCount": 0,

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "payoutAmount": 38.56,

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "distributionPreference": "DistributeCashBalance",

## A1-2109 — Delete/retry dividend: source DistributedCashBalance versus JSON DistributeCashBalance;19.28 each

**Source stance:** reported-verification

**Context:**

> component: None; operation: feat(dividend): Additional validation for dividend to minimize impact of race condition with trade settlement; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ### Delete wrongly distributed dividend and retry succesfully
> 
> Since it is DistributedCashBalance, we can delete the dividend on plan 1 `
> […incidental material or intervening source omitted…]
> ` and retry for whole distribution. This would be successful now that no more validation errors
> […incidental material or intervening source omitted…]
> "successfulBrokerAccountCount": 1
> […incidental material or intervening source omitted…]
> "payoutAmount": 19.28,
> […incidental material or intervening source omitted…]
> "distributionPreference": "DistributeCashBalance",
> […incidental material or intervening source omitted…]
> "payoutAmount": 19.28,
> […incidental material or intervening source omitted…]
> "distributionPreference": "DistributeCashBalance",

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Full raw logs not needed; preserve selected exact scenario predicates, amounts, dates, instrument and exception messages without account/customer IDs.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.
- The source prose calls the deletion preference DistributedCashBalance, while its JSON discriminator is distributionPreference=DistributeCashBalance. Both spellings are retained; no silent normalization or guaranteed outcome beyond the reported test is inferred.

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> ### Delete wrongly distributed dividend and retry succesfully
> 
> Since it is DistributedCashBalance, we can delete the dividend on plan 1 `

**Explicit source context (pr_title):**

> feat(dividend): Additional validation for dividend to minimize impact of race condition with trade settlement

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> ` and retry for whole distribution. This would be successful now that no more validation errors

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "successfulBrokerAccountCount": 1

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "payoutAmount": 19.28,

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "distributionPreference": "DistributeCashBalance",

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "payoutAmount": 19.28,

**Evidence:** anon-1.jsonl:2126 · comment 609683987 · PR 11327 · 2025-03-17

> "distributionPreference": "DistributeCashBalance",

## A1-2162 — Retest pending recurring task at submit even if workflowId supposedly protects

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgTenantAwarePlanUpsertValidationBehaviour.scala; operation: [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> When we submit-for-approval, we need to re-validate against `hasPendingApprovalRecurringInvestmentTask`. This in theory is protected by workflow-engine, via the way we generate workflowId. So maybe we don’t need to repeat here, but let’s test this scenario

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2179 · comment 585709641 · PR 10480 · 2025-01-13

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgTenantAwarePlanUpsertValidationBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal

## A1-2186 — Unified BFF has no scheme/prefix in Swagger

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4185] feat(bff): Merge API with auth endpoints too, removing the need for /silver prefix; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No more scheme / prefix

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:2203 · comment 616480033 · PR 11568 · 2025-04-04

**Explicit source context (pr_title):**

> [INV-4185] feat(bff): Merge API with auth endpoints too, removing the need for /silver prefix

## A1-2267 — Goal performance metrics tested d56; screenshot only

**Source stance:** reported-verification

**Context:**

> component: None; operation: Feat/goal perf metrics; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Tested in d56

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:2284 · comment 608990783 · PR 11396 · 2025-03-14

**Explicit source context (pr_title):**

> Feat/goal perf metrics

## A1-2297 — Assert total count when not checking every multicurrency entry

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/test/scala/com/endowus/silver/marketdata/impl/mas/MasApiServiceV2Test.scala; operation: Feat/TT-5709 enable add mccy hk; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Add assertion on total count since we are not checking all entries?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2314 · comment 595163335 · PR 11028 · 2025-02-11

Source path: `marketdata-impl/src/test/scala/com/endowus/silver/marketdata/impl/mas/MasApiServiceV2Test.scala`

**Explicit source context (pr_title):**

> Feat/TT-5709 enable add mccy hk

**Evidence:** anon-1.jsonl:2314 · comment 595163335 · PR 11028 · 2025-02-11

Source path: `marketdata-impl/src/test/scala/com/endowus/silver/marketdata/impl/mas/MasApiServiceV2Test.scala`

**Explicit source context (hunk):**

> val hkSupportedCurrencyPairs = getSupportCurrencyPairs(LocalConfig.HongKongSupportedCurrencyList)
>          service.getFxRatesFromMasApi(hkSupportedCurrencyPairs, today).map { results =>
> -          results should contain theSameElementsAs Map(
> +          results should contain allElementsOf Map(
> +            //Cross Pairs
>              CurrencyPair(USD, HKD) -> (today, 7.82427),
> -            CurrencyPair(HKD, USD) -> (today, 0.12781)
> +            CurrencyPair(HKD, USD) -> (today, 0.12781),

## A1-2299 — Cluster-sharding eager init works in test; prior cause unclear

**Source stance:** reported-verification

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala; operation: [INV-3987] Ensure clusterSharding.init(Entity) are called first during application init; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This works. Not sure what the issue was before

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2316 · comment 598595885 · PR 11197 · 2025-02-21

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

**Explicit source context (pr_title):**

> [INV-3987] Ensure clusterSharding.init(Entity) are called first during application init

**Evidence:** anon-1.jsonl:2316 · comment 598595885 · PR 11197 · 2025-02-21

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

**Explicit source context (hunk):**

> -          _ = wire[VCStateChangeDailyTriggerTopicSubscriber]
> -        } yield ()
> -    )
> +    createCustomTopics().map { _ =>
> +      wire[CRAExpiryDailyTriggerTopicSubscriber]
> +      wire[VCStateChangeDailyTriggerTopicSubscriber]
> +    }
>    }

## A1-2338 — Eager init reduces AskTimeout during restarts but coordinator deletion still causes some

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-3987] Use akka v2.6.21. Eager init *Application via *ApplicationExtension; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Noncoordinator deletion no errors; rolling restart similar; shard distribution influences

**Source-preserving request, proposal, or question:**

> Testing completed. The change helps to reduce the AskTimeout occurrences during pod restart/deployment, however do not remove it completely.
> 
> ‌
> 
> Test setup: a simple client that repeatedly hit an endpoint that would hit an entity & interfere with the cluster while the client is running and observe any errors
> 
> ```
> execFut {
>   Source
>     .tick(1.second, 100.millis, "tick")
>     .runForeach { _ =>
>       if (counter.incrementAndGet() % 100 == 0) {
>         logger.info("Still running")
>       }
>       Source(1 to 10)
>         .map(_ => UUID.randomUUID())
>         .mapAsync(4) {
>           chargeService.getPlanProfile(_).invoke().recover {
>             case e => logger.error(s"FAILED with ${e.getMessage}")
>           }
>         }
>         .runWith(Sink.ignore)
>     }
> }
> ```
> 
> ‌
> 
> Before the change:
> 
> * Delete any node \(simulate node consolidation\) would trigger the AskTimeout errors, particularly worse if the node is currently the ShardCoordinator \(oldest node\)
> * Rolling restart \(i.e. simulate deployment\) would trigger AskTimeout errors
> 
> ‌
> 
> After the change:
> 
> * Deleting non-ShardCoordinator node does not trigger any AskTimeout errors. No errors from the ShardCoordinator either
> * Deleting ShardCoordinator node still trigger a few AskTimeout errors, however much fewer number of errors as compared to before the change. Still no errors logged by the new ShardCoordinator, so it’s likely just extra latency caused by the shard rebalancing. Indeed can observe less AskTimeout errors if deleting the node when the shard allocation is more even. Could be related to [
> […incidental material or intervening source omitted…]
> * Rolling restart exhibit similar pattern: no errors for younger nodes, fewer errors for the oldest ShardCoordinator node
> 
> ‌
> 
> I can try with the experiment to enable faster shard rebalance in next PR \([
> […incidental material or intervening source omitted…]
> introduced since v.2.6.10 with a note that it would be the new default however disabled by default, and only rebalance one shard at a time\), but I think this one is good to go.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Faster rebalance experiment next PR, historical2.6.10 default-off single-shard note.

**Evidence:** anon-1.jsonl:2356 · comment 597494111 · PR 11145 · 2025-02-18

> Testing completed. The change helps to reduce the AskTimeout occurrences during pod restart/deployment, however do not remove it completely.
> 
> ‌
> 
> Test setup: a simple client that repeatedly hit an endpoint that would hit an entity & interfere with the cluster while the client is running and observe any errors
> 
> ```
> execFut {
>   Source
>     .tick(1.second, 100.millis, "tick")
>     .runForeach { _ =>
>       if (counter.incrementAndGet() % 100 == 0) {
>         logger.info("Still running")
>       }
>       Source(1 to 10)
>         .map(_ => UUID.randomUUID())
>         .mapAsync(4) {
>           chargeService.getPlanProfile(_).invoke().recover {
>             case e => logger.error(s"FAILED with ${e.getMessage}")
>           }
>         }
>         .runWith(Sink.ignore)
>     }
> }
> ```
> 
> ‌
> 
> Before the change:
> 
> * Delete any node \(simulate node consolidation\) would trigger the AskTimeout errors, particularly worse if the node is currently the ShardCoordinator \(oldest node\)
> * Rolling restart \(i.e. simulate deployment\) would trigger AskTimeout errors
> 
> ‌
> 
> After the change:
> 
> * Deleting non-ShardCoordinator node does not trigger any AskTimeout errors. No errors from the ShardCoordinator either
> * Deleting ShardCoordinator node still trigger a few AskTimeout errors, however much fewer number of errors as compared to before the change. Still no errors logged by the new ShardCoordinator, so it’s likely just extra latency caused by the shard rebalancing. Indeed can observe less AskTimeout errors if deleting the node when the shard allocation is more even. Could be related to [

**Explicit source context (pr_title):**

> [INV-3987] Use akka v2.6.21. Eager init *Application via *ApplicationExtension

**Evidence:** anon-1.jsonl:2356 · comment 597494111 · PR 11145 · 2025-02-18

> * Rolling restart exhibit similar pattern: no errors for younger nodes, fewer errors for the oldest ShardCoordinator node
> 
> ‌
> 
> I can try with the experiment to enable faster shard rebalance in next PR \([

**Evidence:** anon-1.jsonl:2356 · comment 597494111 · PR 11145 · 2025-02-18

> introduced since v.2.6.10 with a note that it would be the new default however disabled by default, and only rebalance one shard at a time\), but I think this one is good to go.

## A1-2339 — All services started SG staging and smoke tests passed

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-3987] Use akka v2.6.21. Eager init *Application via *ApplicationExtension; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Deployed all services to SG staging. All services can come up normally and smoke tests passed [

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2357 · comment 597809454 · PR 11145 · 2025-02-19

**Explicit source context (pr_title):**

> [INV-3987] Use akka v2.6.21. Eager init *Application via *ApplicationExtension

## A1-2340 — CHINA_FI-to-FundSmart script: goal before, after, and ordered event relationships

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Reported d56 verification. Shared source caveats: * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact
> 
> Selected fields with original nesting. The stage keys below are editorial labels for the source headings “Existing entity data” and “Entity state & events after running the script”. The event array retains the source event order. UUID role labels distinguish old/new portfolio identity without exporting literal identifiers.
> 
> ```json
> {
>   "before_script": {
>     "maybeGoal": {
>       "name": "Satellite - Technology",
>       "marketRiskToleranceLevel": "CONTROLLER_GROWTH",
>       "marketRiskToleranceValue": 0.3,
>       "targetStockRatio": 0,
>       "targetStockRatioSelfSelected": false,
>       "productLineAndIntent": {
>         "_type": "SatelliteProduct",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "satelliteType": "CHINA_FI",
>         "ackRiskAdvisoryOverride": true,
>         "ackCustomerInformationAccurate": true
>       }
>     },
>     "plans": [
>       {
>         "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>         "planCcy": "SGD",
>         "initialInvestmentAmount": 0,
>         "recurringInvestmentSchedule": {
>           "interval": "MONTHLY",
>           "startingFrom": "2023-07-02",
>           "investmentAmount": 100,
>           "fundingInstructions": {
>             "_type": "PlanAccountFundingInstructions",
>             "amount": 100
>           }
>         },
>         "targetAssetAllocation": {
>           "modelPortfolioId": "[old portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "targetStockRatio": 0,
>           "targetBondRatio": 1,
>           "fundLevelFee": 0.000115,
>           "trailerFeeRebateRatio": 3.28e-05,
>           "fundLevelFeeAfterRebate": 8.22e-05,
>           "targetInstrumentWeights": {
>             "IE00BHXGRN56": {
>               "id": "IE00BHXGRN56",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.3
>             },
>             "LU1847653497": {
>               "id": "LU1847653497",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.7
>             }
>           }
>         }
>       }
>     ]
>   },
>   "after_script": {
>     "maybeGoal": {
>       "name": "Satellite - Technology",
>       "marketRiskToleranceLevel": "CONTROLLER_GROWTH",
>       "marketRiskToleranceValue": 0.3,
>       "targetStockRatio": 0,
>       "targetStockRatioSelfSelected": true,
>       "productLineAndIntent": {
>         "_type": "FundSmartProduct",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "riskToleranceValue": 0.3,
>         "acknowledgments": {
>           "fundSmartNoAdvice": true,
>           "fundSmartCustomerInformationStillAccurate": true
>         }
>       }
>     },
>     "plans": [
>       {
>         "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>         "planCcy": "SGD",
>         "initialInvestmentAmount": 0,
>         "recurringInvestmentSchedule": {
>           "interval": "MONTHLY",
>           "startingFrom": "2023-07-02",
>           "investmentAmount": 100,
>           "fundingInstructions": {
>             "_type": "PlanAccountFundingInstructions",
>             "amount": 100
>           }
>         },
>         "targetAssetAllocation": {
>           "modelPortfolioId": "[new portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "targetStockRatio": 0,
>           "targetBondRatio": 1,
>           "fundLevelFee": 0.000115,
>           "trailerFeeRebateRatio": 3.28e-05,
>           "fundLevelFeeAfterRebate": 8.22e-05,
>           "targetInstrumentWeights": {
>             "IE00BHXGRN56": {
>               "id": "IE00BHXGRN56",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.3
>             },
>             "LU1847653497": {
>               "id": "LU1847653497",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.7
>             }
>           }
>         }
>       }
>     ]
>   },
>   "events_after_script_in_source_order": [
>     {
>       "eventName": "package$PlanTargetAssetAllocationUpdatedEvt",
>       "event": {
>         "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>         "currentTaa": {
>           "modelPortfolioId": "[old portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "targetStockRatio": 0,
>           "targetBondRatio": 1,
>           "fundLevelFee": 0.000115,
>           "trailerFeeRebateRatio": 3.28e-05,
>           "fundLevelFeeAfterRebate": 8.22e-05,
>           "targetInstrumentWeights": {
>             "IE00BHXGRN56": {
>               "id": "IE00BHXGRN56",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.3
>             },
>             "LU1847653497": {
>               "id": "LU1847653497",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.7
>             }
>           }
>         },
>         "newTaa": {
>           "modelPortfolioId": "[new portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "targetStockRatio": 0,
>           "targetBondRatio": 1,
>           "fundLevelFee": 0.000115,
>           "trailerFeeRebateRatio": 3.28e-05,
>           "fundLevelFeeAfterRebate": 8.22e-05,
>           "targetInstrumentWeights": {
>             "IE00BHXGRN56": {
>               "id": "IE00BHXGRN56",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.3
>             },
>             "LU1847653497": {
>               "id": "LU1847653497",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.7
>             }
>           }
>         },
>         "requestedBy": "[identity omitted]",
>         "reason": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart"
>       }
>     },
>     {
>       "eventName": "package$GoalProductLineAndIntentModifiedEvt",
>       "event": {
>         "previousProductLineAndIntent": {
>           "_type": "SatelliteProduct",
>           "goalType": "GENERAL_WEALTH_ACCUMULATION",
>           "investmentHorizonInYears": 30,
>           "riskToleranceLevel": "CONTROLLER_GROWTH",
>           "satelliteType": "CHINA_FI",
>           "ackRiskAdvisoryOverride": true,
>           "ackCustomerInformationAccurate": true
>         },
>         "newProductLineAndIntent": {
>           "_type": "FundSmartProduct",
>           "goalType": "GENERAL_WEALTH_ACCUMULATION",
>           "investmentHorizonInYears": 30,
>           "riskToleranceLevel": "CONTROLLER_GROWTH",
>           "riskToleranceValue": 0.3,
>           "acknowledgments": {
>             "fundSmartNoAdvice": true,
>             "fundSmartCustomerInformationStillAccurate": true
>           }
>         }
>       }
>     },
>     {
>       "eventName": "package$GoalProductLineAndIntentModifiedEvt",
>       "event": {
>         "previousProductLineAndIntent": {
>           "_type": "FundSmartProduct",
>           "goalType": "GENERAL_WEALTH_ACCUMULATION",
>           "investmentHorizonInYears": 30,
>           "riskToleranceLevel": "CONTROLLER_GROWTH",
>           "riskToleranceValue": 0.3,
>           "acknowledgments": {
>             "fundSmartNoAdvice": true,
>             "fundSmartCustomerInformationStillAccurate": true
>           }
>         },
>         "newProductLineAndIntent": {
>           "_type": "FundSmartProduct",
>           "goalType": "GENERAL_WEALTH_ACCUMULATION",
>           "investmentHorizonInYears": 30,
>           "riskToleranceLevel": "CONTROLLER_GROWTH",
>           "riskToleranceValue": 0.3,
>           "acknowledgments": {
>             "fundSmartNoAdvice": true,
>             "fundSmartCustomerInformationStillAccurate": true
>           }
>         },
>         "requestedBy": "[identity omitted]",
>         "reason": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart"
>       }
>     },
>     {
>       "eventName": "package$GoalTargetStockRatioUpdatedEvt",
>       "event": {
>         "newTargetStockRatio": 0,
>         "newTargetStockRatioSelfSelected": true,
>         "newTargetStockRatioDescription": "Fund Smart portfolio for [identity omitted] for Satellite - Technology (GENERAL_WEALTH_ACCUMULATION)",
>         "newMarketRiskToleranceLevel": "CONTROLLER_GROWTH",
>         "newMarketRiskToleranceValue": 0.3,
>         "requestedBy": "[identity omitted]",
>         "reason": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart"
>       }
>     }
>   ]
> }
> ```

**Conditions and limits:**

- Historical reported verification in d56; the displayed JSON is an editorial selected-field view, not a verbatim complete dump and not a recommended current migration procedure.
- The source effective date differs from prod because this d56 fixture was created later. Its goal name remained Satellite - Technology after a Technology-to-ChineFI modification; the source explicitly keeps that misleading name intact.
- before_script and after_script correspond to source headings Existing entity data and Entity state & events after running the script. The events_after_script_in_source_order array preserves the source event order and each event payload nesting, including previous/current/new object roles.
- Old/new portfolio identity labels are editorial replacements for incidental UUID values. The same old and new identities recur across goal, rebalance, trading and charge; no literal entity/customer/account UUID is exported.
- The effectiveDate2023-02-16, IE00BHXGRN56 weight0.3, LU1847653497 weight0.7, risk values, acknowledgement fields and recurring100 values remain source-specific. Unchanged repetitive state and descriptive fund metadata are omitted from the selected view.
- Exact coherent source member/event spans support the selected view; excerpt_scope is an editorial source-section locator and is not quoted source wording.

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "marketRiskToleranceValue": 0.3

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "targetStockRatioSelfSelected": false

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "productLineAndIntent": {
>                 "_type": "SatelliteProduct",
>                 "goalType": "GENERAL_WEALTH_ACCUMULATION",
>                 "investmentHorizonInYears": 30,
>                 "riskToleranceLevel": "CONTROLLER_GROWTH",
>                 "satelliteType": "CHINA_FI",
>                 "ackRiskAdvisoryOverride": true,
>                 "ackCustomerInformationAccurate": true
>             }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "recurringInvestmentSchedule": {
>                     "interval": "MONTHLY",
>                     "startingFrom": "2023-07-02",
>                     "investmentAmount": 100,
>                     "fundingInstructions": {
>                         "_type": "PlanAccountFundingInstructions",
>                         "amount": 100
>                     }
>                 }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "targetAssetAllocation": {
>                     "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                     "modelPortfolioName": "China Fixed Income",
>                     "effectiveDate": "2023-02-16",
>                     "targetStockRatio": 0,
>                     "targetBondRatio": 1,
>                     "fundLevelFee": 0.000115,
>                     "trailerFeeRebateRatio": 0.0000328,
>                     "fundLevelFeeAfterRebate": 0.0000822,
>                     "targetInstrumentWeights": {
>                         "IE00BHXGRN56": {
>                             "id": "IE00BHXGRN56",
>                             "name": "Neuberger Berman China Bond Fund",
>                             "instrumentType": "FIXED_INCOME_FUND",
>                             "instrumentCcy": "SGD",
>                             "description": "The Fund aims to achieve a target average return of 3% over the benchmark before fees over a market cycle by primarily investing in fixed income instruments issued in the Chinese local currency markets.",
>                             "trailerFeeRebateRatio": 0.000065,
>                             "expenseRatio": 0.00015,
>                             "targetStockRatio": 0,
>                             "targetBondRatio": 1,
>                             "targetWeight": 0.3
>                         },
>                         "LU1847653497": {
>                             "id": "LU1847653497",
>                             "name": "BlackRock BGF China Bond Fund",
>                             "instrumentType": "FIXED_INCOME_FUND",
>                             "instrumentCcy": "SGD",
>                             "description": "The Fund seeks to maximise total return by investing at least 70% of its total assets in fixed income transferable securities denominated in Renminbi or other non-Chinese domestic currencies issued by entities exercising the predominant part of their economic activity in the PRC.",
>                             "trailerFeeRebateRatio": 0.000019,
>                             "expenseRatio": 0.0001,
>                             "targetStockRatio": 0,
>                             "targetBondRatio": 1,
>                             "targetWeight": 0.7
>                         }
>                     }
>                 }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "marketRiskToleranceValue": 0.3

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "targetStockRatioSelfSelected": true

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "productLineAndIntent": {
>                 "_type": "FundSmartProduct",
>                 "goalType": "GENERAL_WEALTH_ACCUMULATION",
>                 "investmentHorizonInYears": 30,
>                 "riskToleranceLevel": "CONTROLLER_GROWTH",
>                 "riskToleranceValue": 0.3,
>                 "acknowledgments": {
>                     "fundSmartNoAdvice": true,
>                     "fundSmartCustomerInformationStillAccurate": true
>                 }
>             }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "recurringInvestmentSchedule": {
>                     "interval": "MONTHLY",
>                     "startingFrom": "2023-07-02",
>                     "investmentAmount": 100,
>                     "fundingInstructions": {
>                         "_type": "PlanAccountFundingInstructions",
>                         "amount": 100
>                     }
>                 }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "targetAssetAllocation": {
>                     "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                     "modelPortfolioName": "Fund Smart portfolio for

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> for goal Satellite - Technology (seed

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> )",
>                     "effectiveDate": "2023-02-16",
>                     "targetStockRatio": 0,
>                     "targetBondRatio": 1,
>                     "fundLevelFee": 0.000115,
>                     "trailerFeeRebateRatio": 0.0000328,
>                     "fundLevelFeeAfterRebate": 0.0000822,
>                     "targetInstrumentWeights": {
>                         "IE00BHXGRN56": {
>                             "id": "IE00BHXGRN56",
>                             "name": "Neuberger Berman China Bond Fund",
>                             "instrumentType": "FIXED_INCOME_FUND",
>                             "instrumentCcy": "SGD",
>                             "description": "The Fund aims to achieve a target average return of 3% over the benchmark before fees over a market cycle by primarily investing in fixed income instruments issued in the Chinese local currency markets.",
>                             "trailerFeeRebateRatio": 0.000065,
>                             "expenseRatio": 0.00015,
>                             "targetStockRatio": 0,
>                             "targetBondRatio": 1,
>                             "targetWeight": 0.3
>                         },
>                         "LU1847653497": {
>                             "id": "LU1847653497",
>                             "name": "BlackRock BGF China Bond Fund",
>                             "instrumentType": "FIXED_INCOME_FUND",
>                             "instrumentCcy": "SGD",
>                             "description": "The Fund seeks to maximise total return by investing at least 70% of its total assets in fixed income transferable securities denominated in Renminbi or other non-Chinese domestic currencies issued by entities exercising the predominant part of their economic activity in the PRC.",
>                             "trailerFeeRebateRatio": 0.000019,
>                             "expenseRatio": 0.0001,
>                             "targetStockRatio": 0,
>                             "targetBondRatio": 1,
>                             "targetWeight": 0.7
>                         }
>                     }
>                 }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "package$PlanTargetAssetAllocationUpdatedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "currentTaa": {
>         "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "modelPortfolioName": "China Fixed Income",
>         "effectiveDate": "2023-02-16",
>         "targetStockRatio": 0,
>         "targetBondRatio": 1,
>         "fundLevelFee": 0.000115,
>         "trailerFeeRebateRatio": 0.0000328,
>         "fundLevelFeeAfterRebate": 0.0000822,
>         "targetInstrumentWeights": {
>           "IE00BHXGRN56": {
>             "id": "IE00BHXGRN56",
>             "name": "Neuberger Berman China Bond Fund",
>             "instrumentType": "FIXED_INCOME_FUND",
>             "instrumentCcy": "SGD",
>             "description": "The Fund aims to achieve a target average return of 3% over the benchmark before fees over a market cycle by primarily investing in fixed income instruments issued in the Chinese local currency markets.",
>             "trailerFeeRebateRatio": 0.000065,
>             "expenseRatio": 0.00015,
>             "targetStockRatio": 0,
>             "targetBondRatio": 1,
>             "targetWeight": 0.3
>           },
>           "LU1847653497": {
>             "id": "LU1847653497",
>             "name": "BlackRock BGF China Bond Fund",
>             "instrumentType": "FIXED_INCOME_FUND",
>             "instrumentCcy": "SGD",
>             "description": "The Fund seeks to maximise total return by investing at least 70% of its total assets in fixed income transferable securities denominated in Renminbi or other non-Chinese domestic currencies issued by entities exercising the predominant part of their economic activity in the PRC.",
>             "trailerFeeRebateRatio": 0.000019,
>             "expenseRatio": 0.0001,
>             "targetStockRatio": 0,
>             "targetBondRatio": 1,
>             "targetWeight": 0.7
>           }
>         }
>       },
>       "newTaa": {
>         "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "modelPortfolioName": "Fund Smart portfolio for

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> for goal Satellite - Technology (seed

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> )",
>         "effectiveDate": "2023-02-16",
>         "targetStockRatio": 0,
>         "targetBondRatio": 1,
>         "fundLevelFee": 0.000115,
>         "trailerFeeRebateRatio": 0.0000328,
>         "fundLevelFeeAfterRebate": 0.0000822,
>         "targetInstrumentWeights": {
>           "IE00BHXGRN56": {
>             "id": "IE00BHXGRN56",
>             "name": "Neuberger Berman China Bond Fund",
>             "instrumentType": "FIXED_INCOME_FUND",
>             "instrumentCcy": "SGD",
>             "description": "The Fund aims to achieve a target average return of 3% over the benchmark before fees over a market cycle by primarily investing in fixed income instruments issued in the Chinese local currency markets.",
>             "trailerFeeRebateRatio": 0.000065,
>             "expenseRatio": 0.00015,
>             "targetStockRatio": 0,
>             "targetBondRatio": 1,
>             "targetWeight": 0.3
>           },
>           "LU1847653497": {
>             "id": "LU1847653497",
>             "name": "BlackRock BGF China Bond Fund",
>             "instrumentType": "FIXED_INCOME_FUND",
>             "instrumentCcy": "SGD",
>             "description": "The Fund seeks to maximise total return by investing at least 70% of its total assets in fixed income transferable securities denominated in Renminbi or other non-Chinese domestic currencies issued by entities exercising the predominant part of their economic activity in the PRC.",
>             "trailerFeeRebateRatio": 0.000019,
>             "expenseRatio": 0.0001,
>             "targetStockRatio": 0,
>             "targetBondRatio": 1,
>             "targetWeight": 0.7
>           }
>         }
>       },
>       "requestedBy": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "reason": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "package$GoalProductLineAndIntentModifiedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "planIds": [
>         "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "
>       ],
>       "previousProductLineAndIntent": {
>         "_type": "SatelliteProduct",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "satelliteType": "CHINA_FI",
>         "ackRiskAdvisoryOverride": true,
>         "ackCustomerInformationAccurate": true
>       },
>       "newProductLineAndIntent": {
>         "_type": "FundSmartProduct",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "riskToleranceValue": 0.3,
>         "acknowledgments": {
>           "fundSmartNoAdvice": true,
>           "fundSmartCustomerInformationStillAccurate": true
>         }
>       },
>       "modifiedAt": "2025-03-04T16:38:47.366712412+08:00[Asia/Singapore]"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "package$GoalProductLineAndIntentModifiedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "planIds": [
>         "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "
>       ],
>       "previousProductLineAndIntent": {
>         "_type": "FundSmartProduct",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "riskToleranceValue": 0.3,
>         "acknowledgments": {
>           "fundSmartNoAdvice": true,
>           "fundSmartCustomerInformationStillAccurate": true
>         }
>       },
>       "newProductLineAndIntent": {
>         "_type": "FundSmartProduct",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "riskToleranceValue": 0.3,
>         "acknowledgments": {
>           "fundSmartNoAdvice": true,
>           "fundSmartCustomerInformationStillAccurate": true
>         }
>       },
>       "modifiedAt": "2025-03-04T16:38:47.438340959+08:00[Asia/Singapore]",
>       "requestedBy": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "reason": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "package$GoalTargetStockRatioUpdatedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "newTargetStockRatio": 0,
>       "newTargetStockRatioSelfSelected": true,
>       "newTargetStockRatioDescription": "Fund Smart portfolio for

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> for Satellite - Technology (GENERAL_WEALTH_ACCUMULATION)",
>       "newMarketRiskToleranceLevel": "CONTROLLER_GROWTH",
>       "newMarketRiskToleranceValue": 0.3,
>       "requestedBy": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "reason": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

**Explicit source context (pr_title):**

> [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script

## A1-2341 — CHINA_FI-to-FundSmart script: rebalance before, after, and ordered event relationships

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Reported d56 verification. Shared source caveats: * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact
> 
> Selected fields with original nesting. The stage keys below are editorial labels for the source headings “Existing entity data” and “Entity state & events after running the script”. The event array retains the source event order. UUID role labels distinguish old/new portfolio identity without exporting literal identifiers.
> 
> ```json
> {
>   "before_script": {
>     "plan": {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "currentTaa": {
>         "portfolioId": "[old portfolio identity omitted]",
>         "effectiveDate": "2023-02-16",
>         "instrumentWeights": {
>           "IE00BHXGRN56": 0.3,
>           "LU1847653497": 0.7
>         }
>       },
>       "config": {
>         "rebalancingEnabled": true,
>         "strategy": "THRESHOLD_BASED_STRATEGY"
>       },
>       "isDiscretionaryPortfolio": false
>     }
>   },
>   "after_script": {
>     "plan": {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "currentTaa": {
>         "portfolioId": "[new portfolio identity omitted]",
>         "effectiveDate": "2023-02-16",
>         "instrumentWeights": {
>           "IE00BHXGRN56": 0.3,
>           "LU1847653497": 0.7
>         }
>       },
>       "config": {
>         "rebalancingEnabled": true,
>         "strategy": "THRESHOLD_BASED_STRATEGY"
>       },
>       "isDiscretionaryPortfolio": false
>     }
>   },
>   "events_after_script_in_source_order": [
>     {
>       "eventName": "package$PlanTargetAssetAllocationChangedEvt",
>       "event": {
>         "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>         "previousTaa": {
>           "portfolioId": "[old portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "instrumentWeights": {
>             "IE00BHXGRN56": 0.3,
>             "LU1847653497": 0.7
>           }
>         },
>         "newTaa": {
>           "portfolioId": "[new portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "instrumentWeights": {
>             "IE00BHXGRN56": 0.3,
>             "LU1847653497": 0.7
>           }
>         },
>         "reasonForChange": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart",
>         "reason": "PORTFOLIO_CHANGE"
>       }
>     }
>   ]
> }
> ```

**Conditions and limits:**

- Historical reported verification in d56; the displayed JSON is an editorial selected-field view, not a verbatim complete dump and not a recommended current migration procedure.
- The source effective date differs from prod because this d56 fixture was created later. Its goal name remained Satellite - Technology after a Technology-to-ChineFI modification; the source explicitly keeps that misleading name intact.
- before_script and after_script correspond to source headings Existing entity data and Entity state & events after running the script. The events_after_script_in_source_order array preserves the source event order and each event payload nesting, including previous/current/new object roles.
- Old/new portfolio identity labels are editorial replacements for incidental UUID values. The same old and new identities recur across goal, rebalance, trading and charge; no literal entity/customer/account UUID is exported.
- The effectiveDate2023-02-16, IE00BHXGRN56 weight0.3, LU1847653497 weight0.7, risk values, acknowledgement fields and recurring100 values remain source-specific. Unchanged repetitive state and descriptive fund metadata are omitted from the selected view.
- Exact coherent source member/event spans support the selected view; excerpt_scope is an editorial source-section locator and is not quoted source wording.

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "plan": {
>             "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>             "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "planCcy": "SGD",
>             "currentTaa": {
>                 "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                 "effectiveDate": "2023-02-16",
>                 "note": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                 "instrumentWeights": {
>                     "IE00BHXGRN56": 0.3,
>                     "LU1847653497": 0.7
>                 }
>             },
>             "config": {
>                 "rebalancingEnabled": true,
>                 "strategy": "THRESHOLD_BASED_STRATEGY"
>             },
>             "isDiscretionaryPortfolio": false
>         }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "plan": {
>             "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>             "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "planCcy": "SGD",
>             "currentTaa": {
>                 "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                 "effectiveDate": "2023-02-16",
>                 "note": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart",
>                 "instrumentWeights": {
>                     "IE00BHXGRN56": 0.3,
>                     "LU1847653497": 0.7
>                 }
>             },
>             "config": {
>                 "rebalancingEnabled": true,
>                 "strategy": "THRESHOLD_BASED_STRATEGY"
>             },
>             "isDiscretionaryPortfolio": false
>         }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "package$PlanTargetAssetAllocationChangedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "planCcy": "SGD",
>       "previousTaa": {
>         "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "effectiveDate": "2023-02-16",
>         "note": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "instrumentWeights": {
>           "IE00BHXGRN56": 0.3,
>           "LU1847653497": 0.7
>         }
>       },
>       "newTaa": {
>         "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "effectiveDate": "2023-02-16",
>         "note": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart",
>         "instrumentWeights": {
>           "IE00BHXGRN56": 0.3,
>           "LU1847653497": 0.7
>         }
>       },
>       "reasonForChange": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart",
>       "reason": "PORTFOLIO_CHANGE",
>       "changedAt": "2025-03-04T16:38:55.48368178+08:00[Asia/Singapore]"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

**Explicit source context (pr_title):**

> [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script

## A1-2342 — CHINA_FI-to-FundSmart script: trading before, after, and ordered event relationships

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Reported d56 verification. Shared source caveats: * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact
> 
> Selected fields with original nesting. The stage keys below are editorial labels for the source headings “Existing entity data” and “Entity state & events after running the script”. The event array retains the source event order. UUID role labels distinguish old/new portfolio identity without exporting literal identifiers.
> 
> ```json
> {
>   "before_script": {
>     "maybeProfile": {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD"
>     },
>     "maybeTaa": {
>       "modelPortfolioId": "[old portfolio identity omitted]",
>       "effectiveDate": "2023-02-16",
>       "targetWeights": {
>         "IE00BHXGRN56": 0.3,
>         "LU1847653497": 0.7
>       }
>     }
>   },
>   "after_script": {
>     "maybeProfile": {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD"
>     },
>     "maybeTaa": {
>       "modelPortfolioId": "[new portfolio identity omitted]",
>       "effectiveDate": "2023-02-16",
>       "targetWeights": {
>         "IE00BHXGRN56": 0.3,
>         "LU1847653497": 0.7
>       }
>     }
>   },
>   "events_after_script_in_source_order": [
>     {
>       "eventName": "package$PlanTraderTaaUpdatedEvt",
>       "event": {
>         "planProfile": {
>           "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>           "planCcy": "SGD"
>         },
>         "taa": {
>           "modelPortfolioId": "[new portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "targetWeights": {
>             "IE00BHXGRN56": 0.3,
>             "LU1847653497": 0.7
>           }
>         }
>       }
>     }
>   ]
> }
> ```

**Conditions and limits:**

- Historical reported verification in d56; the displayed JSON is an editorial selected-field view, not a verbatim complete dump and not a recommended current migration procedure.
- The source effective date differs from prod because this d56 fixture was created later. Its goal name remained Satellite - Technology after a Technology-to-ChineFI modification; the source explicitly keeps that misleading name intact.
- before_script and after_script correspond to source headings Existing entity data and Entity state & events after running the script. The events_after_script_in_source_order array preserves the source event order and each event payload nesting, including previous/current/new object roles.
- Old/new portfolio identity labels are editorial replacements for incidental UUID values. The same old and new identities recur across goal, rebalance, trading and charge; no literal entity/customer/account UUID is exported.
- The effectiveDate2023-02-16, IE00BHXGRN56 weight0.3, LU1847653497 weight0.7, risk values, acknowledgement fields and recurring100 values remain source-specific. Unchanged repetitive state and descriptive fund metadata are omitted from the selected view.
- Exact coherent source member/event spans support the selected view; excerpt_scope is an editorial source-section locator and is not quoted source wording.

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "maybeProfile": {
>             "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>             "planCcy": "SGD"
>         }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "maybeTaa": {
>             "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "effectiveDate": "2023-02-16",
>             "targetWeights": {
>                 "IE00BHXGRN56": 0.3,
>                 "LU1847653497": 0.7
>             }
>         }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "maybeProfile": {
>       "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "maybeTaa": {
>       "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "effectiveDate": "2023-02-16",
>       "targetWeights": {
>         "IE00BHXGRN56": 0.3,
>         "LU1847653497": 0.7
>       }
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "package$PlanTraderTaaUpdatedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "planProfile": {
>         "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>         "planCcy": "SGD"
>       },
>       "taa": {
>         "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "effectiveDate": "2023-02-16",
>         "targetWeights": {
>           "IE00BHXGRN56": 0.3,
>           "LU1847653497": 0.7
>         }
>       }
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

**Explicit source context (pr_title):**

> [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script

## A1-2343 — CHINA_FI-to-FundSmart script: charge before, after, and ordered event relationships

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Reported d56 verification. Shared source caveats: * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact
> 
> Selected fields with original nesting. The stage keys below are editorial labels for the source headings “Existing entity data” and “Entity state & events after running the script”. The event array retains the source event order. UUID role labels distinguish old/new portfolio identity without exporting literal identifiers.
> 
> ```json
> {
>   "before_script": {
>     "profile": {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "goalType": "GENERAL_WEALTH_ACCUMULATION",
>       "productLineAndIntent": {
>         "_type": "SatelliteProductDto",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "satelliteType": "CHINA_FI",
>         "ackRiskAdvisoryOverride": true,
>         "ackCustomerInformationAccurate": true
>       },
>       "targetPortfolio": {
>         "portfolioId": "[old portfolio identity omitted]",
>         "effectiveDate": "2023-02-16",
>         "isDiyPortfolio": false
>       }
>     }
>   },
>   "after_script": {
>     "profile": {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "goalType": "GENERAL_WEALTH_ACCUMULATION",
>       "productLineAndIntent": {
>         "_type": "FundSmartProductDto",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "riskToleranceValue": 0.3,
>         "acknowledgements": {
>           "fundSmartNoAdvice": true,
>           "fundSmartCustomerInformationStillAccurate": true
>         }
>       },
>       "targetPortfolio": {
>         "portfolioId": "[new portfolio identity omitted]",
>         "effectiveDate": "2023-02-16",
>         "isDiyPortfolio": true
>       }
>     }
>   },
>   "events_after_script_in_source_order": [
>     {
>       "eventName": "FeePlanProductLineModifiedEvt",
>       "event": {
>         "previousProductLine": {
>           "_type": "SatelliteProductDto",
>           "goalType": "GENERAL_WEALTH_ACCUMULATION",
>           "investmentHorizonInYears": 30,
>           "riskToleranceLevel": "CONTROLLER_GROWTH",
>           "satelliteType": "CHINA_FI",
>           "ackRiskAdvisoryOverride": true,
>           "ackCustomerInformationAccurate": true
>         },
>         "newProductLine": {
>           "_type": "FundSmartProductDto",
>           "goalType": "GENERAL_WEALTH_ACCUMULATION",
>           "investmentHorizonInYears": 30,
>           "riskToleranceLevel": "CONTROLLER_GROWTH",
>           "riskToleranceValue": 0.3,
>           "acknowledgements": {
>             "fundSmartNoAdvice": true,
>             "fundSmartCustomerInformationStillAccurate": true
>           }
>         }
>       }
>     },
>     {
>       "eventName": "TargetPortfolioUpdatedEvt",
>       "event": {
>         "targetPortfolio": {
>           "portfolioId": "[new portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "isDiyPortfolio": true
>         }
>       }
>     }
>   ]
> }
> ```

**Conditions and limits:**

- Historical reported verification in d56; the displayed JSON is an editorial selected-field view, not a verbatim complete dump and not a recommended current migration procedure.
- The source effective date differs from prod because this d56 fixture was created later. Its goal name remained Satellite - Technology after a Technology-to-ChineFI modification; the source explicitly keeps that misleading name intact.
- before_script and after_script correspond to source headings Existing entity data and Entity state & events after running the script. The events_after_script_in_source_order array preserves the source event order and each event payload nesting, including previous/current/new object roles.
- Old/new portfolio identity labels are editorial replacements for incidental UUID values. The same old and new identities recur across goal, rebalance, trading and charge; no literal entity/customer/account UUID is exported.
- The effectiveDate2023-02-16, IE00BHXGRN56 weight0.3, LU1847653497 weight0.7, risk values, acknowledgement fields and recurring100 values remain source-specific. Unchanged repetitive state and descriptive fund metadata are omitted from the selected view.
- Exact coherent source member/event spans support the selected view; excerpt_scope is an editorial source-section locator and is not quoted source wording.

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "profile": {
>             "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>             "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "goalType": "GENERAL_WEALTH_ACCUMULATION",
>             "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "planCcy": "SGD",
>             "targetPortfolio": {
>                 "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                 "effectiveDate": "2023-02-16",
>                 "isDiyPortfolio": false
>             },
>             "productLineAndIntent": {
>                 "_type": "SatelliteProductDto",
>                 "goalType": "GENERAL_WEALTH_ACCUMULATION",
>                 "investmentHorizonInYears": 30,
>                 "riskToleranceLevel": "CONTROLLER_GROWTH",
>                 "satelliteType": "CHINA_FI",
>                 "ackRiskAdvisoryOverride": true,
>                 "ackCustomerInformationAccurate": true
>             }
>         }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "profile": {
>             "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>             "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "goalType": "GENERAL_WEALTH_ACCUMULATION",
>             "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "planCcy": "SGD",
>             "targetPortfolio": {
>                 "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                 "effectiveDate": "2023-02-16",
>                 "isDiyPortfolio": true
>             },
>             "productLineAndIntent": {
>                 "_type": "FundSmartProductDto",
>                 "goalType": "GENERAL_WEALTH_ACCUMULATION",
>                 "investmentHorizonInYears": 30,
>                 "riskToleranceLevel": "CONTROLLER_GROWTH",
>                 "riskToleranceValue": 0.3,
>                 "acknowledgements": {
>                     "fundSmartNoAdvice": true,
>                     "fundSmartCustomerInformationStillAccurate": true
>                 }
>             }
>         }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "FeePlanProductLineModifiedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "previousProductLine": {
>         "_type": "SatelliteProductDto",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "satelliteType": "CHINA_FI",
>         "ackRiskAdvisoryOverride": true,
>         "ackCustomerInformationAccurate": true
>       },
>       "newProductLine": {
>         "_type": "FundSmartProductDto",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "riskToleranceValue": 0.3,
>         "acknowledgements": {
>           "fundSmartNoAdvice": true,
>           "fundSmartCustomerInformationStillAccurate": true
>         }
>       },
>       "modifiedAt": "2025-03-04T16:38:47.366712412+08:00[Asia/Singapore]"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "TargetPortfolioUpdatedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "targetPortfolio": {
>         "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "effectiveDate": "2023-02-16",
>         "isDiyPortfolio": true
>       }
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

**Explicit source context (pr_title):**

> [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script

## A1-2397 — Add employee document and task ownership guard unit tests

**Source stance:** requested-change

**Context:**

> component: bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/Guards.scala; operation: [INV-3861] feat(bff): Review RBAC + guards settings of existing BFF endpoints; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Oops. I’ll top up the unit tests :pray:  need to add for `canActionForEmployee` / `canActionForDocument` / `canActionForTask`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2413 · comment 586725010 · PR 10888 · 2025-01-16

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/Guards.scala`

**Explicit source context (pr_title):**

> [INV-3861] feat(bff): Review RBAC + guards settings of existing BFF endpoints

## A2-0041 — SgB2bRedemptionCommunicationManager: There’s no A&B in advisor portal? At least not without a ref to specific customerId?

**Source stance:** suggestion

**Context:**

> PR 11207 ([EN-4396] feat(redemption)(communication) Support B2B redemption emails and migrate to Communicator V2), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/managers/sg/SgB2bRedemptionCommunicationManager.scala; original row 41.

**Source-preserving request, proposal, or question:**

> There’s no A&B in advisor portal? At least not without a ref to specific customerId?
> 
> Nevertheless, I think it was discussed that FA copy is intended as true copy, hence it’s ok to link to client portal here

**Conditions and limits:**

- FA copy is understood as a true copy; linking to client portal is considered acceptable.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:41 · comment 610711635 · PR 11207 · 2025-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/managers/sg/SgB2bRedemptionCommunicationManager.scala`

**Evidence:** anon-2.jsonl:41 · comment 610711635 · PR 11207 · 2025-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/managers/sg/SgB2bRedemptionCommunicationManager.scala`

**Explicit source context (pr_title):**

> [EN-4396] feat(redemption)(communication) Support B2B redemption emails and migrate to Communicator V2

## A2-0054 — SgWorkflowEngineE4s: Confirm that this should assigneeRole, and it should be optional. For our use case, we dont want to specify assigneeRole

**Source stance:** suggestion

**Context:**

> PR 10812 ([INV-3426] feat(bff, workflow-engine, advisory): Portfolio / Investment summaries), workflowengine-api/src/main/scala/com/endowus/silver/workflowengine/api/SgWorkflowEngineE4s.scala; original row 54.

**Concern stated in the source:** For this use case assigneeRole should be optional and unspecified.

**Source-preserving request, proposal, or question:**

> Confirm that this should assigneeRole, and it should be optional. For our use case, we dont want to specify assigneeRole

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:54 · comment 585704222 · PR 10812 · 2025-01-13

Source path: `workflowengine-api/src/main/scala/com/endowus/silver/workflowengine/api/SgWorkflowEngineE4s.scala`

**Evidence:** anon-2.jsonl:54 · comment 585704222 · PR 10812 · 2025-01-13

Source path: `workflowengine-api/src/main/scala/com/endowus/silver/workflowengine/api/SgWorkflowEngineE4s.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, workflow-engine, advisory): Portfolio / Investment summaries

## A2-0056 — Review: `advisory` currently already validates the input fees in both investment-summary & validation behaviours. So adding this extra logic in `charge` feels a bit redundant, e...

**Source stance:** suggestion

**Context:**

> PR 10732 (Resolve INV-3574: Adding sales fee range validations in charge svc), no inline path; original row 56.

**Concern stated in the source:** Advisory already validates fee inputs in investment-summary and validation behaviours; charge duplication is unrelated to actual fee amount calculation.

**Source-preserving request, proposal, or question:**

> `advisory` currently already validates the input fees in both investment-summary & validation behaviours. So adding this extra logic in `charge` feels a bit redundant, especially when it has nothing to do with the actual fee amount calculation itself

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:56 · comment 582763106 · PR 10732 · 2025-01-06

**Evidence:** anon-2.jsonl:56 · comment 582763106 · PR 10732 · 2025-01-06

**Explicit source context (pr_title):**

> Resolve INV-3574: Adding sales fee range validations in charge svc

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

## A2-0095 — InstrumentTransferService: Do we need to specify brokerAccountId in this cmd? Since it’s possible to have multiple broker accounts?

**Source stance:** open-question

**Context:**

> PR 11820 (TT-5817 Use case for full transfer plan out), trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/InstrumentTransferService.scala; original row 95.

**Concern stated in the source:** Multiple broker accounts can exist.

**Source-preserving request, proposal, or question:**

> Do we need to specify brokerAccountId in this cmd? Since it’s possible to have multiple broker accounts?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:95 · comment 632628854 · PR 11820 · 2025-05-14

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/InstrumentTransferService.scala`

**Evidence:** anon-2.jsonl:95 · comment 632628854 · PR 11820 · 2025-05-14

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/InstrumentTransferService.scala`

**Explicit source context (pr_title):**

> TT-5817 Use case for full transfer plan out

## A2-0104 — package: We cannot use DTO, especially other services' DTO in our domain event. It can feel clumsy at times, but always better and safer to redefine the model.

**Source stance:** explanation

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/events/package.scala; original row 104.

**Concern stated in the source:** Persisted domain events must not embed service DTOs, especially DTOs owned by other services.

**Source-preserving request, proposal, or question:**

> We cannot use DTO, especially other services' DTO in our domain event. It can feel clumsy at times, but always better and safer to redefine the model.

**Conditions and limits:**

- Do not infer that every API DTO is forbidden everywhere: this comment is specifically about DTOs inside domain events.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:104 · comment 587730434 · PR 10896 · 2025-01-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/events/package.scala`

**Evidence:** anon-2.jsonl:104 · comment 587730434 · PR 10896 · 2025-01-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/events/package.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0107 — BaseServiceLogicImpl: Take context in request payload as well. No need to make this endpoint specific for invest once

**Source stance:** suggestion

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; original row 107.

**Source-preserving request, proposal, or question:**

> Take context in request payload as well. No need to make this endpoint specific for invest once

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:107 · comment 587734418 · PR 10896 · 2025-01-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:107 · comment 587734418 · PR 10896 · 2025-01-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0117 — SgComplianceChecker: Unfortunately tenant service is not deployed in prod/staging yet. So we will need to make this dependent on env in order to not break existing flow

**Source stance:** suggestion

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/SgComplianceChecker.scala; original row 117.

**Concern stated in the source:** Tenant service has not yet reached prod/staging; unconditional use would break existing flows.

**Source-preserving request, proposal, or question:**

> Unfortunately tenant service is not deployed in prod/staging yet. So we will need to make this dependent on env in order to not break existing flow

**Conditions and limits:**

- This is a deployment-time condition; the source does not assert tenant service remains absent today.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:117 · comment 587731444 · PR 10896 · 2025-01-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/SgComplianceChecker.scala`

**Evidence:** anon-2.jsonl:117 · comment 587731444 · PR 10896 · 2025-01-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/SgComplianceChecker.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0200 — InitiateCancellationFlowCmdHandler: This `INVALID_CANCEL_ATTEMPT` is mapped to NotFound right now. It seems not used, so maybe change it to BadRequest instead?

**Source stance:** suggestion

**Context:**

> PR 10714 ([INV-3798] feat(investment): Throw error on cancellation failed in investment service), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala; original row 200.

**Concern stated in the source:** INVALID_CANCEL_ATTEMPT currently maps to NotFound; throwing always can violate expected idempotent best-effort cancellation from projections/subscribers.

**Source-preserving request, proposal, or question:**

> This `INVALID_CANCEL_ATTEMPT` is mapped to NotFound right now. It seems not used, so maybe change it to BadRequest instead?
> 
> Generally, we want these cmd to be idempotent especially when they are used in projection / kafka subscriber. I think all these use cases that trigger investment cancellation from BE \(redemption / expiry / compliance\) understand that it is best effort basis. So it’s better to expose a flag to ignore this error instead of throwing always?

**Conditions and limits:**

- Best-effort cancellation is specifically discussed for backend redemption/expiry/compliance triggers; the source proposes an ignore-error flag.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:200 · comment 580810035 · PR 10714 · 2024-12-23

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Evidence:** anon-2.jsonl:200 · comment 580810035 · PR 10714 · 2024-12-23

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3798] feat(investment): Throw error on cancellation failed in investment service

## A2-0209 — BffServiceE4s: `withAccessControl` is extension method of `AuthenticatedEndpoint`. When we reuse existing BE endpoint, we can wrap them with `authenticated`, and optionally add ...

**Source stance:** explanation

**Context:**

> PR 10301 ([AD-2061] feat(advisory-portal,bff): Added BrokerAccountCashBalances endpoint), bff-api/src/main/scala/com/endowus/silver/bff/api/BffServiceE4s.scala; original row 209.

**Source-preserving request, proposal, or question:**

> `withAccessControl` is extension method of `AuthenticatedEndpoint`. When we reuse existing BE endpoint, we can wrap them with `authenticated`, and optionally add required permission in `<FE-Client>RouteDefinitionsE4s`.
> 
> I put a README in `bff-impl` as well as some example in a route test in `BaseBffRouteDefinitionsE4sTest`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:209 · comment 563075577 · PR 10301 · 2024-11-08

Source path: `bff-api/src/main/scala/com/endowus/silver/bff/api/BffServiceE4s.scala`

**Evidence:** anon-2.jsonl:209 · comment 563075577 · PR 10301 · 2024-11-08

Source path: `bff-api/src/main/scala/com/endowus/silver/bff/api/BffServiceE4s.scala`

**Explicit source context (pr_title):**

> [AD-2061] feat(advisory-portal,bff): Added BrokerAccountCashBalances endpoint

## A2-0232 — GuardsTest: Same for this one

**Source stance:** suggestion

**Context:**

> PR 10576 ([ONB-4302][ONB-4308] B2C tenantId fallback and Not Found error for getClientById), bff-impl/src/test/scala/com/endowus/silver/bff/impl/routes/guards/GuardsTest.scala; original row 232.

**Source-preserving request, proposal, or question:**

> Same for this one

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- This is a continuation of the managerId=None/Some(random) test-splitting request in row 233; hunk supplies the FA-not-managing case.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:232 · comment 576371293 · PR 10576 · 2024-12-10

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/routes/guards/GuardsTest.scala`

**Evidence:** anon-2.jsonl:232 · comment 576371293 · PR 10576 · 2024-12-10

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/routes/guards/GuardsTest.scala`

**Explicit source context (hunk):**

> +      "fail when fa who does not manage the customer requests for them (client has managerId)" in {
>          val request: UUID = customerId
> -        val client = ClientDto(clientId = customerId, managerId = random, tenantId = tenantId)
> +        val client = ClientDto(clientId = customerId, managerId = Some(random), tenantId = tenantId)
> +        val getClientEndpoint = mock[tenantServiceClient.Endpoint[UUID, ClientDto]]
> +        when(tenantServiceClient.TenantApi.getClientById).thenReturn(getClientEndpoint)
> +        when(getClientEndpoint(request)).thenReturn(Future.successful(client))

**Evidence:** anon-2.jsonl:232 · comment 576371293 · PR 10576 · 2024-12-10

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/routes/guards/GuardsTest.scala`

**Explicit source context (pr_title):**

> [ONB-4302][ONB-4308] B2C tenantId fallback and Not Found error for getClientById

## A2-0233 — GuardsTest: Can we break this test into 2, one with `managerId = None` and another with `managerId = Some(random)`

**Source stance:** open-question

**Context:**

> PR 10576 ([ONB-4302][ONB-4308] B2C tenantId fallback and Not Found error for getClientById), bff-impl/src/test/scala/com/endowus/silver/bff/impl/routes/guards/GuardsTest.scala; original row 233.

**Source-preserving request, proposal, or question:**

> Can we break this test into 2, one with `managerId = None` and another with `managerId = Some(random)`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:233 · comment 576371044 · PR 10576 · 2024-12-10

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/routes/guards/GuardsTest.scala`

**Evidence:** anon-2.jsonl:233 · comment 576371044 · PR 10576 · 2024-12-10

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/routes/guards/GuardsTest.scala`

**Explicit source context (pr_title):**

> [ONB-4302][ONB-4308] B2C tenantId fallback and Not Found error for getClientById

## A2-0260 — Authorizer: [person] I’m trying to make the test works, but I swap the 2 logs here, it seems it was a typo. We don’t want error log on EFFECT\_DENY, and we want error log if the...

**Source stance:** observed-defect

**Context:**

> PR 10536 ([INV-3751] feat(bff): Set+Matching using resourceId), bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/Authorizer.scala; original row 260.

**Concern stated in the source:** The two log cases appear swapped: EFFECT_DENY should not log error, but a missing generated resourceId in the response should.

**Source-preserving request, proposal, or question:**

> [person] I’m trying to make the test works, but I swap the 2 logs here, it seems it was a typo. We don’t want error log on EFFECT\_DENY, and we want error log if the check result response doesn’t contain the resourceId we generate

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:260 · comment 573395584 · PR 10536 · 2024-12-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/Authorizer.scala`

> I’m trying to make the test works, but I swap the 2 logs here, it seems it was a typo. We don’t want error log on EFFECT\_DENY, and we want error log if the check result response doesn’t contain the resourceId we generate

**Evidence:** anon-2.jsonl:260 · comment 573395584 · PR 10536 · 2024-12-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/Authorizer.scala`

**Explicit source context (pr_title):**

> [INV-3751] feat(bff): Set+Matching using resourceId

## A2-0279 — PlanFeeInstructionEvents: It’s easier to track & inspect if the event capture the individual change \(potentially with context, e.g. requestedBy/reason\), rather than updating w...

**Source stance:** suggestion

**Context:**

> PR 10030 ([EN-3952] (charge) Create new PlanFeeInstructionEntity), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/ces/PlanFeeInstructionEvents.scala; original row 279.

**Concern stated in the source:** Individual change events, potentially with requestedBy/reason, are easier to inspect than whole-map replacement.

**Source-preserving request, proposal, or question:**

> It’s easier to track & inspect if the event capture the individual change \(potentially with context, e.g. requestedBy/reason\), rather than updating whole map always

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:279 · comment 552089535 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/ces/PlanFeeInstructionEvents.scala`

**Evidence:** anon-2.jsonl:279 · comment 552089535 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/ces/PlanFeeInstructionEvents.scala`

**Explicit source context (pr_title):**

> [EN-3952] (charge) Create new PlanFeeInstructionEntity

## A2-0299 — Review: Reported config-endpoint verification: cassandra-query-journal/events-by-tag/eventual-consistency-delay returned 20s before the environment override and 7s afterward. Po...

**Source stance:** reported-verification

**Context:**

> PR 10485 ([INV-3738] feat(common): Make eventual-consistency-delay configurable), no inline path; original row 299.

**Concern stated in the source:** The config endpoint reported 20s before the override and 7s after.

**Source-preserving request, proposal, or question:**

> Reported config-endpoint verification: cassandra-query-journal/events-by-tag/eventual-consistency-delay returned 20s before the environment override and 7s afterward. Pod identifiers are incidental.

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:299 · comment 571849321 · PR 10485 · 2024-11-29

> Before override env var

**Evidence:** anon-2.jsonl:299 · comment 571849321 · PR 10485 · 2024-11-29

> localhost:10002/config/cassandra-query-journal/events-by-tag/eventual-consistency-delay

**Evidence:** anon-2.jsonl:299 · comment 571849321 · PR 10485 · 2024-11-29

> 20s

**Evidence:** anon-2.jsonl:299 · comment 571849321 · PR 10485 · 2024-11-29

> After

**Evidence:** anon-2.jsonl:299 · comment 571849321 · PR 10485 · 2024-11-29

> 7s

**Evidence:** anon-2.jsonl:299 · comment 571849321 · PR 10485 · 2024-11-29

**Explicit source context (pr_title):**

> [INV-3738] feat(common): Make eventual-consistency-delay configurable

## A2-0305 — package: Maybe we make specific event for this. This `InvestmentPlanUpdatedEvt` is very generic. This event supposed to not introduce any change, while `InvestmentPlanUpdatedEvt...

**Source stance:** suggestion

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/events/package.scala; original row 305.

**Concern stated in the source:** InvestmentPlanUpdatedEvt implies arbitrary change; this backfill event is intended not to change values.

**Source-preserving request, proposal, or question:**

> Maybe we make specific event for this. This `InvestmentPlanUpdatedEvt` is very generic. This event supposed to not introduce any change, while `InvestmentPlanUpdatedEvt` means anything could have changed

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:305 · comment 570153884 · PR 10417 · 2024-11-25

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/events/package.scala`

**Evidence:** anon-2.jsonl:305 · comment 570153884 · PR 10417 · 2024-11-25

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/events/package.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0371 — InstrumentBalanceRepository: ```

**Source stance:** explanation

**Context:**

> PR 10367 ([INV-3683] feat(goal)(trading): Validate empty goal & no pending trades/transfers before goal deactivation), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/db/instrumentBalance/InstrumentBalanceRepository.scala; original row 371.

**Concern stated in the source:** Cassandra access must specify at least customerId, the partition key, to avoid an unsafe scan.

**Source-preserving request, proposal, or question:**

> ```
> PRIMARY KEY((customerId), planId, broker, accountNumber, instrumentId)
> ```
> 
> Very important to specify at least `customerId` otherwise we might cause blow up in Cassandra

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:371 · comment 564825467 · PR 10367 · 2024-11-14

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/db/instrumentBalance/InstrumentBalanceRepository.scala`

**Evidence:** anon-2.jsonl:371 · comment 564825467 · PR 10367 · 2024-11-14

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/db/instrumentBalance/InstrumentBalanceRepository.scala`

**Explicit source context (pr_title):**

> [INV-3683] feat(goal)(trading): Validate empty goal & no pending trades/transfers before goal deactivation

## A2-0375 — package: Let’s include the `SubscriptionAmountRegulation` fields too? I suppose that would be useful information, especially if we anticipate the FA will use at least our liquid...

**Source stance:** open-question

**Context:**

> PR 10184 ([INV-3559] feat(bff, advisory): Portfolio Builder Portfolio Summary), advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/fundsmart/package.scala; original row 375.

**Source-preserving request, proposal, or question:**

> Let’s include the `SubscriptionAmountRegulation` fields too? I suppose that would be useful information, especially if we anticipate the FA will use at least our liquid alts

**Conditions and limits:**

- Row 376 withdraws this subscription-regulation suggestion after Figma review; preserve the historical question rather than make it a current requirement.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:375 · comment 558136111 · PR 10184 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/fundsmart/package.scala`

**Evidence:** anon-2.jsonl:375 · comment 558136111 · PR 10184 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/fundsmart/package.scala`

**Explicit source context (pr_title):**

> [INV-3559] feat(bff, advisory): Portfolio Builder Portfolio Summary

## A2-0397 — BaseAdvisoryServiceE4s: Similar to the fund selection APIs, we can group these into

**Source stance:** suggestion

**Context:**

> PR 10183 ([INV-3558] feat(bff, advisory): Portfolio Builder Fund Details), advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala; original row 397.

**Concern stated in the source:** Similar to the fund selection APIs, we can group these into

```
// all APIs here will require Tenant from TracingContext
object TenantSpecificApi {
  val getInstrumentDetailsForFA = ...
  
  val getInstrumentDetailsForClient = ...
}

object BaseAdvisoryApi {
  val getInstrumentDetailsWithoutAuth = ...
}
```

‌

Then BFF will essentially proxy `getInstrumentDetailsForFA` and `getInstrumentDetailsForClient` as authenticated endpoint \(I will make PR so that BFF will also set CustomerId in TracingContext, in addition to TenantId\), while `getInstrumentDetailsWithoutAuth` with be proxied using public endpoint.

‌

In `BaseAdvisoryServiceImpl`, we will lookup and call corresponding logic method

* `getInstrumentDetailsForFA` should call inner logic with AI/PI investorType and tenantId as corporate profile
* `getInstrumentDetailsForClient` should call inner logic with AI/PI or Retail investorType look up from customerId, and tenantId as corporate profile
* `getInstrumentDetailsWithoutAuth` should call inner logic with Retail investorType and none as corporate profile

And the inner logic would be reusable code

‌

**Source-preserving request, proposal, or question:**

> Similar to the fund selection APIs, we can group these into
> 
> ```
> // all APIs here will require Tenant from TracingContext
> object TenantSpecificApi {
>   val getInstrumentDetailsForFA = ...
>   
>   val getInstrumentDetailsForClient = ...
> }
> 
> object BaseAdvisoryApi {
>   val getInstrumentDetailsWithoutAuth = ...
> }
> ```
> 
> ‌
> 
> Then BFF will essentially proxy `getInstrumentDetailsForFA` and `getInstrumentDetailsForClient` as authenticated endpoint \(I will make PR so that BFF will also set CustomerId in TracingContext, in addition to TenantId\), while `getInstrumentDetailsWithoutAuth` with be proxied using public endpoint.
> 
> ‌
> 
> In `BaseAdvisoryServiceImpl`, we will lookup and call corresponding logic method
> 
> * `getInstrumentDetailsForFA` should call inner logic with AI/PI investorType and tenantId as corporate profile
> * `getInstrumentDetailsForClient` should call inner logic with AI/PI or Retail investorType look up from customerId, and tenantId as corporate profile
> * `getInstrumentDetailsWithoutAuth` should call inner logic with Retail investorType and none as corporate profile
> 
> And the inner logic would be reusable code
> 
> ‌

**Conditions and limits:**

- The initial TracingContext customerId propagation proposal is revised in row 399 after Kamon/test considerations.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:397 · comment 558115007 · PR 10183 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Evidence:** anon-2.jsonl:397 · comment 558115007 · PR 10183 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> [INV-3558] feat(bff, advisory): Portfolio Builder Fund Details

## A2-0399 — BaseAdvisoryServiceE4s: Ok nvm about proxy endpoint with customerId/employeeId context propagation for now. In theory, it is possible to set them onto TracingContext, but will n...

**Source stance:** suggestion

**Context:**

> PR 10183 ([INV-3558] feat(bff, advisory): Portfolio Builder Fund Details), advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala; original row 399.

**Concern stated in the source:** TracingContext customer/employee propagation needs to work both with Kamon in containers and without it in tests; redefinition is accepted for now.

**Source-preserving request, proposal, or question:**

> Ok nvm about proxy endpoint with customerId/employeeId context propagation for now. In theory, it is possible to set them onto TracingContext, but will need to make it work in container with Kamon and in tests without Kamon, e.g. we will need to do something similar to the impl of TenantProvider.
> 
> This feels clunky for now, let’s define these endpoints as above, but we simply re-define them in BFF and set customerId/employeeId accordingly

**Conditions and limits:**

- Source explicitly accepts redefining BFF endpoints and setting customerId/employeeId for now.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:399 · comment 558261018 · PR 10183 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Evidence:** anon-2.jsonl:399 · comment 558261018 · PR 10183 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> [INV-3558] feat(bff, advisory): Portfolio Builder Fund Details

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

## A2-0414 — BaseAdvisoryServiceE4s: Should we create another API object for all these tenant specific endpoints? Their logic should extract the tenant from tracing context, and use it for c...

**Source stance:** suggestion

**Context:**

> PR 10182 ([INV-3430] feat(bff, advisory): Portfolio Builder Fund List), advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala; original row 414.

**Concern stated in the source:** Tenant-specific APIs can use tenant tracing context after BFF auth/RBAC; faId is unnecessary until any future FA-specific RF need.

**Source-preserving request, proposal, or question:**

> Should we create another API object for all these tenant specific endpoints? Their logic should extract the tenant from tracing context, and use it for corp profile lookup.
> 
> This means for now, we do not need to have `faId` in the query params. On BFF, it would be an authenticated proxy endpoints with appropriate RBAC resource. Once that passes, `advisory` just need to proceed with the tenantId.
> 
> In future, if we ever need to support fa specific RF, an optional `faId` can be added?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:414 · comment 558075298 · PR 10182 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Evidence:** anon-2.jsonl:414 · comment 558075298 · PR 10182 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> [INV-3430] feat(bff, advisory): Portfolio Builder Fund List

## A2-0419 — TenantAwareInstrumentBuilderTest: Maybe add option to set these providers in `SgAdvisoryServiceMockUtils#getService` instead of casting like this

**Source stance:** suggestion

**Context:**

> PR 10182 ([INV-3430] feat(bff, advisory): Portfolio Builder Fund List), advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilderTest.scala; original row 419.

**Source-preserving request, proposal, or question:**

> Maybe add option to set these providers in `SgAdvisoryServiceMockUtils#getService` instead of casting like this

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:419 · comment 561789749 · PR 10182 · 2024-11-06

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilderTest.scala`

**Evidence:** anon-2.jsonl:419 · comment 561789749 · PR 10182 · 2024-11-06

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilderTest.scala`

**Explicit source context (pr_title):**

> [INV-3430] feat(bff, advisory): Portfolio Builder Fund List

## A2-0422 — TenantAwareInstrumentBuilderTest: Let’s add another test for SRS or CPF. That would have failed with this PR

**Source stance:** requested-change

**Context:**

> PR 10182 ([INV-3430] feat(bff, advisory): Portfolio Builder Fund List), advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilderTest.scala; original row 422.

**Concern stated in the source:** An SRS/CPF test would fail with this PR.

**Source-preserving request, proposal, or question:**

> Let’s add another test for SRS or CPF. That would have failed with this PR

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:422 · comment 561789882 · PR 10182 · 2024-11-06

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilderTest.scala`

**Evidence:** anon-2.jsonl:422 · comment 561789882 · PR 10182 · 2024-11-06

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilderTest.scala`

**Explicit source context (pr_title):**

> [INV-3430] feat(bff, advisory): Portfolio Builder Fund List

## A2-0425 — SgInstrumentFilterManager: The logic in this manager is not SG specific AFAICS. Better we move it out to `managers` package instead of `managers.sg`

**Source stance:** suggestion

**Context:**

> PR 10182 ([INV-3430] feat(bff, advisory): Portfolio Builder Fund List), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgInstrumentFilterManager.scala; original row 425.

**Source-preserving request, proposal, or question:**

> The logic in this manager is not SG specific AFAICS. Better we move it out to `managers` package instead of `managers.sg`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:425 · comment 561768282 · PR 10182 · 2024-11-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgInstrumentFilterManager.scala`

**Evidence:** anon-2.jsonl:425 · comment 561768282 · PR 10182 · 2024-11-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgInstrumentFilterManager.scala`

**Explicit source context (pr_title):**

> [INV-3430] feat(bff, advisory): Portfolio Builder Fund List

## A2-0430 — TenantAwareInstrumentBuilder: Only need customerService as we are overriding its type to SG, otherwise we don’t need to specify these ruleService/instrumentCaches again

**Source stance:** explanation

**Context:**

> PR 10182 ([INV-3430] feat(bff, advisory): Portfolio Builder Fund List), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilder.scala; original row 430.

**Concern stated in the source:** Only customerService is overridden to SG; repeated ruleService/instrumentCache injection is unnecessary.

**Source-preserving request, proposal, or question:**

> Only need customerService as we are overriding its type to SG, otherwise we don’t need to specify these ruleService/instrumentCaches again

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:430 · comment 561767781 · PR 10182 · 2024-11-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilder.scala`

**Evidence:** anon-2.jsonl:430 · comment 561767781 · PR 10182 · 2024-11-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> [INV-3430] feat(bff, advisory): Portfolio Builder Fund List

## A2-0432 — TenantAwareInstrumentBuilderTest: I was thinking to provide easier way to override this when we create the `*ServiceLogicImpl` instead of forced changing it like this.

**Source stance:** suggestion

**Context:**

> PR 10182 ([INV-3430] feat(bff, advisory): Portfolio Builder Fund List), advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilderTest.scala; original row 432.

**Concern stated in the source:** ServiceLogic overrides are unnecessary if dynamic providers remain confined to ServiceImpl.

**Source-preserving request, proposal, or question:**

> I was thinking to provide easier way to override this when we create the `*ServiceLogicImpl` instead of forced changing it like this.
> 
> But looks like it won’t be needed if we switch back to [person]’s suggestion to look up providers only at `*ServiceImpl` layer, and keep Logic/Manager clean

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:432 · comment 562282569 · PR 10182 · 2024-11-07

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilderTest.scala`

> I was thinking to provide easier way to override this when we create the `*ServiceLogicImpl` instead of forced changing it like this.
> 
> But looks like it won’t be needed if we switch back to

**Evidence:** anon-2.jsonl:432 · comment 562282569 · PR 10182 · 2024-11-07

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilderTest.scala`

> ’s suggestion to look up providers only at `*ServiceImpl` layer, and keep Logic/Manager clean

**Evidence:** anon-2.jsonl:432 · comment 562282569 · PR 10182 · 2024-11-07

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/TenantAwareInstrumentBuilderTest.scala`

**Explicit source context (pr_title):**

> [INV-3430] feat(bff, advisory): Portfolio Builder Fund List

## A2-0469 — BffServiceImpl: In on-behalf operations:

**Source stance:** suggestion

**Context:**

> PR 10258 ([INV-3639] feat(bff): Capture and propagate Customer/Employee context in BFF), bff-impl/src/main/scala/com/endowus/silver/bff/impl/BffServiceImpl.scala; original row 469.

**Concern stated in the source:** In on-behalf operations:

* auth user would be employee, which we would set into context using EmployeeProvider
* and the request \(either payload or query param\) should specify the customer, which we would use to validate proper ownership/relationship in guards

‌

Once it reaches the handler \(logic layer\), it is up to the domain to decide how they want to implement it. Example:

1. they could use an endpoint in BE that expects customerId in either payload or query param \(and hence we can simply reuse it completely, and define it as proxy endpoint in BFF\)
2. they could set context using CustomerProvider, and call the endpoint in BE that expects customerId from context instead \(and if not available, 500 error is rightfully thrown\)

I would prefer \(1\) instead and we stick to setting TenantId/CustomerId/EmployeeId context by auth only.

**Source-preserving request, proposal, or question:**

> In on-behalf operations:
> 
> * auth user would be employee, which we would set into context using EmployeeProvider
> * and the request \(either payload or query param\) should specify the customer, which we would use to validate proper ownership/relationship in guards
> 
> ‌
> 
> Once it reaches the handler \(logic layer\), it is up to the domain to decide how they want to implement it. Example:
> 
> 1. they could use an endpoint in BE that expects customerId in either payload or query param \(and hence we can simply reuse it completely, and define it as proxy endpoint in BFF\)
> 2. they could set context using CustomerProvider, and call the endpoint in BE that expects customerId from context instead \(and if not available, 500 error is rightfully thrown\)
> 
> I would prefer \(1\) instead and we stick to setting TenantId/CustomerId/EmployeeId context by auth only.

**Conditions and limits:**

- Two on-behalf designs are presented; the preferred one leaves auth context tied to authentication and sends target customerId explicitly in payload/query.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:469 · comment 560709898 · PR 10258 · 2024-11-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/BffServiceImpl.scala`

**Evidence:** anon-2.jsonl:469 · comment 560709898 · PR 10258 · 2024-11-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/BffServiceImpl.scala`

**Explicit source context (pr_title):**

> [INV-3639] feat(bff): Capture and propagate Customer/Employee context in BFF

## A2-0472 — Guards: The intention is since we will have the endpoints specifically for each FE application, these guards are there to allow us to validate correct endpoint is called \(espec...

**Source stance:** suggestion

**Context:**

> PR 10258 ([INV-3639] feat(bff): Capture and propagate Customer/Employee context in BFF), bff-impl/src/main/scala/com/endowus/silver/bff/impl/routes/guards/Guards.scala; original row 472.

**Concern stated in the source:** The intention is since we will have the endpoints specifically for each FE application, these guards are there to allow us to validate correct endpoint is called \(especially when RBAC alone is not sufficient\)

‌

Example: both FA and Customer can initiate a redemption request

* `/advisor-portal/redeem?customerId&goalId`

    * authenticated endpoint with access control expecting `CUSTOMER:REDEMPTION` - `Create`
    * guards require both isEmployee and managesCustomer
    
* `` `/client-portal/redeem?goalId``

    * authenticated endpoint with access control expecting `CUSTOMER:REDEMPTION` - `Create`
    * guards require isCustomer
    

‌

**Source-preserving request, proposal, or question:**

> The intention is since we will have the endpoints specifically for each FE application, these guards are there to allow us to validate correct endpoint is called \(especially when RBAC alone is not sufficient\)
> 
> ‌
> 
> Example: both FA and Customer can initiate a redemption request
> 
> * `/advisor-portal/redeem?customerId&goalId`
> 
>     * authenticated endpoint with access control expecting `CUSTOMER:REDEMPTION` - `Create`
>     * guards require both isEmployee and managesCustomer
>     
> * `` `/client-portal/redeem?goalId``
> 
>     * authenticated endpoint with access control expecting `CUSTOMER:REDEMPTION` - `Create`
>     * guards require isCustomer
>     
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:472 · comment 560714659 · PR 10258 · 2024-11-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/routes/guards/Guards.scala`

**Evidence:** anon-2.jsonl:472 · comment 560714659 · PR 10258 · 2024-11-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/routes/guards/Guards.scala`

**Explicit source context (pr_title):**

> [INV-3639] feat(bff): Capture and propagate Customer/Employee context in BFF

## A2-0479 — Review: Tested e2e flow bff swagger → bff → advisory and verified the contexts are propagated correct [<url> data-inline-card='' } 

**Source stance:** reported-verification

**Context:**

> PR 10269 ([INV-3639] feat(bff): Re-organize BFF RouteDefinitions and RoutesProvider), no inline path; original row 479.

**Source-preserving request, proposal, or question:**

> Tested e2e flow bff swagger → bff → advisory and verified the contexts are propagated correct [<url> data-inline-card='' } 
> 
> ![](<url>
> ![](<url>
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:479 · comment 560305770 · PR 10269 · 2024-11-01

**Evidence:** anon-2.jsonl:479 · comment 560305770 · PR 10269 · 2024-11-01

**Explicit source context (pr_title):**

> [INV-3639] feat(bff): Re-organize BFF RouteDefinitions and RoutesProvider

## A2-0490 — InstrumentInfoData: Also can we make one instrument having 3 asset class types, instead of both having 2 same types

**Source stance:** suggestion

**Context:**

> PR 10077 ([INV-3441] feat(composition): use instrument EndowusAssetClassType map to calculate taa and aaa), composition-impl/src/test/scala/com/endowus/silver/composition/impl/utils/InstrumentInfoData.scala; original row 490.

**Concern stated in the source:** Also can we make one instrument having 3 asset class types, instead of both having 2 same types

**Source-preserving request, proposal, or question:**

> Also can we make one instrument having 3 asset class types, instead of both having 2 same types

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:490 · comment 551485063 · PR 10077 · 2024-10-11

Source path: `composition-impl/src/test/scala/com/endowus/silver/composition/impl/utils/InstrumentInfoData.scala`

**Evidence:** anon-2.jsonl:490 · comment 551485063 · PR 10077 · 2024-10-11

Source path: `composition-impl/src/test/scala/com/endowus/silver/composition/impl/utils/InstrumentInfoData.scala`

**Explicit source context (pr_title):**

> [INV-3441] feat(composition): use instrument EndowusAssetClassType map to calculate taa and aaa

## A2-0492 — InstrumentInfoData: Can add dependency `` `instrument-api` % "test->test"``, and use `InstrumentV2TestData` instead

**Source stance:** suggestion

**Context:**

> PR 10077 ([INV-3441] feat(composition): use instrument EndowusAssetClassType map to calculate taa and aaa), composition-impl/src/test/scala/com/endowus/silver/composition/impl/utils/InstrumentInfoData.scala; original row 492.

**Source-preserving request, proposal, or question:**

> Can add dependency `` `instrument-api` % "test->test"``, and use `InstrumentV2TestData` instead

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:492 · comment 551484801 · PR 10077 · 2024-10-11

Source path: `composition-impl/src/test/scala/com/endowus/silver/composition/impl/utils/InstrumentInfoData.scala`

**Evidence:** anon-2.jsonl:492 · comment 551484801 · PR 10077 · 2024-10-11

Source path: `composition-impl/src/test/scala/com/endowus/silver/composition/impl/utils/InstrumentInfoData.scala`

**Explicit source context (pr_title):**

> [INV-3441] feat(composition): use instrument EndowusAssetClassType map to calculate taa and aaa

## A2-0493 — InstrumentV2TestData: Let’s keep this very simple, and add `withAssetClassAllocation` in `InstrumentV2TestDataExt` instead

**Source stance:** suggestion

**Context:**

> PR 10077 ([INV-3441] feat(composition): use instrument EndowusAssetClassType map to calculate taa and aaa), instrument-api/src/test/scala/com/endowus/silver/instrument/api/testdata/InstrumentV2TestData.scala; original row 493.

**Source-preserving request, proposal, or question:**

> Let’s keep this very simple, and add `withAssetClassAllocation` in `InstrumentV2TestDataExt` instead

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:493 · comment 551538981 · PR 10077 · 2024-10-11

Source path: `instrument-api/src/test/scala/com/endowus/silver/instrument/api/testdata/InstrumentV2TestData.scala`

**Evidence:** anon-2.jsonl:493 · comment 551538981 · PR 10077 · 2024-10-11

Source path: `instrument-api/src/test/scala/com/endowus/silver/instrument/api/testdata/InstrumentV2TestData.scala`

**Explicit source context (pr_title):**

> [INV-3441] feat(composition): use instrument EndowusAssetClassType map to calculate taa and aaa

## A2-0494 — SgAdvisedPortfolioOfferingsManager: After you’re done with e2e testing, let’s put a cache here, similar to `AdvisedPortfolioPerformanceCache`

**Source stance:** suggestion

**Context:**

> PR 10077 ([INV-3441] feat(composition): use instrument EndowusAssetClassType map to calculate taa and aaa), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioOfferingsManager.scala; original row 494.

**Concern stated in the source:** After you’re done with e2e testing, let’s put a cache here, similar to `AdvisedPortfolioPerformanceCache`

**Source-preserving request, proposal, or question:**

> After you’re done with e2e testing, let’s put a cache here, similar to `AdvisedPortfolioPerformanceCache`

**Conditions and limits:**

- Cache is requested only after end-to-end testing completes.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:494 · comment 551539508 · PR 10077 · 2024-10-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioOfferingsManager.scala`

**Evidence:** anon-2.jsonl:494 · comment 551539508 · PR 10077 · 2024-10-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioOfferingsManager.scala`

**Explicit source context (pr_title):**

> [INV-3441] feat(composition): use instrument EndowusAssetClassType map to calculate taa and aaa

## A2-0512 — SgPlanUpsertPortfolioSummaryBehaviourTest: check not empty instead?

**Source stance:** open-question

**Context:**

> PR 10156 ([INV-3237] feat(advisory): add instruments in upsert portfolio summary api), advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertPortfolioSummaryBehaviourTest.scala; original row 512.

**Source-preserving request, proposal, or question:**

> check not empty instead?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:512 · comment 552252068 · PR 10156 · 2024-10-14

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertPortfolioSummaryBehaviourTest.scala`

**Evidence:** anon-2.jsonl:512 · comment 552252068 · PR 10156 · 2024-10-14

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertPortfolioSummaryBehaviourTest.scala`

**Explicit source context (pr_title):**

> [INV-3237] feat(advisory): add instruments in upsert portfolio summary api

## A2-0534 — HkFeeManagerEntityTest: We don’t need this test cuz there is no split logic at entity level?

**Source stance:** open-question

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/test/scala/com/endowus/silver/charge/impl/HkFeeManagerEntityTest.scala; original row 534.

**Concern stated in the source:** We don’t need this test cuz there is no split logic at entity level?

**Source-preserving request, proposal, or question:**

> We don’t need this test cuz there is no split logic at entity level?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:534 · comment 549740654 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/HkFeeManagerEntityTest.scala`

**Evidence:** anon-2.jsonl:534 · comment 549740654 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/HkFeeManagerEntityTest.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0537 — HkFeeManagerEntityTest: There is no logical change in the entity/cmd handler. It’s better to have the waiver bit injected, and keep the existing test in tact. Then you can unit ...

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/test/scala/com/endowus/silver/charge/impl/HkFeeManagerEntityTest.scala; original row 537.

**Concern stated in the source:** There is no logical change in the entity/cmd handler. It’s better to have the waiver bit injected, and keep the existing test in tact. Then you can unit test the waiver limit in isolation

**Source-preserving request, proposal, or question:**

> There is no logical change in the entity/cmd handler. It’s better to have the waiver bit injected, and keep the existing test in tact. Then you can unit test the waiver limit in isolation

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:537 · comment 549763340 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/HkFeeManagerEntityTest.scala`

**Evidence:** anon-2.jsonl:537 · comment 549763340 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/HkFeeManagerEntityTest.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0542 — HkEstimateFeeGoalModifyBehaviourTest: This test was expecting to return tier 2 of 0.0035…. so either we update the test name to “ranked fee 3”, or we update the existing MV so t...

**Source stance:** explanation

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/test/scala/com/endowus/silver/charge/impl/productline/hk/HkEstimateFeeGoalModifyBehaviourTest.scala; original row 542.

**Concern stated in the source:** This test was expecting to return tier 2 of 0.0035…. so either we update the test name to “ranked fee 3”, or we update the existing MV so that returned fee is 0.0035

**Source-preserving request, proposal, or question:**

> This test was expecting to return tier 2 of 0.0035…. so either we update the test name to “ranked fee 3”, or we update the existing MV so that returned fee is 0.0035

**Conditions and limits:**

- The test expects fee tier 2 rate 0.0035; either rename to ranked fee 3 or change MV to yield 0.0035.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:542 · comment 550150814 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/productline/hk/HkEstimateFeeGoalModifyBehaviourTest.scala`

**Evidence:** anon-2.jsonl:542 · comment 550150814 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/productline/hk/HkEstimateFeeGoalModifyBehaviourTest.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0553 — ProductPortfolioHelper: We should log `specified style` instead of `specified risk tolerance` here

**Source stance:** suggestion

**Context:**

> PR 10043 ([INV-3488] feat(advisory, charge): Enable portfolio (for advisory flow) and investment summaries (for execution only flow)), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ProductPortfolioHelper.scala; original row 553.

**Concern stated in the source:** We should log `specified style` instead of `specified risk tolerance` here

**Source-preserving request, proposal, or question:**

> We should log `specified style` instead of `specified risk tolerance` here

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:553 · comment 550427157 · PR 10043 · 2024-10-09

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ProductPortfolioHelper.scala`

**Evidence:** anon-2.jsonl:553 · comment 550427157 · PR 10043 · 2024-10-09

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ProductPortfolioHelper.scala`

**Explicit source context (pr_title):**

> [INV-3488] feat(advisory, charge): Enable portfolio (for advisory flow) and investment summaries (for execution only flow)

## A2-0567 — GoalCreateBehaviourHelpers: Ok to throw for now. We can either make this specific to B2C, or make it generic and default some values for B2B

**Source stance:** suggestion

**Context:**

> PR 10010 (Feat/INV-3472 b2b product line), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/GoalCreateBehaviourHelpers.scala; original row 567.

**Concern stated in the source:** Ok to throw for now. We can either make this specific to B2C, or make it generic and default some values for B2B

**Source-preserving request, proposal, or question:**

> Ok to throw for now. We can either make this specific to B2C, or make it generic and default some values for B2B

**Conditions and limits:**

- Throwing is accepted for now; B2C-only versus generic-with-B2B-defaults remains a future option.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:567 · comment 545907848 · PR 10010 · 2024-09-26

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/GoalCreateBehaviourHelpers.scala`

**Evidence:** anon-2.jsonl:567 · comment 545907848 · PR 10010 · 2024-09-26

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/GoalCreateBehaviourHelpers.scala`

**Explicit source context (pr_title):**

> Feat/INV-3472 b2b product line

## A2-0568 — productline: All of these private conversion should be specific type

**Source stance:** suggestion

**Context:**

> PR 10010 (Feat/INV-3472 b2b product line), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/model/productline/productline.scala; original row 568.

**Source-preserving request, proposal, or question:**

> All of these private conversion should be specific type

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:568 · comment 545902660 · PR 10010 · 2024-09-26

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/model/productline/productline.scala`

**Evidence:** anon-2.jsonl:568 · comment 545902660 · PR 10010 · 2024-09-26

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/model/productline/productline.scala`

**Explicit source context (pr_title):**

> Feat/INV-3472 b2b product line

## A2-0570 — package: Maybe we don’t add this yet, cuz as of now, we would only return the specific B2B/B2C type to FE \(since they have separate apps\)

**Source stance:** suggestion

**Context:**

> PR 10010 (Feat/INV-3472 b2b product line), goal-api/src/main/scala/com/endowus/silver/goal/api/models/goal/package.scala; original row 570.

**Concern stated in the source:** Maybe we don’t add this yet, cuz as of now, we would only return the specific B2B/B2C type to FE \(since they have separate apps\)

**Source-preserving request, proposal, or question:**

> Maybe we don’t add this yet, cuz as of now, we would only return the specific B2B/B2C type to FE \(since they have separate apps\)

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:570 · comment 545905092 · PR 10010 · 2024-09-26

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/models/goal/package.scala`

**Evidence:** anon-2.jsonl:570 · comment 545905092 · PR 10010 · 2024-09-26

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/models/goal/package.scala`

**Explicit source context (pr_title):**

> Feat/INV-3472 b2b product line

## A2-0599 — BaseBffServiceImplCorsTest: Oops I missed this. Can you help me fix in this PR too, just need to explicitly set it for the test

**Source stance:** suggestion

**Context:**

> PR 10031 (RBAC for new BFF), bff-impl/src/test/scala/com/endowus/silver/bff/impl/BaseBffServiceImplCorsTest.scala; original row 599.

**Source-preserving request, proposal, or question:**

> Oops I missed this. Can you help me fix in this PR too, just need to explicitly set it for the test
> 
> ```
> class BffServiceImplCorsTest extends BaseBffServiceImplCorsTest {
> 
>   override def testConfigSource: String = "akka-http-cors.allowed-origins-with-wildcard-port=[]," + super.testConfigSource
>   
>   ...
>   
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:599 · comment 544061874 · PR 10031 · 2024-09-23

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/BaseBffServiceImplCorsTest.scala`

**Evidence:** anon-2.jsonl:599 · comment 544061874 · PR 10031 · 2024-09-23

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/BaseBffServiceImplCorsTest.scala`

**Explicit source context (pr_title):**

> RBAC for new BFF

## A2-0613 — Review: Local testing

**Source stance:** reported-verification

**Context:**

> PR 9928 ([INV-3372] feat(bff): Expose swagger on akka management port), no inline path; original row 613.

**Concern stated in the source:** Local testing

Able to start up BFF and dummy endpoint works \(note that BffApplication is used twice, but init only once\)

![](<url>
‌

![](<url>
‌

Swagger UI and openapi.json files are accessible on port 10002 \(requests to fetch openapi.json are not intercepted\)

![](<url>
‌

“Try it out” requests are intercepted correctly to change to port 10000

![](<url>
‌

E2E using local BFF connecting to remote BE services still doesn’t work yet:

* Setting SERVICES\_DOMAIN to `.silver.d56.dynamic.sg.endow.us` in some `application.override.conf` is minimum requirement
* However, we still need to support:

    * `BaseServiceClient` needs to support HTTPS \(we need this when running locally connecting to remote BE\)
    * Propagate CF header from OpenApi to BE endpoints
    

‌

**Source-preserving request, proposal, or question:**

> Local testing
> 
> Able to start up BFF and dummy endpoint works \(note that BffApplication is used twice, but init only once\)
> 
> ![](<url>
> ‌
> 
> ![](<url>
> ‌
> 
> Swagger UI and openapi.json files are accessible on port 10002 \(requests to fetch openapi.json are not intercepted\)
> 
> ![](<url>
> ‌
> 
> “Try it out” requests are intercepted correctly to change to port 10000
> 
> ![](<url>
> ‌
> 
> E2E using local BFF connecting to remote BE services still doesn’t work yet:
> 
> * Setting SERVICES\_DOMAIN to `.silver.d56.dynamic.sg.endow.us` in some `application.override.conf` is minimum requirement
> * However, we still need to support:
> 
>     * `BaseServiceClient` needs to support HTTPS \(we need this when running locally connecting to remote BE\)
>     * Propagate CF header from OpenApi to BE endpoints
>     
> 
> ‌

**Conditions and limits:**

- Local startup/swagger interception passed; local-BFF-to-remote-BE e2e still failed pending SERVICES_DOMAIN, HTTPS BaseServiceClient, and Cloudflare header propagation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:613 · comment 538597278 · PR 9928 · 2024-09-05

**Evidence:** anon-2.jsonl:613 · comment 538597278 · PR 9928 · 2024-09-05

**Explicit source context (pr_title):**

> [INV-3372] feat(bff): Expose swagger on akka management port

## A2-0614 — Review: D56 testing

**Source stance:** reported-verification

**Context:**

> PR 9928 ([INV-3372] feat(bff): Expose swagger on akka management port), no inline path; original row 614.

**Concern stated in the source:** D56 testing

Able to start up BFF and dummy endpoint works \(single init of BffApplication\)

![](<url>
![](<url>
‌

Swagger UI and openapi.json files are accessible on docs ingress.

Note: I’ll drop the bff-docs.ifa and keep only silver-bff-docs. Originally I was thinking to expose them separately, but as per last discussion, we want single place for all BFF swagger

![](<url>
![](<url>
‌

Try it out requests are intercepted correctly, and BFF successfully proxies the request to BE advisory

![](<url>
‌

**Source-preserving request, proposal, or question:**

> D56 testing
> 
> Able to start up BFF and dummy endpoint works \(single init of BffApplication\)
> 
> ![](<url>
> ![](<url>
> ‌
> 
> Swagger UI and openapi.json files are accessible on docs ingress.
> 
> Note: I’ll drop the bff-docs.ifa and keep only silver-bff-docs. Originally I was thinking to expose them separately, but as per last discussion, we want single place for all BFF swagger
> 
> ![](<url>
> ![](<url>
> ‌
> 
> Try it out requests are intercepted correctly, and BFF successfully proxies the request to BE advisory
> 
> ![](<url>
> ‌

**Conditions and limits:**

- D56 proxying to advisory passed; planned docs ingress consolidation removes bff-docs.ifa in favor of silver-bff-docs.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:614 · comment 538605350 · PR 9928 · 2024-09-05

**Evidence:** anon-2.jsonl:614 · comment 538605350 · PR 9928 · 2024-09-05

**Explicit source context (pr_title):**

> [INV-3372] feat(bff): Expose swagger on akka management port

## A2-0626 — AkkaHttpAuthRecipesTest: Which executionContext is this? We should probably use the one from AsyncWordSpec right?

**Source stance:** open-question

**Context:**

> PR 9891 (Feat/endpoints4s bff phase2), bff-impl/src/test/scala/com/endowus/silver/bff/impl/auth/AkkaHttpAuthRecipesTest.scala; original row 626.

**Concern stated in the source:** Which executionContext is this? We should probably use the one from AsyncWordSpec right?

**Source-preserving request, proposal, or question:**

> Which executionContext is this? We should probably use the one from AsyncWordSpec right?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:626 · comment 537782683 · PR 9891 · 2024-09-03

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/auth/AkkaHttpAuthRecipesTest.scala`

**Evidence:** anon-2.jsonl:626 · comment 537782683 · PR 9891 · 2024-09-03

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/auth/AkkaHttpAuthRecipesTest.scala`

**Explicit source context (pr_title):**

> Feat/endpoints4s bff phase2

## A2-0627 — GuardsTest: This should be enough

**Source stance:** suggestion

**Context:**

> PR 9891 (Feat/endpoints4s bff phase2), bff-impl/src/test/scala/com/endowus/silver/bff/impl/auth/GuardsTest.scala; original row 627.

**Source-preserving request, proposal, or question:**

> This should be enough
> 
> ```
> private val goalServiceClient = mock[SgGoalServiceClient](RETURNS_DEEP_STUBS)
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:627 · comment 537783122 · PR 9891 · 2024-09-03

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/auth/GuardsTest.scala`

**Evidence:** anon-2.jsonl:627 · comment 537783122 · PR 9891 · 2024-09-03

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/auth/GuardsTest.scala`

**Explicit source context (pr_title):**

> Feat/endpoints4s bff phase2

## A2-0674 — deploy_config: Actually I’m not sure why we need this requires… why does deployment to dev needs to be after deployment to staging? Isn’t it backward?

**Source stance:** open-question

**Context:**

> PR 9847 ([INV-3372] Add missing deploy_argocd steps for dev_deploy and qa_deploy workflows), .circleci/deploy_config.yml; original row 674.

**Source-preserving request, proposal, or question:**

> Actually I’m not sure why we need this requires… why does deployment to dev needs to be after deployment to staging? Isn’t it backward?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:674 · comment 535609237 · PR 9847 · 2024-08-27

Source path: `.circleci/deploy_config.yml`

**Evidence:** anon-2.jsonl:674 · comment 535609237 · PR 9847 · 2024-08-27

Source path: `.circleci/deploy_config.yml`

**Explicit source context (pr_title):**

> [INV-3372] Add missing deploy_argocd steps for dev_deploy and qa_deploy workflows

## A2-0683 — D56 CORS matrix: valid/local origins, rejected origins, and no Origin header

**Source stance:** reported-verification

**Context:**

> PR 9799 ([INV-3372] feat(bff): Add CORS support), no inline path; original row 683.

**Source-preserving request, proposal, or question:**

> D56 CORS verification reported pre-flight OPTIONS and ordinary GET with valid and localhost origins returning 200, invalid origins returning 400 plain-text CORS rejection, and no-Origin GET (e.g. mobile) returning 200 without access-control-* headers. Valid preflight advertised credentials=true, GET/POST/OPTIONS/PUT/DELETE/PATCH, max-age 1800, and the listed allowed headers; GET exposed Content-Disposition.

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> Tested in d56

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> ### Pre-flight requests

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> With valid origin

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> With localhost origin

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> With invalid origin

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> < HTTP/2 200

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> < HTTP/2 400

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> CORS: invalid origin

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> < access-control-allow-credentials: true

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> < access-control-allow-headers: DNT, X-CustomHeader, Keep-Alive, User-Agent, X-Requested-With, If-Modified-Since, Cache-Control, Content-Type, Authorization, endowus-otp-id, endowus-otp-token, Client-Id, Device-Id

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> < access-control-allow-methods: GET, POST, OPTIONS, PUT, DELETE, PATCH

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> < access-control-max-age: 1800

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> < access-control-expose-headers: Content-Disposition

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

> Without origin \(e.g. Mobile\): no access-control-\* headers returned

**Evidence:** anon-2.jsonl:683 · comment 532828814 · PR 9799 · 2024-08-20

**Explicit source context (pr_title):**

> [INV-3372] feat(bff): Add CORS support

## A2-0712 — PortfolioMonthlyChangesHelper: 1. Let’s not persist dummy values \(empty or last value\) on failure

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala; original row 712.

**Concern stated in the source:** 1. Let’s not persist dummy values \(empty or last value\) on failure
2. Maybe we can validate instrument mc → log error at instrument, then can we log warn with it’s instrument mc issue. Otherwise we log error if portfolio mc calculation issue. That would require `generatePortfolioMonthlyChanges` to throw more specific exception

‌

**Source-preserving request, proposal, or question:**

> 1. Let’s not persist dummy values \(empty or last value\) on failure
> 2. Maybe we can validate instrument mc → log error at instrument, then can we log warn with it’s instrument mc issue. Otherwise we log error if portfolio mc calculation issue. That would require `generatePortfolioMonthlyChanges` to throw more specific exception
> 
> ‌

**Conditions and limits:**

- Do not persist empty/last dummy values after failure. Distinguish instrument-MC validation errors (instrument error, portfolio warning) from portfolio-calculation errors, requiring more specific exceptions.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:712 · comment 524619598 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Evidence:** anon-2.jsonl:712 · comment 524619598 · PR 9603 · 2024-07-24

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

## A2-0783 — SgRecommendedInvestmentManager: Best if we can refactor to avoid make unnecessary calls

**Source stance:** suggestion

**Context:**

> PR 9739 (Feat/EN-3683 sg create a new api to get recommended investment amount), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala; original row 783.

**Concern stated in the source:** Best if we can refactor to avoid make unnecessary calls

```
lazy val tierLevelFut = getCustomerIncomeTierLevel(customerId)
lazy val myInfoFinancialDataFut = getMyInfoFinancialData(customerId)

tradingAccountType match {
  case TradingAccountType.SINGAPORE_SGD_CASH_ACCOUNT =>
    tierLevelFut.map { level =>
      deriveRecommendationFromIncomeTier(level, RecommendedRecurringMonthlyAmountSgdCashBasedOnIncomeLevelMap)
    }

  case TradingAccountType.SINGAPORE_CPF_OA_ACCOUNT =>
    for {
      myInfoFinancialData <- myInfoFinancialDataFut
      response <- deriveRecommendationFromMyInfo(myInfoFinancialData) match {
        case Some(recommendation) =>
          Future.successful(recommendation)
        case None =>
          tierLevelFut.map { level =>
            deriveRecommendationFromIncomeTier(level, RecommendedRecurringMonthlyAmountCpfBasedOnIncomeLevelMap)
          }
      }
    } yield response

  case _ =>
    Future.successful(RecommendedInvestmentDto.noRecommendation())
}
```

‌

No need to split the helper methods too fine, especially when they are not used in more than one place

* `getCustomerIncomeTierLevel` can do both customer lookup and perform mapping to TierLevel
* `getMyInfoFinancialData` can do myinfo lookup, if found then return, else only then do onboarding lookup and perform mapping

‌

**Source-preserving request, proposal, or question:**

> Best if we can refactor to avoid make unnecessary calls
> 
> ```
> lazy val tierLevelFut = getCustomerIncomeTierLevel(customerId)
> lazy val myInfoFinancialDataFut = getMyInfoFinancialData(customerId)
> 
> tradingAccountType match {
>   case TradingAccountType.SINGAPORE_SGD_CASH_ACCOUNT =>
>     tierLevelFut.map { level =>
>       deriveRecommendationFromIncomeTier(level, RecommendedRecurringMonthlyAmountSgdCashBasedOnIncomeLevelMap)
>     }
> 
>   case TradingAccountType.SINGAPORE_CPF_OA_ACCOUNT =>
>     for {
>       myInfoFinancialData <- myInfoFinancialDataFut
>       response <- deriveRecommendationFromMyInfo(myInfoFinancialData) match {
>         case Some(recommendation) =>
>           Future.successful(recommendation)
>         case None =>
>           tierLevelFut.map { level =>
>             deriveRecommendationFromIncomeTier(level, RecommendedRecurringMonthlyAmountCpfBasedOnIncomeLevelMap)
>           }
>       }
>     } yield response
> 
>   case _ =>
>     Future.successful(RecommendedInvestmentDto.noRecommendation())
> }
> ```
> 
> ‌
> 
> No need to split the helper methods too fine, especially when they are not used in more than one place
> 
> * `getCustomerIncomeTierLevel` can do both customer lookup and perform mapping to TierLevel
> * `getMyInfoFinancialData` can do myinfo lookup, if found then return, else only then do onboarding lookup and perform mapping
> 
> ‌

**Conditions and limits:**

- SGD uses only income-tier lookup; CPF tries MyInfo first, falling back to income tier only if needed; unsupported account returns noRecommendation. Customer/onboarding lookup should also be lazy.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:783 · comment 530404623 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Evidence:** anon-2.jsonl:783 · comment 530404623 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Explicit source context (pr_title):**

> Feat/EN-3683 sg create a new api to get recommended investment amount

## A2-0785 — SgRecommendedInvestmentManagerTest: These brackets are extra here, causing all the below tests to be outside of `"getRecommendedInvestmentAmount" should {`

**Source stance:** observed-defect

**Context:**

> PR 9739 (Feat/EN-3683 sg create a new api to get recommended investment amount), advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManagerTest.scala; original row 785.

**Concern stated in the source:** These brackets are extra here, causing all the below tests to be outside of `"getRecommendedInvestmentAmount" should {`

**Source-preserving request, proposal, or question:**

> These brackets are extra here, causing all the below tests to be outside of `"getRecommendedInvestmentAmount" should {`

**Conditions and limits:**

- Extra braces put subsequent tests outside the intended getRecommendedInvestmentAmount should block.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:785 · comment 530406192 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManagerTest.scala`

**Evidence:** anon-2.jsonl:785 · comment 530406192 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManagerTest.scala`

**Explicit source context (pr_title):**

> Feat/EN-3683 sg create a new api to get recommended investment amount

## A2-0818 — ServiceClientExceptionSerializerTest: Let’s add a positive test too?

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala; original row 818.

**Source-preserving request, proposal, or question:**

> Let’s add a positive test too?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:818 · comment 525233980 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala`

**Evidence:** anon-2.jsonl:818 · comment 525233980 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0819 — application: This should be moved to `test/resources`

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), akka-client-commons/src/main/resources/application.conf; original row 819.

**Source-preserving request, proposal, or question:**

> This should be moved to `test/resources`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:819 · comment 525231252 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/main/resources/application.conf`

**Evidence:** anon-2.jsonl:819 · comment 525231252 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/main/resources/application.conf`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0820 — ServiceClientExceptionSerializerTest: Shouldn’t it be `implicit val system: ActorSystem`

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala; original row 820.

**Concern stated in the source:** Shouldn’t it be `implicit val system: ActorSystem`

‌

**Source-preserving request, proposal, or question:**

> Shouldn’t it be `implicit val system: ActorSystem`
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:820 · comment 525234003 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala`

**Evidence:** anon-2.jsonl:820 · comment 525234003 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0836 — CustomerStatusHelper: Can we make this change for HK too

**Source stance:** suggestion

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/CustomerStatusHelper.scala; original row 836.

**Concern stated in the source:** Can we make this change for HK too

I think no need to name them separately like current code

```
trait CustomerStatusHelper {
  def checkCustomerAiPiStatus(customerId: UUID): Future[Boolean]
}

trait SgCustomerStatusHelper extends CustomerStatusHelper with RegionSpecific[SilverRegion.Sg.type] {
  ...
}

trait HkCustomerStatusHelper extends CustomerStatusHelper with RegionSpecific[SilverRegion.Hk.type] {
  ...
}
```

‌

**Source-preserving request, proposal, or question:**

> Can we make this change for HK too
> 
> I think no need to name them separately like current code
> 
> ```
> trait CustomerStatusHelper {
>   def checkCustomerAiPiStatus(customerId: UUID): Future[Boolean]
> }
> 
> trait SgCustomerStatusHelper extends CustomerStatusHelper with RegionSpecific[SilverRegion.Sg.type] {
>   ...
> }
> 
> trait HkCustomerStatusHelper extends CustomerStatusHelper with RegionSpecific[SilverRegion.Hk.type] {
>   ...
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:836 · comment 524566116 · PR 9605 · 2024-07-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/CustomerStatusHelper.scala`

**Evidence:** anon-2.jsonl:836 · comment 524566116 · PR 9605 · 2024-07-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/CustomerStatusHelper.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

## A2-0851 — Terms: Since all non-alts product use same terms for this, let’s just name this group `InvestmentAlignmentTerms` I think, i.e. we don’t have product specific terms like FlagshipDpm

**Source stance:** explanation

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/termsagreement/sg/Terms.scala; original row 851.

**Concern stated in the source:** Since all non-alts product use same terms for this, let’s just name this group `InvestmentAlignmentTerms` I think, i.e. we don’t have product specific terms like FlagshipDpm

**Source-preserving request, proposal, or question:**

> Since all non-alts product use same terms for this, let’s just name this group `InvestmentAlignmentTerms` I think, i.e. we don’t have product specific terms like FlagshipDpm

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:851 · comment 524906063 · PR 9605 · 2024-07-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/termsagreement/sg/Terms.scala`

**Evidence:** anon-2.jsonl:851 · comment 524906063 · PR 9605 · 2024-07-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/termsagreement/sg/Terms.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

## A2-0857 — build: Let’s add `% Test`?

**Source stance:** open-question

**Context:**

> PR 8424 ([NE-237] (all) Upgrade akka version to 2.6.21), build.sbt; original row 857.

**Source-preserving request, proposal, or question:**

> Let’s add `% Test`?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:857 · comment 525230690 · PR 8424 · 2024-07-26

Source path: `build.sbt`

**Evidence:** anon-2.jsonl:857 · comment 525230690 · PR 8424 · 2024-07-26

Source path: `build.sbt`

**Explicit source context (pr_title):**

> [NE-237] (all) Upgrade akka version to 2.6.21

## A2-0865 — PerformanceCalculatorTest: Let’s also assert on the peak and trough’s yearmonth at least

**Source stance:** suggestion

**Context:**

> PR 9543 (Resolve INV-3136: Calculate max draw down for a given set of monthlyChanges.), performance-impl/src/test/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculatorTest.scala; original row 865.

**Concern stated in the source:** Let’s also assert on the peak and trough’s yearmonth at least

**Source-preserving request, proposal, or question:**

> Let’s also assert on the peak and trough’s yearmonth at least

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:865 · comment 520111138 · PR 9543 · 2024-07-11

Source path: `performance-impl/src/test/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculatorTest.scala`

**Evidence:** anon-2.jsonl:865 · comment 520111138 · PR 9543 · 2024-07-11

Source path: `performance-impl/src/test/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculatorTest.scala`

**Explicit source context (pr_title):**

> Resolve INV-3136: Calculate max draw down for a given set of monthlyChanges.

## A2-0866 — PerformanceCalculatorTest: `performanceMetrics1` already covers the case when peak->trough is the first drop, let’s make this case returning 2nd drop

**Source stance:** suggestion

**Context:**

> PR 9543 (Resolve INV-3136: Calculate max draw down for a given set of monthlyChanges.), performance-impl/src/test/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculatorTest.scala; original row 866.

**Concern stated in the source:** `performanceMetrics1` already covers the case when peak->trough is the first drop, let’s make this case returning 2nd drop

**Source-preserving request, proposal, or question:**

> `performanceMetrics1` already covers the case when peak->trough is the first drop, let’s make this case returning 2nd drop

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:866 · comment 520115222 · PR 9543 · 2024-07-11

Source path: `performance-impl/src/test/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculatorTest.scala`

**Evidence:** anon-2.jsonl:866 · comment 520115222 · PR 9543 · 2024-07-11

Source path: `performance-impl/src/test/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculatorTest.scala`

**Explicit source context (pr_title):**

> Resolve INV-3136: Calculate max draw down for a given set of monthlyChanges.

## A2-0877 — PerformanceCalculator: Prev condition is `count < 2`, so this should just be `case Nil | _ :: Nil`. Actually we should add a test case with just 2 mc as well

**Source stance:** explanation

**Context:**

> PR 9623 ([INV-3136] (performance) refactor calculation of max draw down), performance-impl/src/main/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculator.scala; original row 877.

**Concern stated in the source:** Prev condition is `count < 2`, so this should just be `case Nil | _ :: Nil`. Actually we should add a test case with just 2 mc as well

**Source-preserving request, proposal, or question:**

> Prev condition is `count < 2`, so this should just be `case Nil | _ :: Nil`. Actually we should add a test case with just 2 mc as well

**Conditions and limits:**

- Nil and singleton correspond to prior count<2, while exactly two monthly changes must be tested.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:877 · comment 524068893 · PR 9623 · 2024-07-22

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculator.scala`

**Evidence:** anon-2.jsonl:877 · comment 524068893 · PR 9623 · 2024-07-22

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculator.scala`

**Explicit source context (pr_title):**

> [INV-3136] (performance) refactor calculation of max draw down

## A2-0878 — PerformanceCalculator: No no I mean there’s no tests for exactly 2 mc - which would have failed. There is only tests for 1 mc and >=3 mc as of now

**Source stance:** explanation

**Context:**

> PR 9623 ([INV-3136] (performance) refactor calculation of max draw down), performance-impl/src/main/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculator.scala; original row 878.

**Concern stated in the source:** No no I mean there’s no tests for exactly 2 mc - which would have failed. There is only tests for 1 mc and >=3 mc as of now

**Source-preserving request, proposal, or question:**

> No no I mean there’s no tests for exactly 2 mc - which would have failed. There is only tests for 1 mc and >=3 mc as of now

**Conditions and limits:**

- Source reports tests existed for one and >=3 MC only; exactly two would fail.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:878 · comment 524073469 · PR 9623 · 2024-07-22

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculator.scala`

**Evidence:** anon-2.jsonl:878 · comment 524073469 · PR 9623 · 2024-07-22

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/utils/PerformanceCalculator.scala`

**Explicit source context (pr_title):**

> [INV-3136] (performance) refactor calculation of max draw down

## A2-0889 — HkServiceLogicImpl: Looking at `StatementDataGenerator.createStatementDataAndGeneratePdf`, looks like it’s better to use `statementPeriod = END_OF_MONTH` and `monthPeriod = Some...

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/HkServiceLogicImpl.scala; original row 889.

**Concern stated in the source:** Looking at `StatementDataGenerator.createStatementDataAndGeneratePdf`, looks like it’s better to use `statementPeriod = END_OF_MONTH` and `monthPeriod = Some(6)`, and only specify `startDateOfStatement`

‌

**Source-preserving request, proposal, or question:**

> Looking at `StatementDataGenerator.createStatementDataAndGeneratePdf`, looks like it’s better to use `statementPeriod = END_OF_MONTH` and `monthPeriod = Some(6)`, and only specify `startDateOfStatement`
> 
> ‌

**Conditions and limits:**

- Use statementPeriod=END_OF_MONTH, monthPeriod=Some(6), and specify only startDateOfStatement.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:889 · comment 507802852 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:889 · comment 507802852 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/HkServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0908 — Review: Can you help to test a few cases, just in case…

**Source stance:** explanation

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), no inline path; original row 908.

**Concern stated in the source:** Can you help to test a few cases, just in case…

* DPM goals but no settled DPM transactions at all \(those goals would be empty\): should not print
* DPM goals and settled DPM transactions in the printing period: should print
* DPM goals and settled DPM transactions before the printing period: should print
* all deactivated DPM goals and settled DPM transactions before the printing period: looks like we are printing?

‌

**Source-preserving request, proposal, or question:**

> Can you help to test a few cases, just in case…
> 
> * DPM goals but no settled DPM transactions at all \(those goals would be empty\): should not print
> * DPM goals and settled DPM transactions in the printing period: should print
> * DPM goals and settled DPM transactions before the printing period: should print
> * all deactivated DPM goals and settled DPM transactions before the printing period: looks like we are printing?
> 
> ‌

**Conditions and limits:**

- The first three print expectations are specified; all-deactivated DPM goals with earlier settled transactions remains phrased as "looks like we are printing?".
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:908 · comment 512167484 · PR 9240 · 2024-06-20

**Evidence:** anon-2.jsonl:908 · comment 512167484 · PR 9240 · 2024-06-20

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0953 — package: This should be a List, so that IO/Product can control the ordering. And we will need another field to specify which benchmark to highlight

**Source stance:** suggestion

**Context:**

> PR 9487 ([INV-3233] feat(advisory): Support portfolio-offerings for Core-Enhanced), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/models/advisoryinfo/package.scala; original row 953.

**Concern stated in the source:** This should be a List, so that IO/Product can control the ordering. And we will need another field to specify which benchmark to highlight

**Source-preserving request, proposal, or question:**

> This should be a List, so that IO/Product can control the ordering. And we will need another field to specify which benchmark to highlight

**Conditions and limits:**

- List plus separate highlighted benchmark id is one ordering design; row 957 offers Set plus response sorting as an alternative.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:953 · comment 518017857 · PR 9487 · 2024-07-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/models/advisoryinfo/package.scala`

**Evidence:** anon-2.jsonl:953 · comment 518017857 · PR 9487 · 2024-07-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/models/advisoryinfo/package.scala`

**Explicit source context (pr_title):**

> [INV-3233] feat(advisory): Support portfolio-offerings for Core-Enhanced

## A2-1024 — CorporateProductRuleInterpreterTest: Let’s add more tests to verify multiple `SpecificInstrumentAccessRule` can compose correctly

**Source stance:** suggestion

**Context:**

> PR 9403 ([INV-3211] feat(advisory): Add new specific instrument access rule for ringfencing), advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/logic/corporate/CorporateProductRuleInterpreterTest.scala; original row 1024.

**Concern stated in the source:** Let’s add more tests to verify multiple `SpecificInstrumentAccessRule` can compose correctly

**Source-preserving request, proposal, or question:**

> Let’s add more tests to verify multiple `SpecificInstrumentAccessRule` can compose correctly

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1024 · comment 512934465 · PR 9403 · 2024-06-24

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/logic/corporate/CorporateProductRuleInterpreterTest.scala`

**Evidence:** anon-2.jsonl:1024 · comment 512934465 · PR 9403 · 2024-06-24

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/logic/corporate/CorporateProductRuleInterpreterTest.scala`

**Explicit source context (pr_title):**

> [INV-3211] feat(advisory): Add new specific instrument access rule for ringfencing

## A2-1025 — CorporateProfile: Let’s add tests for this `CorporateProfile.validate` method.

**Source stance:** open-question

**Context:**

> PR 9403 ([INV-3211] feat(advisory): Add new specific instrument access rule for ringfencing), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/corporate/ces/CorporateProfile.scala; original row 1025.

**Concern stated in the source:** Let’s add tests for this `CorporateProfile.validate` method.

The below `case _ => false` will block rules containing only `UnRestricted` or `Restricted` won’t it?

**Source-preserving request, proposal, or question:**

> Let’s add tests for this `CorporateProfile.validate` method.
> 
> The below `case _ => false` will block rules containing only `UnRestricted` or `Restricted` won’t it?

**Conditions and limits:**

- CorporateProfile.validate wildcard false may wrongly reject UnRestricted-only or Restricted-only rules; tests are requested rather than asserted results.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1025 · comment 512932296 · PR 9403 · 2024-06-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/corporate/ces/CorporateProfile.scala`

**Evidence:** anon-2.jsonl:1025 · comment 512932296 · PR 9403 · 2024-06-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/corporate/ces/CorporateProfile.scala`

**Explicit source context (pr_title):**

> [INV-3211] feat(advisory): Add new specific instrument access rule for ringfencing

## A2-1044 — PlanCommunicationV2EventProcessor: [person] [person] Unlike emails, if customer changes preferred language, the existing platform notifications would have to switch display acco...

**Source stance:** suggestion

**Context:**

> PR 9206 (TT-4229 - recurring autofund investment schedule created comms), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; original row 1044.

**Concern stated in the source:** [person] [person] Unlike emails, if customer changes preferred language, the existing platform notifications would have to switch display accordingly. Hence this `localeSpecificInterpolation` needs to be populated for all values of `Locale.getSupportedLocales(localConfig.getSilverRegion)`.

**Source-preserving request, proposal, or question:**

> [person] [person] Unlike emails, if customer changes preferred language, the existing platform notifications would have to switch display accordingly. Hence this `localeSpecificInterpolation` needs to be populated for all values of `Locale.getSupportedLocales(localConfig.getSilverRegion)`.

**Conditions and limits:**

- Existing platform notifications must re-render after preferred-language changes; populate localeSpecificInterpolation for every supported locale, unlike email.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1044 · comment 509679815 · PR 9206 · 2024-06-11

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

> Unlike emails, if customer changes preferred language, the existing platform notifications would have to switch display accordingly. Hence this `localeSpecificInterpolation` needs to be populated for all values of `Locale.getSupportedLocales(localConfig.getSilverRegion)`.

**Evidence:** anon-2.jsonl:1044 · comment 509679815 · PR 9206 · 2024-06-11

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (pr_title):**

> TT-4229 - recurring autofund investment schedule created comms

## A2-1045 — PlanCommunicationV2EventProcessor: In anticipation for more custom interpolations in future, we can change this a little to below \(similar to locale specific one\)

**Source stance:** suggestion

**Context:**

> PR 9206 (TT-4229 - recurring autofund investment schedule created comms), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; original row 1045.

**Concern stated in the source:** In anticipation for more custom interpolations in future, we can change this a little to below \(similar to locale specific one\)

```
val commonInterpolations = Seq(...)
val autoFundInterpolations = recurringFundingInstructionDetails.autoFundDetails match {
  case Some(autoFundDetails) => Seq(...)
  case None => Seq.empty
}
<more custom interpolations go here>
commonInterpolations ++ autoFundInterpolations
```

‌

**Source-preserving request, proposal, or question:**

> In anticipation for more custom interpolations in future, we can change this a little to below \(similar to locale specific one\)
> 
> ```
> val commonInterpolations = Seq(...)
> val autoFundInterpolations = recurringFundingInstructionDetails.autoFundDetails match {
>   case Some(autoFundDetails) => Seq(...)
>   case None => Seq.empty
> }
> <more custom interpolations go here>
> commonInterpolations ++ autoFundInterpolations
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1045 · comment 510029419 · PR 9206 · 2024-06-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:1045 · comment 510029419 · PR 9206 · 2024-06-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (pr_title):**

> TT-4229 - recurring autofund investment schedule created comms

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

## A2-1061 — GoalBasedStatementInfoDbDto: Yea so I think adding these new fields to `*DbDto` can cause confusion for existing data if we don’t retrospectively update them.

**Source stance:** explanation

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala; original row 1061.

**Concern stated in the source:** Yea so I think adding these new fields to `*DbDto` can cause confusion for existing data if we don’t retrospectively update them.

Based on my understanding, it seems these new fields are not needed anyway. The new design will anyway cause it to be reprinted cuz we have the new page split for AllInvestmentGoals pages \+ the ordering for other goal pages. Other than that, once new design is printed, these isDpm flags are no longer useful, cuz goal cannot change its dpm flag.

**Source-preserving request, proposal, or question:**

> Yea so I think adding these new fields to `*DbDto` can cause confusion for existing data if we don’t retrospectively update them.
> 
> Based on my understanding, it seems these new fields are not needed anyway. The new design will anyway cause it to be reprinted cuz we have the new page split for AllInvestmentGoals pages \+ the ordering for other goal pages. Other than that, once new design is printed, these isDpm flags are no longer useful, cuz goal cannot change its dpm flag.

**Conditions and limits:**

- New format already forces reprinting through page splitting/order changes; mutable persisted isDpm fields are considered unnecessary and confusing without retrospective data updates.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1061 · comment 502499163 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Evidence:** anon-2.jsonl:1061 · comment 502499163 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1062 — StatementPdfGeneratorTest: I suppose this assertion at best can only verify the html templates don’t throw error, and that some pdf file is generated.

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/test/scala/com/endowus/silver/report/impl/pdfGenerator/statementPdfGenerator/StatementPdfGeneratorTest.scala; original row 1062.

**Concern stated in the source:** I suppose this assertion at best can only verify the html templates don’t throw error, and that some pdf file is generated.

IDK how we can effectively assert the result of the template \(since it has logic\). But at least, let’s validate the result of `PageDataGenerator`, e.g. for CoverPage, let’s also also check number of pageData returned, for each of them, validate the dynamic fields `goalNames` / `startOfNonDPMGoalIndex` / `showDisclaimer` as well as the corresponding templateName.

Then we do the same for AllInvestmentGoals page. For the rest, I’m ok with not touching as we know we don’t change them much other than just additional isDpm flag

**Source-preserving request, proposal, or question:**

> I suppose this assertion at best can only verify the html templates don’t throw error, and that some pdf file is generated.
> 
> IDK how we can effectively assert the result of the template \(since it has logic\). But at least, let’s validate the result of `PageDataGenerator`, e.g. for CoverPage, let’s also also check number of pageData returned, for each of them, validate the dynamic fields `goalNames` / `startOfNonDPMGoalIndex` / `showDisclaimer` as well as the corresponding templateName.
> 
> Then we do the same for AllInvestmentGoals page. For the rest, I’m ok with not touching as we know we don’t change them much other than just additional isDpm flag

**Conditions and limits:**

- Successful HTML/PDF rendering only verifies no template throw; PageDataGenerator tests must assert page count, goalNames/startOfNonDPMGoalIndex/showDisclaimer and template names.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1062 · comment 503069656 · PR 9052 · 2024-05-22

Source path: `report-impl/src/test/scala/com/endowus/silver/report/impl/pdfGenerator/statementPdfGenerator/StatementPdfGeneratorTest.scala`

**Evidence:** anon-2.jsonl:1062 · comment 503069656 · PR 9052 · 2024-05-22

Source path: `report-impl/src/test/scala/com/endowus/silver/report/impl/pdfGenerator/statementPdfGenerator/StatementPdfGeneratorTest.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1064 — package: [person] after checking the usage of this class again, I’m convinced that

**Source stance:** explanation

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala; original row 1064.

**Concern stated in the source:** [person] after checking the usage of this class again, I’m convinced that

* it’s not used for public DTO - let’s move to report-impl instead, otherwise it can be confusing to see `*RawData` case class in report-api. I think these can just stay in `GoalBasedStatementDataGenerator`
* it’s not used at all for serdes, not even in test - so we don’t need the format at all

‌

I checked the lookup usage of this `goalsInfoForDisplay`. Not too bad so I guess we can leave it as a List still. But let’s move both `GoalBasedStatementRawData` and `GoalInfoToDisplay` to impl so that it’s less confusing on usage scope

**Source-preserving request, proposal, or question:**

> [person] after checking the usage of this class again, I’m convinced that
> 
> * it’s not used for public DTO - let’s move to report-impl instead, otherwise it can be confusing to see `*RawData` case class in report-api. I think these can just stay in `GoalBasedStatementDataGenerator`
> * it’s not used at all for serdes, not even in test - so we don’t need the format at all
> 
> ‌
> 
> I checked the lookup usage of this `goalsInfoForDisplay`. Not too bad so I guess we can leave it as a List still. But let’s move both `GoalBasedStatementRawData` and `GoalInfoToDisplay` to impl so that it’s less confusing on usage scope

**Conditions and limits:**

- After inspection, raw-data classes are neither public DTOs nor serialized; move GoalBasedStatementRawData/GoalInfoToDisplay into report-impl and remove format. List lookup is accepted, revising row 1056.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1064 · comment 503067120 · PR 9052 · 2024-05-22

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala`

> after checking the usage of this class again, I’m convinced that
> 
> * it’s not used for public DTO - let’s move to report-impl instead, otherwise it can be confusing to see `*RawData` case class in report-api. I think these can just stay in `GoalBasedStatementDataGenerator`
> * it’s not used at all for serdes, not even in test - so we don’t need the format at all
> 
> ‌
> 
> I checked the lookup usage of this `goalsInfoForDisplay`. Not too bad so I guess we can leave it as a List still. But let’s move both `GoalBasedStatementRawData` and `GoalInfoToDisplay` to impl so that it’s less confusing on usage scope

**Evidence:** anon-2.jsonl:1064 · comment 503067120 · PR 9052 · 2024-05-22

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1069 — Review: Without the mock timeout header, Route tests' log would be flooded with these WARN entries from `TimeoutDirectives`

**Source stance:** explanation

**Context:**

> PR 9331 ([INV-3148] feat(testkit): Add common RouteTestUtils with mock timeout header to avoid noise WARN logs), no inline path; original row 1069.

**Concern stated in the source:** Without the mock timeout header, Route tests' log would be flooded with these WARN entries from `TimeoutDirectives`

```
withRequestTimeout was used in route however no request-timeout is set!
```

‌

**Source-preserving request, proposal, or question:**

> Without the mock timeout header, Route tests' log would be flooded with these WARN entries from `TimeoutDirectives`
> 
> ```
> withRequestTimeout was used in route however no request-timeout is set!
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1069 · comment 509052252 · PR 9331 · 2024-06-07

**Evidence:** anon-2.jsonl:1069 · comment 509052252 · PR 9331 · 2024-06-07

**Explicit source context (pr_title):**

> [INV-3148] feat(testkit): Add common RouteTestUtils with mock timeout header to avoid noise WARN logs

## A2-1072 — InvestmentCommunicationV2EventProcessor: Hmm this assumes the “problems” are specific to plan account is it? I guess we can revisit these templates again….

**Source stance:** open-question

**Context:**

> PR 9267 (TT-4231 autofund upcoming recur inv has problem comm), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala; original row 1072.

**Concern stated in the source:** Hmm this assumes the “problems” are specific to plan account is it? I guess we can revisit these templates again….

**Source-preserving request, proposal, or question:**

> Hmm this assumes the “problems” are specific to plan account is it? I guess we can revisit these templates again….

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1072 · comment 508960241 · PR 9267 · 2024-06-07

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:1072 · comment 508960241 · PR 9267 · 2024-06-07

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (pr_title):**

> TT-4231 autofund upcoming recur inv has problem comm

## A2-1080 — DpmStatusLogic: [person] [person] this kind of validation in logic \+ blind update in entity is actually not safe against race condition / concurrent modification. Specialized c...

**Source stance:** explanation

**Context:**

> PR 9314 ([INV-3127] feat(compliance): Add edge endpoint to query DPM status with cross validation against DPM eligibility in case of EC), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/DpmStatusLogic.scala; original row 1080.

**Concern stated in the source:** [person] [person] this kind of validation in logic \+ blind update in entity is actually not safe against race condition / concurrent modification. Specialized cmd\+events or proper versioning \(optimistic locking\) can help solve this, but I’ll leave that out as another improvement

**Source-preserving request, proposal, or question:**

> [person] [person] this kind of validation in logic \+ blind update in entity is actually not safe against race condition / concurrent modification. Specialized cmd\+events or proper versioning \(optimistic locking\) can help solve this, but I’ll leave that out as another improvement

**Conditions and limits:**

- Logic-layer validation plus blind entity update is unsafe for concurrent modification; specialized commands/events or optimistic locking are proposed as later improvement.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1080 · comment 508719218 · PR 9314 · 2024-06-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/DpmStatusLogic.scala`

> this kind of validation in logic \+ blind update in entity is actually not safe against race condition / concurrent modification. Specialized cmd\+events or proper versioning \(optimistic locking\) can help solve this, but I’ll leave that out as another improvement

**Evidence:** anon-2.jsonl:1080 · comment 508719218 · PR 9314 · 2024-06-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/DpmStatusLogic.scala`

**Explicit source context (pr_title):**

> [INV-3127] feat(compliance): Add edge endpoint to query DPM status with cross validation against DPM eligibility in case of EC

## A2-1092 — HkGoalCreateValidationBehaviour: Can we add test to capture this case please

**Source stance:** suggestion

**Context:**

> PR 9212 (Fix/INV-3070/flagship dpm minor integration fixes), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/hk/HkGoalCreateValidationBehaviour.scala; original row 1092.

**Source-preserving request, proposal, or question:**

> Can we add test to capture this case please

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1092 · comment 505681017 · PR 9212 · 2024-05-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/hk/HkGoalCreateValidationBehaviour.scala`

**Evidence:** anon-2.jsonl:1092 · comment 505681017 · PR 9212 · 2024-05-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/hk/HkGoalCreateValidationBehaviour.scala`

**Explicit source context (pr_title):**

> Fix/INV-3070/flagship dpm minor integration fixes

## A2-1100 — Review: Did we test recurring investment flow in staging this time?

**Source stance:** open-question

**Context:**

> PR 9103 ([EN-3368] Use v7 investment plan table), no inline path; original row 1100.

**Source-preserving request, proposal, or question:**

> Did we test recurring investment flow in staging this time?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1100 · comment 500231756 · PR 9103 · 2024-05-13

**Evidence:** anon-2.jsonl:1100 · comment 500231756 · PR 9103 · 2024-05-13

**Explicit source context (pr_title):**

> [EN-3368] Use v7 investment plan table

## A2-1126 — DetectUpcomingRecurringInvestmentCmdHandler: Does this amount needs to be “correct” amount here? Maybe just make it as deprecated, and only use if old events

**Source stance:** suggestion

**Context:**

> PR 9102 ([EN-3248] Autofx upcoming recurring comms), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala; original row 1126.

**Concern stated in the source:** Does this amount needs to be “correct” amount here? Maybe just make it as deprecated, and only use if old events

```
case class UpcomingRecurringTransactionDetectedEvt(
  ...
  @deprecated scheduledInvestmentAmount: BigDecimal,
  fundingInstructions: Option[PlanFundingInstructions]
) {

  def resolvedScheduledInvestmentAmount: BigDecimal = {
    fundingInstructions match {
      case Some(specifiedAccount) => ...
      case Some(planAccount) => ...
      case None => scheduledInvestmentAmount
    }
  }

}
```

‌

**Source-preserving request, proposal, or question:**

> Does this amount needs to be “correct” amount here? Maybe just make it as deprecated, and only use if old events
> 
> ```
> case class UpcomingRecurringTransactionDetectedEvt(
>   ...
>   @deprecated scheduledInvestmentAmount: BigDecimal,
>   fundingInstructions: Option[PlanFundingInstructions]
> ) {
> 
>   def resolvedScheduledInvestmentAmount: BigDecimal = {
>     fundingInstructions match {
>       case Some(specifiedAccount) => ...
>       case Some(planAccount) => ...
>       case None => scheduledInvestmentAmount
>     }
>   }
> 
> }
> ```
> 
> ‌

**Conditions and limits:**

- FundingInstructions is optional for old events; deprecated scheduledInvestmentAmount is fallback only when absent. New variants should derive currency-correct amount.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1126 · comment 500278057 · PR 9102 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala`

**Evidence:** anon-2.jsonl:1126 · comment 500278057 · PR 9102 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-3248] Autofx upcoming recurring comms

## A2-1136 — CassandraProjectionManager: Due to this issue, currently all of these spans completes almost instantly \(~0.005s as per current metrics in both prod and staging env\)

**Source stance:** explanation

**Context:**

> PR 9219 ([INV-3090] feat(common): Manually finish the CassandraProjection spans), akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/CassandraProjectionManager.scala; original row 1136.

**Concern stated in the source:** Due to this issue, currently all of these spans completes almost instantly \(~0.005s as per current metrics in both prod and staging env\)

**Source-preserving request, proposal, or question:**

> Due to this issue, currently all of these spans completes almost instantly \(~0.005s as per current metrics in both prod and staging env\)

**Conditions and limits:**

- Observed prematurely completed CassandraProjection spans were about 0.005s in both prod and staging.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1136 · comment 504016232 · PR 9219 · 2024-05-27

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/CassandraProjectionManager.scala`

**Evidence:** anon-2.jsonl:1136 · comment 504016232 · PR 9219 · 2024-05-27

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/CassandraProjectionManager.scala`

**Explicit source context (pr_title):**

> [INV-3090] feat(common): Manually finish the CassandraProjection spans

## A2-1171 — Review: Tested in SG staging with `charge` svc

**Source stance:** reported-verification

**Context:**

> PR 9178 ([INV-3074] Manual start/stop for TaskTopicSubscriber), no inline path; original row 1171.

**Concern stated in the source:** Tested in SG staging with `charge` svc

* auto init subscription on startup
* auto terminate subscription on shutdown
* NOOP \+ error log only if trigger start/stop with wrong task
* propagate start/stop to all instances of the service if trigger start/stop with correct task
* idempotency: 2nd consecutive start or stop are NOOP with expected logs
* verify kafka subscription correctly pauses in the midst of processing if stopped, and correctly resumes from last committed offset if started again

‌

**Source-preserving request, proposal, or question:**

> Tested in SG staging with `charge` svc
> 
> * auto init subscription on startup
> * auto terminate subscription on shutdown
> * NOOP \+ error log only if trigger start/stop with wrong task
> * propagate start/stop to all instances of the service if trigger start/stop with correct task
> * idempotency: 2nd consecutive start or stop are NOOP with expected logs
> * verify kafka subscription correctly pauses in the midst of processing if stopped, and correctly resumes from last committed offset if started again
> 
> ‌

**Conditions and limits:**

- Reported SG-staging charge test includes auto init/terminate, wrong-task NOOP+error log, all-instance propagation, repeated start/stop idempotency, and stop/resume from last committed Kafka offset.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1171 · comment 502171718 · PR 9178 · 2024-05-20

**Evidence:** anon-2.jsonl:1171 · comment 502171718 · PR 9178 · 2024-05-20

**Explicit source context (pr_title):**

> [INV-3074] Manual start/stop for TaskTopicSubscriber

## A2-1189 — BaseInvestmentCommunicationEventProcessor: This doesn’t look like it’s specific about direct debit isn’t it?

**Source stance:** open-question

**Context:**

> PR 9172 (TT-4232 autofund investment cancellation comms), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/BaseInvestmentCommunicationEventProcessor.scala; original row 1189.

**Source-preserving request, proposal, or question:**

> This doesn’t look like it’s specific about direct debit isn’t it?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- The cancellation text may apply beyond direct debit; exact intended template scope remains open.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1189 · comment 502192221 · PR 9172 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/BaseInvestmentCommunicationEventProcessor.scala`

**Evidence:** anon-2.jsonl:1189 · comment 502192221 · PR 9172 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/BaseInvestmentCommunicationEventProcessor.scala`

**Explicit source context (hunk):**

> +            )
> +          }
> +          else if (cancelledReason.isRetryDateExceedCutoffDate) {
> +            (
> +              "platformNotificationTitleAutoFundInvestmentCancelledPassedCutOffDate",
> +              "platformNotificationBodyAutoFundInvestmentCancelledPassedCutOffDate",
> +              None,

**Evidence:** anon-2.jsonl:1189 · comment 502192221 · PR 9172 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/BaseInvestmentCommunicationEventProcessor.scala`

**Explicit source context (pr_title):**

> TT-4232 autofund investment cancellation comms

## A2-1202 — HttpServerStartup: Oh we definitely want to set `rejectionHandler` for all services, especially when we extract this to common code. And in order to use a custom rejection handl...

**Source stance:** suggestion

**Context:**

> PR 9049 (DYNAMIC-1046: Terminate service if onMemberUp fails (ready for review)), akka-http-commons/src/main/scala/com/endowus/silver/server/akka/http/HttpServerStartup.scala; original row 1202.

**Concern stated in the source:** Oh we definitely want to set `rejectionHandler` for all services, especially when we extract this to common code. And in order to use a custom rejection handler, we need to use `Route.seal` with implicit `rejectionHandler`

Last time I checked, that was the only way to provide. And this is useful to catch errors before the ServiceLogic is hit, and allow us to handle and return them in usual error json format that other services \+ FE knows how to deserialize.

I took a shortcut and only added for the services we need back then \(some issue in FE sending incorrect payload, and we reject with validation errors not in json, and Davinci doesn’t log full error msg\)

**Source-preserving request, proposal, or question:**

> Oh we definitely want to set `rejectionHandler` for all services, especially when we extract this to common code. And in order to use a custom rejection handler, we need to use `Route.seal` with implicit `rejectionHandler`
> 
> Last time I checked, that was the only way to provide. And this is useful to catch errors before the ServiceLogic is hit, and allow us to handle and return them in usual error json format that other services \+ FE knows how to deserialize.
> 
> I took a shortcut and only added for the services we need back then \(some issue in FE sending incorrect payload, and we reject with validation errors not in json, and Davinci doesn’t log full error msg\)

**Conditions and limits:**

- Route.seal with implicit rejectionHandler is needed to return standard JSON for validation errors rejected before service logic.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1202 · comment 497987974 · PR 9049 · 2024-05-03

Source path: `akka-http-commons/src/main/scala/com/endowus/silver/server/akka/http/HttpServerStartup.scala`

**Evidence:** anon-2.jsonl:1202 · comment 497987974 · PR 9049 · 2024-05-03

Source path: `akka-http-commons/src/main/scala/com/endowus/silver/server/akka/http/HttpServerStartup.scala`

**Explicit source context (pr_title):**

> DYNAMIC-1046: Terminate service if onMemberUp fails (ready for review)

## A2-1210 — ThresholdBreachedRebalanceRestrictionSpec: permitted

**Source stance:** suggestion

**Context:**

> PR 9101 (Feat/INV-2746 dpm threshold rebalance), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/ThresholdBreachedRebalanceRestrictionSpec.scala; original row 1210.

**Source-preserving request, proposal, or question:**

> permitted

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1210 · comment 499780625 · PR 9101 · 2024-05-10

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/ThresholdBreachedRebalanceRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:1210 · comment 499780625 · PR 9101 · 2024-05-10

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/ThresholdBreachedRebalanceRestrictionSpec.scala`

**Explicit source context (hunk):**

> +      val responseFut = serviceLogic.checkCustomerTradingRestriction(customerId, referenceId)(request)
> +
> +      Then("request is permitted")
> +      responseFut.map { response =>
> +        response shouldBe Permitted(referenceId)
> +      }
> +    }

**Evidence:** anon-2.jsonl:1210 · comment 499780625 · PR 9101 · 2024-05-10

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/ThresholdBreachedRebalanceRestrictionSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2746 dpm threshold rebalance

## A2-1211 — ThresholdBreachedRebalanceRestrictionSpec: Can we also add more tests that:

**Source stance:** suggestion

**Context:**

> PR 9101 (Feat/INV-2746 dpm threshold rebalance), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/ThresholdBreachedRebalanceRestrictionSpec.scala; original row 1211.

**Concern stated in the source:** Can we also add more tests that:

* request is permitted for DPM goal even if currently breaching CR
* request is permitted for normal goal even if currently breaching CR
* request is permitted for normal goal even if currently breaching CRA \(which I believe is missing in your current impl\)

‌

**Source-preserving request, proposal, or question:**

> Can we also add more tests that:
> 
> * request is permitted for DPM goal even if currently breaching CR
> * request is permitted for normal goal even if currently breaching CR
> * request is permitted for normal goal even if currently breaching CRA \(which I believe is missing in your current impl\)
> 
> ‌

**Conditions and limits:**

- Requested tests permit DPM goal under CR breach, normal goal under CR breach, and normal goal under CRA breach; last may be missing in current implementation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1211 · comment 499780977 · PR 9101 · 2024-05-10

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/ThresholdBreachedRebalanceRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:1211 · comment 499780977 · PR 9101 · 2024-05-10

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/ThresholdBreachedRebalanceRestrictionSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2746 dpm threshold rebalance

## A2-1221 — ThresholdBreachedRebalanceRestrictionSpec: Not matching scenario description

**Source stance:** observed-defect

**Context:**

> PR 9101 (Feat/INV-2746 dpm threshold rebalance), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/ThresholdBreachedRebalanceRestrictionSpec.scala; original row 1221.

**Source-preserving request, proposal, or question:**

> Not matching scenario description

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Scenario description and asserted Blocked(CraCat2WithDiscretionaryPortfolio) mismatch; short comment does not settle which should change.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1221 · comment 500212243 · PR 9101 · 2024-05-13

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/ThresholdBreachedRebalanceRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:1221 · comment 500212243 · PR 9101 · 2024-05-13

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/ThresholdBreachedRebalanceRestrictionSpec.scala`

**Explicit source context (hunk):**

> +      Then("request is blocked")
> +      responseFut.map { response =>
> +        response shouldBe Blocked(referenceId, Set(CraCat2WithDiscretionaryPortfolio))
> +      }
> +    }
> +
> +    Scenario(s"success if customer is dpm eligible and its a dpm goal, even though customer has CR breach cat 1") {

**Evidence:** anon-2.jsonl:1221 · comment 500212243 · PR 9101 · 2024-05-13

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/ThresholdBreachedRebalanceRestrictionSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2746 dpm threshold rebalance

## A2-1228 — ComplianceHelper: This we can remove, and just `RegionSpecific` for impl

**Source stance:** suggestion

**Context:**

> PR 9082 (Feat/INV-2598 duplicate goal name handling), goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/ComplianceHelper.scala; original row 1228.

**Concern stated in the source:** This we can remove, and just `RegionSpecific` for impl

**Source-preserving request, proposal, or question:**

> This we can remove, and just `RegionSpecific` for impl

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1228 · comment 498857540 · PR 9082 · 2024-05-07

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/ComplianceHelper.scala`

**Evidence:** anon-2.jsonl:1228 · comment 498857540 · PR 9082 · 2024-05-07

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/ComplianceHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-2598 duplicate goal name handling

## A2-1240 — package: No need to say `PlanAccount` again I think. How about these names?

**Source stance:** suggestion

**Context:**

> PR 8984 (TT-4211 investment auto fund model), investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala; original row 1240.

**Concern stated in the source:** No need to say `PlanAccount` again I think. How about these names?

```
sealed trait PlanFundingInstructions
case class SpecifiedAccountPlanFundingInstructions(...)
case class PlanAccountPlanFundingInstructions(..., planAutoFundDetails: Option[PlanAutoFundDetails])

sealed trait FundingInstructions
case class SpecifiedAccountFundingInstructions(...)
case class PlanAccountFundingInstructions(..., autoFundDetails: Option[AutoFundDetails])
```

‌

I’m inclined to use “Details” instead so not to confuse with the outer “Instruction”

**Source-preserving request, proposal, or question:**

> No need to say `PlanAccount` again I think. How about these names?
> 
> ```
> sealed trait PlanFundingInstructions
> case class SpecifiedAccountPlanFundingInstructions(...)
> case class PlanAccountPlanFundingInstructions(..., planAutoFundDetails: Option[PlanAutoFundDetails])
> 
> sealed trait FundingInstructions
> case class SpecifiedAccountFundingInstructions(...)
> case class PlanAccountFundingInstructions(..., autoFundDetails: Option[AutoFundDetails])
> ```
> 
> ‌
> 
> I’m inclined to use “Details” instead so not to confuse with the outer “Instruction”

**Conditions and limits:**

- Details naming is an initial preference; row 1243 later accepts keeping Instruction naming with a narrower rename.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1240 · comment 498394970 · PR 8984 · 2024-05-06

Source path: `investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala`

**Evidence:** anon-2.jsonl:1240 · comment 498394970 · PR 8984 · 2024-05-06

Source path: `investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala`

**Explicit source context (pr_title):**

> TT-4211 investment auto fund model

## A2-1243 — package: [person] I’m ok with this too :see_no_evil: 

**Source stance:** suggestion

**Context:**

> PR 8984 (TT-4211 investment auto fund model), investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala; original row 1243.

**Concern stated in the source:** [person] I’m ok with this too :see_no_evil: 

```
sealed trait PlanFundingInstructions
case class SpecifiedAccountPlanFundingInstructions(...)
case class PlanAccountPlanFundingInstructions(..., planAutoFundInstruction: Option[PlanAutoFundInstruction])

sealed trait FundingInstructions
case class SpecifiedAccountFundingInstructions(...)
case class PlanAccountFundingInstructions(..., autoFundInstruction: Option[AutoFundInstruction])
```

‌

So basically keeping things intact, and only rename in this PR

`PlanAccountPlanAutoFundInstruction` → `PlanAutoFundInstruction` 

‌

**Source-preserving request, proposal, or question:**

> [person] I’m ok with this too :see_no_evil: 
> 
> ```
> sealed trait PlanFundingInstructions
> case class SpecifiedAccountPlanFundingInstructions(...)
> case class PlanAccountPlanFundingInstructions(..., planAutoFundInstruction: Option[PlanAutoFundInstruction])
> 
> sealed trait FundingInstructions
> case class SpecifiedAccountFundingInstructions(...)
> case class PlanAccountFundingInstructions(..., autoFundInstruction: Option[AutoFundInstruction])
> ```
> 
> ‌
> 
> So basically keeping things intact, and only rename in this PR
> 
> `PlanAccountPlanAutoFundInstruction` → `PlanAutoFundInstruction` 
> 
> ‌

**Conditions and limits:**

- Accepted narrow rename: PlanAccountPlanAutoFundInstruction→PlanAutoFundInstruction; retain this separately from initial Details preference.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1243 · comment 498474798 · PR 8984 · 2024-05-06

Source path: `investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala`

> I’m ok with this too :see_no_evil: 
> 
> ```
> sealed trait PlanFundingInstructions
> case class SpecifiedAccountPlanFundingInstructions(...)
> case class PlanAccountPlanFundingInstructions(..., planAutoFundInstruction: Option[PlanAutoFundInstruction])
> 
> sealed trait FundingInstructions
> case class SpecifiedAccountFundingInstructions(...)
> case class PlanAccountFundingInstructions(..., autoFundInstruction: Option[AutoFundInstruction])
> ```
> 
> ‌
> 
> So basically keeping things intact, and only rename in this PR
> 
> `PlanAccountPlanAutoFundInstruction` → `PlanAutoFundInstruction` 
> 
> ‌

**Evidence:** anon-2.jsonl:1243 · comment 498474798 · PR 8984 · 2024-05-06

Source path: `investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala`

**Explicit source context (pr_title):**

> TT-4211 investment auto fund model

## A2-1261 — HkGoalCreateSimulationSummaryBehaviour: This method should be generic to support all types of portfolioId-specific request \(as opposed to TAA-specific request for FundSmart\)

**Source stance:** suggestion

**Context:**

> PR 8933 (Feat/INV-2808/flagship dpm goal create endpoints), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/hk/HkGoalCreateSimulationSummaryBehaviour.scala; original row 1261.

**Source-preserving request, proposal, or question:**

> This method should be generic to support all types of portfolioId-specific request \(as opposed to TAA-specific request for FundSmart\)

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1261 · comment 494560014 · PR 8933 · 2024-04-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/hk/HkGoalCreateSimulationSummaryBehaviour.scala`

**Evidence:** anon-2.jsonl:1261 · comment 494560014 · PR 8933 · 2024-04-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/hk/HkGoalCreateSimulationSummaryBehaviour.scala`

**Explicit source context (pr_title):**

> Feat/INV-2808/flagship dpm goal create endpoints

## A2-1307 — Wrongly deleted fee-redemption recovery: first order stays deleted, second assumption restores, confirmations complete

**Source stance:** reported-verification

**Context:**

> PR 9060 ([INV-3021] fix(charge)(redemption)(transaction): Recover wrongly deleted fee redemption trade. To revert after data is fixed), no inline path; original row 1307.

**Source-preserving request, proposal, or question:**

> ## Test setup
> 
> Trading: `SUBMITTED_EXTERNALLY`
> 
> ‌
> 
> Redemption: `TRADE_SUBMITTED_EXTERNALLY_PENDING_SETTLEMENT`
> 
> ‌
> 
> Charge: `WITHDRAWAL_IN_PROGRESS`
> 
> ‌
> 
> Transaction: `SUBMITTED_EXTERNALLY_AND_PENDING_SETTLEMENT`
> 
> ‌
> 
> ## Reproduce
> 
> ‌
> 
> Trading: `DELETED`
> 
> ‌
> 
> Redemption: `DELETED` with `deletedAt`
> 
> ‌
> 
> Charge: `DELETED`
> 
> ‌
> 
> Transaction: `DELETED`
> 
> ‌
> 
> ## Assume first order
> 
> ‌
> 
> Trading: still `DELETED`. One order has `settlementAssumption` without deletedAt
> 
> ‌
> 
> Redemption: still `DELETED` with `deletedAt`. One order has settlement assumed details without `deletedAt`
> 
> ‌
> 
> Transaction now skip the invalid `RedemptionRequestOrderSettlementAssumedMsg` message instead getting stuck
> 
> ![](<url>
> ‌
> 
> ## Assume second order
> 
> ‌
> 
> Trading: recover to `SETTLEMENT_ASSUMED_WAITING_FOR_CONFIRMATION`
> 
> ‌
> 
> Redemption: recover to `TRADE_SETTLEMENT_ASSUMED_PENDING_CONFIRMATION` without `deletedAt`
> 
> ‌
> 
> Transaction: recover to `SETTLEMENT_ASSUMED_AND_PENDING_FINAL_CONFIRMATION` without `deletedAt`
> 
> ‌
> 
> ## Confirm both orders
> 
> Trading: successfully reach `COMPLETED` with updated `finalStatusConfirmedAt`, and without `deletedAt`
> 
> ‌
> 
> Redemption: successfully reach `COMPLETED` with `completedAt`
> 
> ‌
> 
> Charge: successfully reach `FEE_CHARGE_COMPLETED`
> 
> ‌
> 
> Transaction: successfully reach `SETTLEMENT_CONFIRMED`
> 
> ‌

**Conditions and limits:**

- Reported staged test only; do not generalize this temporary recovery PR into a permanent production workflow. Large repeated state JSON was inspected selectively for statuses, amount/order split and recovery fields; incidental IDs/accounts/timestamps are excluded.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ## Test setup
> 
> Trading: `SUBMITTED_EXTERNALLY`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Redemption: `TRADE_SUBMITTED_EXTERNALLY_PENDING_SETTLEMENT`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Charge: `WITHDRAWAL_IN_PROGRESS`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Transaction: `SUBMITTED_EXTERNALLY_AND_PENDING_SETTLEMENT`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> ## Reproduce

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Trading: `DELETED`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Redemption: `DELETED` with `deletedAt`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Charge: `DELETED`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Transaction: `DELETED`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> ## Assume first order

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Trading: still `DELETED`. One order has `settlementAssumption` without deletedAt

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Redemption: still `DELETED` with `deletedAt`. One order has settlement assumed details without `deletedAt`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Transaction now skip the invalid `RedemptionRequestOrderSettlementAssumedMsg` message instead getting stuck
> 
> ![](<url>
> ‌
> 
> ## Assume second order

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Trading: recover to `SETTLEMENT_ASSUMED_WAITING_FOR_CONFIRMATION`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Redemption: recover to `TRADE_SETTLEMENT_ASSUMED_PENDING_CONFIRMATION` without `deletedAt`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Transaction: recover to `SETTLEMENT_ASSUMED_AND_PENDING_FINAL_CONFIRMATION` without `deletedAt`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> ## Confirm both orders
> 
> Trading: successfully reach `COMPLETED` with updated `finalStatusConfirmedAt`, and without `deletedAt`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Redemption: successfully reach `COMPLETED` with `completedAt`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Charge: successfully reach `FEE_CHARGE_COMPLETED`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Transaction: successfully reach `SETTLEMENT_CONFIRMED`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> "forceDelete": true

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> "forceSettle": true

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> "requestedAmount": 13.19

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> "requestedAmount": 6.59

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> "requestedAmount": 6.6

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

**Explicit source context (pr_title):**

> [INV-3021] fix(charge)(redemption)(transaction): Recover wrongly deleted fee redemption trade. To revert after data is fixed

## A2-1310 — D56 abort rejected withdrawal dividend: 187.44 switches to cash balance; 12.56 reinvestment remains unchanged

**Source stance:** reported-verification

**Context:**

> PR 9037 ([INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested), no inline path; original row 1310.

**Source-preserving request, proposal, or question:**

> Tested in d56
> 
> ‌
> 
> Setup dividend \+ rejected withdrawal
> 
> * withdrawal with amount 187.44 is rejected
> * dividend has distribution withdrawal pref, amount = 187.44, stuck in Processing
> * another dividend with same distribution has distribution reinvested pref, amount = 12.56, in Processing \(not affected\)
> 
> ![](<url>
> dividend svc logs error as expected when received `WithdrawalRequestRejectedMsg` from trading svc
> 
> ‌
> 
> Trigger abort endpoint
> 
> Results:
> 
> * withdrawal with amount 187.44 is still rejected \(in tact\)
> * previously stuck dividend now has distribution cash balance pref, amount = 187.44, and is completed
> * the other dividend with same distribution is not affected
> 
> ![](<url>
> timeseries svc processes the new event and update distribution pref correctly
> 
> ‌
> 
> Inspection reports DividendWithdrawalRequestAbortedEvt with overridingDistributionPreference=DistributeCashBalance, and final Distributed state.

**Conditions and limits:**

- Reported D56 test affects only 187.44 withdrawal dividend; 12.56 reinvestment dividend in same distribution is a negative/control case. Incidental entity/account identifiers omitted.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> Tested in d56
> 
> ‌
> 
> Setup dividend \+ rejected withdrawal
> 
> * withdrawal with amount 187.44 is rejected
> * dividend has distribution withdrawal pref, amount = 187.44, stuck in Processing
> * another dividend with same distribution has distribution reinvested pref, amount = 12.56, in Processing \(not affected\)
> 
> ![](<url>
> dividend svc logs error as expected when received `WithdrawalRequestRejectedMsg` from trading svc
> 
> ‌
> 
> Trigger abort endpoint

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> Results:
> 
> * withdrawal with amount 187.44 is still rejected \(in tact\)
> * previously stuck dividend now has distribution cash balance pref, amount = 187.44, and is completed
> * the other dividend with same distribution is not affected
> 
> ![](<url>
> timeseries svc processes the new event and update distribution pref correctly
> 
> ‌

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "eventName": "DividendWithdrawalRequestAbortedEvt"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "overridingDistributionPreference": "DistributeCashBalance"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "distributionPreference": "DistributeCashBalance"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "_type": "com.endowus.silver.dividend.impl.entities.dividend.ces.Distributed"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

**Explicit source context (pr_title):**

> [INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested

## A2-1317 — SgTradabilityCheckerTest: Can we rename these 2 methods, maybe initGoal vs initPlan?

**Source stance:** suggestion

**Context:**

> PR 9007 (Feat/INV-2818 tradability check), investment-impl/src/test/scala/com/endowus/silver/investment/impl/utils/SgTradabilityCheckerTest.scala; original row 1317.

**Source-preserving request, proposal, or question:**

> Can we rename these 2 methods, maybe initGoal vs initPlan?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1317 · comment 496520890 · PR 9007 · 2024-04-29

Source path: `investment-impl/src/test/scala/com/endowus/silver/investment/impl/utils/SgTradabilityCheckerTest.scala`

**Evidence:** anon-2.jsonl:1317 · comment 496520890 · PR 9007 · 2024-04-29

Source path: `investment-impl/src/test/scala/com/endowus/silver/investment/impl/utils/SgTradabilityCheckerTest.scala`

**Explicit source context (hunk):**

>        initInstruments(Seq(buySellFund.withAllowedInvestorTypes(Set(SINGAPORE_CASH_ACCREDITED_INVESTOR))))
>        initCustomer(isAi = true, CustomerStatus.ACTIVE)
> -      sut.isDividendReinvestmentAllowed(customerId, "instrument").map { result =>
> +      initGoal(isDpmGoal = false)
> +      initPlan()
> +      sut.isDividendReinvestmentAllowed(customerId, "instrument", planId).map { result =>
>          result shouldBe empty

**Evidence:** anon-2.jsonl:1317 · comment 496520890 · PR 9007 · 2024-04-29

Source path: `investment-impl/src/test/scala/com/endowus/silver/investment/impl/utils/SgTradabilityCheckerTest.scala`

**Explicit source context (pr_title):**

> Feat/INV-2818 tradability check

## A2-1345 — package: Many fields of same type next to each other makes this very easy to mess sth up during refactoring if we are not careful. Let’s just use this syntax instead

**Source stance:** suggestion

**Context:**

> PR 8692 ([EN-3026] Add funding instructions to add goal flow), advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/invest/package.scala; original row 1345.

**Concern stated in the source:** Many fields of same type next to each other makes this very easy to mess sth up during refactoring if we are not careful. Let’s just use this syntax instead

```
case r: SpecifiedAccountFundingInstructionsRequest => r.indicativeFxAmount
```

‌

**Source-preserving request, proposal, or question:**

> Many fields of same type next to each other makes this very easy to mess sth up during refactoring if we are not careful. Let’s just use this syntax instead
> 
> ```
> case r: SpecifiedAccountFundingInstructionsRequest => r.indicativeFxAmount
> ```
> 
> ‌

**Conditions and limits:**

- Type-pattern access to r.indicativeFxAmount avoids positional mistakes among many same-typed fields.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1345 · comment 484820008 · PR 8692 · 2024-03-25

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/invest/package.scala`

**Evidence:** anon-2.jsonl:1345 · comment 484820008 · PR 8692 · 2024-03-25

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/invest/package.scala`

**Explicit source context (pr_title):**

> [EN-3026] Add funding instructions to add goal flow

## A2-1354 — package: Let’s support specific instrumentIds too, so that we can run for a few for adhoc check purpose

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-api/src/main/scala/com/endowus/silver/marketdata/api/requests/package.scala; original row 1354.

**Concern stated in the source:** Let’s support specific instrumentIds too, so that we can run for a few for adhoc check purpose

**Source-preserving request, proposal, or question:**

> Let’s support specific instrumentIds too, so that we can run for a few for adhoc check purpose

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1354 · comment 493330477 · PR 8931 · 2024-04-17

Source path: `marketdata-api/src/main/scala/com/endowus/silver/marketdata/api/requests/package.scala`

**Evidence:** anon-2.jsonl:1354 · comment 493330477 · PR 8931 · 2024-04-17

Source path: `marketdata-api/src/main/scala/com/endowus/silver/marketdata/api/requests/package.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1359 — MarketDataUploader: I think no need to log this, or just debug for testing. This will generate a lot of logs we don’t need

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1359.

**Source-preserving request, proposal, or question:**

> I think no need to log this, or just debug for testing. This will generate a lot of logs we don’t need

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1359 · comment 493342863 · PR 8931 · 2024-04-17

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1359 · comment 493342863 · PR 8931 · 2024-04-17

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1372 — MarketDataUploaderTest: Hmm both of tests are not really asserting anything, cuz the logic can only be observed via logs.

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/test/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploaderTest.scala; original row 1372.

**Concern stated in the source:** Hmm both of tests are not really asserting anything, cuz the logic can only be observed via logs.

Maybe we can consider creating a case class for the result and make `reconcilePrices` return it

```
case class InstrumentPriceReconResult(
  instrumentId: String,
  mismatchDates: Set[LocalDate],
  missingInDbDates: Set[LocalDate],
  missingInMStarDates: Set[LocalDate]
)
```

‌

Then we can unit test various cases for `reconcilePrices`, while the unit test for `reconcileInstrumentsPrice` would focus on testing the instrument lookup \+ skip processing on failure

**Source-preserving request, proposal, or question:**

> Hmm both of tests are not really asserting anything, cuz the logic can only be observed via logs.
> 
> Maybe we can consider creating a case class for the result and make `reconcilePrices` return it
> 
> ```
> case class InstrumentPriceReconResult(
>   instrumentId: String,
>   mismatchDates: Set[LocalDate],
>   missingInDbDates: Set[LocalDate],
>   missingInMStarDates: Set[LocalDate]
> )
> ```
> 
> ‌
> 
> Then we can unit test various cases for `reconcilePrices`, while the unit test for `reconcileInstrumentsPrice` would focus on testing the instrument lookup \+ skip processing on failure

**Conditions and limits:**

- Return InstrumentPriceReconResult (mismatch/missing-in-DB/missing-in-MStar dates) so tests assert results rather than only unobserved logs; orchestration tests focus lookup and skip-on-failure.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1372 · comment 495206240 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/test/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploaderTest.scala`

**Evidence:** anon-2.jsonl:1372 · comment 495206240 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/test/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploaderTest.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1392 — GoalModificationRestrictionSpec: blocked

**Source stance:** suggestion

**Context:**

> PR 8885 (Feat/INV-2852 goal modify trade restriction), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalModificationRestrictionSpec.scala; original row 1392.

**Source-preserving request, proposal, or question:**

> blocked

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- The hunk asserts Blocked(referenceId,Set(CraCat2WithDiscretionaryPortfolio)); the terse word blocked appears to align scenario wording with this expected outcome.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1392 · comment 491011014 · PR 8885 · 2024-04-11

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalModificationRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:1392 · comment 491011014 · PR 8885 · 2024-04-11

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalModificationRestrictionSpec.scala`

**Explicit source context (hunk):**

> +      )
> +
> +      Then("request is blocked")
> +      responseFut.map { response =>
> +        response shouldBe Blocked(referenceId, Set(CraCat2WithDiscretionaryPortfolio))
> +      }
> +    }

**Evidence:** anon-2.jsonl:1392 · comment 491011014 · PR 8885 · 2024-04-11

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalModificationRestrictionSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2852 goal modify trade restriction

## A2-1393 — GoalModificationWithPortfolioSimulationRestrictionSpec: Can we split the test cases, similar to `GoalCreationFromPortfolioSimulationRestrictionSpec` and `GoalCreationFromPortfol...

**Source stance:** suggestion

**Context:**

> PR 8885 (Feat/INV-2852 goal modify trade restriction), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionSpec.scala; original row 1393.

**Concern stated in the source:** Can we split the test cases, similar to `GoalCreationFromPortfolioSimulationRestrictionSpec` and `GoalCreationFromPortfolioSimulationRestrictionDpmSpec` \(only DPM significant tests\)?

‌

**Source-preserving request, proposal, or question:**

> Can we split the test cases, similar to `GoalCreationFromPortfolioSimulationRestrictionSpec` and `GoalCreationFromPortfolioSimulationRestrictionDpmSpec` \(only DPM significant tests\)?
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1393 · comment 491012014 · PR 8885 · 2024-04-11

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:1393 · comment 491012014 · PR 8885 · 2024-04-11

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2852 goal modify trade restriction

## A2-1395 — GoalModificationWithPortfolioSimulationRestrictionDpmSpec: Feels like lots of duplicated tests in here, while missing some other cases specific to DPM

**Source stance:** suggestion

**Context:**

> PR 8885 (Feat/INV-2852 goal modify trade restriction), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionDpmSpec.scala; original row 1395.

**Concern stated in the source:** Feels like lots of duplicated tests in here, while missing some other cases specific to DPM

Generally I think it’s ok to piggy-pack on the GoalCreate\*Spec for most of the CRA\+CR checks, and GoalModify\*Spec should just focus on the part specific to goal modify, e.g. portfolio lookup.

But if we want to more test cases, then I think for DPM we should cover these:

* Blocked

    * CraCat3
    * CraCat2WithDiscretionaryPortfolio \(no need so many cases like this current file\)
    * IneligibleForDiscretionaryPortfolio \(missing in this test\)
    * CraCat1WithConcentrationRiskBreach
    
* Permitted

    * Retail with PI funds
    * Aggressive complex
    * normal vanilla CraCat1
    

‌

**Source-preserving request, proposal, or question:**

> Feels like lots of duplicated tests in here, while missing some other cases specific to DPM
> 
> Generally I think it’s ok to piggy-pack on the GoalCreate\*Spec for most of the CRA\+CR checks, and GoalModify\*Spec should just focus on the part specific to goal modify, e.g. portfolio lookup.
> 
> But if we want to more test cases, then I think for DPM we should cover these:
> 
> * Blocked
> 
>     * CraCat3
>     * CraCat2WithDiscretionaryPortfolio \(no need so many cases like this current file\)
>     * IneligibleForDiscretionaryPortfolio \(missing in this test\)
>     * CraCat1WithConcentrationRiskBreach
>     
> * Permitted
> 
>     * Retail with PI funds
>     * Aggressive complex
>     * normal vanilla CraCat1
>     
> 
> ‌

**Conditions and limits:**

- Reuse GoalCreate CRA/CR coverage; GoalModify focuses portfolio lookup plus DPM-specific blocked CraCat3/CraCat2WithDiscretionaryPortfolio/IneligibleForDiscretionaryPortfolio/CraCat1WithConcentrationRiskBreach and permitted Retail-with-PI/aggressive-complex/vanilla-CraCat1.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1395 · comment 491268211 · PR 8885 · 2024-04-12

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionDpmSpec.scala`

**Evidence:** anon-2.jsonl:1395 · comment 491268211 · PR 8885 · 2024-04-12

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionDpmSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2852 goal modify trade restriction

## A2-1396 — GoalModificationWithPortfolioSimulationRestrictionDpmSpec: ineligible

**Source stance:** suggestion

**Context:**

> PR 8885 (Feat/INV-2852 goal modify trade restriction), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionDpmSpec.scala; original row 1396.

**Source-preserving request, proposal, or question:**

> ineligible

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- The hunk fixture describes retail with ineligible DPM; source requests ineligible naming.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1396 · comment 491292453 · PR 8885 · 2024-04-12

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionDpmSpec.scala`

**Evidence:** anon-2.jsonl:1396 · comment 491292453 · PR 8885 · 2024-04-12

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionDpmSpec.scala`

**Explicit source context (hunk):**

> +      `setupAdvisoryService / getCraDetails / customerWithValidCra`(customerId, RiskProfile.ConservativeRiskProfile)
> +
> +      And("Customer is Non PI, with ineligible DPM")
> +      `setupCustomerService / getRegionalCustomer`(customerId, Some(RetailInvestor))
> +
> +      And("customer has existing investments")
> +      setupCustomerGoals(customerId, Map(planId1 -> partiallyComplexModerateRiskMultiFundPortfolioName), baseGoal = Some(

**Evidence:** anon-2.jsonl:1396 · comment 491292453 · PR 8885 · 2024-04-12

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionDpmSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2852 goal modify trade restriction

## A2-1470 — PlanUpsertSimulationRestrictionSpec: This doesnt seem to match the test. Expired CRA? But the setup is valid conservative

**Source stance:** explanation

**Context:**

> PR 8820 (Feat/INV-2779 trading simulation restriction dpm compliance), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/PlanUpsertSimulationRestrictionSpec.scala; original row 1470.

**Source-preserving request, proposal, or question:**

> This doesnt seem to match the test. Expired CRA? But the setup is valid conservative

**Conditions and limits:**

- Test description says expired CRA but fixture is valid conservative; mismatch must be fixed.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1470 · comment 486029814 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/PlanUpsertSimulationRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:1470 · comment 486029814 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/PlanUpsertSimulationRestrictionSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2779 trading simulation restriction dpm compliance

## A2-1471 — HkServiceLogicMockUtils: Did you mean to use FlagshipDpm? Otherwise maybe default to FundSmart?

**Source stance:** open-question

**Context:**

> PR 8820 (Feat/INV-2779 trading simulation restriction dpm compliance), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/utils/HkServiceLogicMockUtils.scala; original row 1471.

**Concern stated in the source:** Did you mean to use FlagshipDpm? Otherwise maybe default to FundSmart?

**Source-preserving request, proposal, or question:**

> Did you mean to use FlagshipDpm? Otherwise maybe default to FundSmart?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1471 · comment 486030570 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/utils/HkServiceLogicMockUtils.scala`

**Evidence:** anon-2.jsonl:1471 · comment 486030570 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/utils/HkServiceLogicMockUtils.scala`

**Explicit source context (pr_title):**

> Feat/INV-2779 trading simulation restriction dpm compliance

## A2-1472 — GoalCreationFromPortfolioSimulationRestrictionSpec: goal creation from portfolio

**Source stance:** suggestion

**Context:**

> PR 8820 (Feat/INV-2779 trading simulation restriction dpm compliance), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionSpec.scala; original row 1472.

**Source-preserving request, proposal, or question:**

> goal creation from portfolio

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1472 · comment 486030709 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:1472 · comment 486030709 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionSpec.scala`

**Explicit source context (hunk):**

> +
> +  info("As a customer")
> +  info("I want to be able to perform compliance check on my goal creation from portfolio simulation intention")
> +  info("So I can know if it is permitted (with or without warnings)")
> +  info("Or if it is blocked by compliance errors")
> +
> +  Scenario("Request for goal creation simulation without any investment cannot be constructed") {

**Evidence:** anon-2.jsonl:1472 · comment 486030709 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2779 trading simulation restriction dpm compliance

## A2-1473 — GoalCreationFromPortfolioSimulationRestrictionSpec: I’m thinking this test is quite big. Should we consider split into 2 files?

**Source stance:** suggestion

**Context:**

> PR 8820 (Feat/INV-2779 trading simulation restriction dpm compliance), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionSpec.scala; original row 1473.

**Concern stated in the source:** I’m thinking this test is quite big. Should we consider split into 2 files?

* GoalCreationFromPortfolioSimulationRestrictionSpec: just cover basic flow that we lookup TAA from portfolio.. no need to duplicate everything
* GoalCreationFromDpmPortfolioSimulationRestrictionSpec: cover stuff that are specific to DPM… again no need to duplicate everything

‌

**Source-preserving request, proposal, or question:**

> I’m thinking this test is quite big. Should we consider split into 2 files?
> 
> * GoalCreationFromPortfolioSimulationRestrictionSpec: just cover basic flow that we lookup TAA from portfolio.. no need to duplicate everything
> * GoalCreationFromDpmPortfolioSimulationRestrictionSpec: cover stuff that are specific to DPM… again no need to duplicate everything
> 
> ‌

**Conditions and limits:**

- Split common portfolio lookup coverage from DPM-specific restriction tests instead of duplicating everything.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1473 · comment 486032061 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:1473 · comment 486032061 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2779 trading simulation restriction dpm compliance

## A2-1477 — GoalCreationFromPortfolioSimulationRestrictionDpmSpec: Let’s add blocked-on-CAT2 here. Also permitted-for-complex-aggressive

**Source stance:** suggestion

**Context:**

> PR 8820 (Feat/INV-2779 trading simulation restriction dpm compliance), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionDpmSpec.scala; original row 1477.

**Source-preserving request, proposal, or question:**

> Let’s add blocked-on-CAT2 here. Also permitted-for-complex-aggressive

**Conditions and limits:**

- Add blocked-on-CAT2 and permitted complex-aggressive tests.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1477 · comment 486107902 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionDpmSpec.scala`

**Evidence:** anon-2.jsonl:1477 · comment 486107902 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionDpmSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2779 trading simulation restriction dpm compliance

## A2-1478 — PlanUpsertSimulationRestrictionSpec: Ok let’s update the scenario description then..

**Source stance:** explanation

**Context:**

> PR 8820 (Feat/INV-2779 trading simulation restriction dpm compliance), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/PlanUpsertSimulationRestrictionSpec.scala; original row 1478.

**Source-preserving request, proposal, or question:**

> Ok let’s update the scenario description then..

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1478 · comment 486109088 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/PlanUpsertSimulationRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:1478 · comment 486109088 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/PlanUpsertSimulationRestrictionSpec.scala`

**Explicit source context (hunk):**

>      }
>  
> +    Scenario(s"Retail customer requests to simulate one time investment on existing DPM plan with PI Instruments") {
> +      Given("customer has conservative valid cra")
> +      `setupAdvisoryService / getCraDetails / customerWithValidCra`(customerId, RiskProfile.ConservativeRiskProfile)
> +
> +      Given("DPM goal with PI instruments")

**Evidence:** anon-2.jsonl:1478 · comment 486109088 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/PlanUpsertSimulationRestrictionSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2779 trading simulation restriction dpm compliance

## A2-1479 — GoalCreationFromPortfolioSimulationRestrictionDpmSpec: This riskTolerance should be low value to prove that we skip aggressive-complex check right? i.e. if you flip `isDiscretio...

**Source stance:** suggestion

**Context:**

> PR 8820 (Feat/INV-2779 trading simulation restriction dpm compliance), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionDpmSpec.scala; original row 1479.

**Concern stated in the source:** This riskTolerance should be low value to prove that we skip aggressive-complex check right? i.e. if you flip `isDiscretionaryPortfolio` to false, this test should fail

**Source-preserving request, proposal, or question:**

> This riskTolerance should be low value to prove that we skip aggressive-complex check right? i.e. if you flip `isDiscretionaryPortfolio` to false, this test should fail

**Conditions and limits:**

- Use low riskTolerance to prove the discretionary bypass; flipping isDiscretionaryPortfolio=false should make the test fail.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1479 · comment 486174267 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionDpmSpec.scala`

**Evidence:** anon-2.jsonl:1479 · comment 486174267 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionDpmSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2779 trading simulation restriction dpm compliance

## A2-1481 — GoalCreationRestrictionSpec: Is this same as 

**Source stance:** open-question

**Context:**

> PR 8832 ([INV-2780] feat(compliance): Trading restriction discretionary portfolio), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalCreationRestrictionSpec.scala; original row 1481.

**Concern stated in the source:** Is this same as 

```
Scenario(s"Customer with ineligible DPM requests to create goal of $portfolioName with only no investment (save only)")
```

‌

**Source-preserving request, proposal, or question:**

> Is this same as 
> 
> ```
> Scenario(s"Customer with ineligible DPM requests to create goal of $portfolioName with only no investment (save only)")
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1481 · comment 486533850 · PR 8832 · 2024-03-28

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalCreationRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:1481 · comment 486533850 · PR 8832 · 2024-03-28

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalCreationRestrictionSpec.scala`

**Explicit source context (pr_title):**

> [INV-2780] feat(compliance): Trading restriction discretionary portfolio

## A2-1502 — UpdateTradeFxConversionRequestIdCmdHandler: Are you planning to use same cmd handler for future cases of `fundingInstructions`?

**Source stance:** open-question

**Context:**

> PR 8663 (TT-3887 Update trade and investment request with queued FX conversion request ID), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeFxConversionRequestIdCmdHandler.scala; original row 1502.

**Concern stated in the source:** Are you planning to use same cmd handler for future cases of `fundingInstructions`?

* if yes, then probably should make this cmd \+ event a bit more generic
* otherwise, let’s also match Some\(\_\) and throw? And maybe rename this cmd \+ event to be a bit specific about fx id of this auto fx funding instructions.

Same suggestion on investment svc side

‌

**Source-preserving request, proposal, or question:**

> Are you planning to use same cmd handler for future cases of `fundingInstructions`?
> 
> * if yes, then probably should make this cmd \+ event a bit more generic
> * otherwise, let’s also match Some\(\_\) and throw? And maybe rename this cmd \+ event to be a bit specific about fx id of this auto fx funding instructions.
> 
> Same suggestion on investment svc side
> 
> ‌

**Conditions and limits:**

- If command will cover future funding instructions, make it generic; otherwise reject existing Some and name specifically for autofx id. Same consideration applies in investment service.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1502 · comment 481440066 · PR 8663 · 2024-03-13

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeFxConversionRequestIdCmdHandler.scala`

**Evidence:** anon-2.jsonl:1502 · comment 481440066 · PR 8663 · 2024-03-13

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeFxConversionRequestIdCmdHandler.scala`

**Explicit source context (pr_title):**

> TT-3887 Update trade and investment request with queued FX conversion request ID

## A2-1524 — SgGoalCreateValidationBehaviour: [person] I asked [person] to call `getAdvisoryQuestionnaire` again here and cross check that specified response from FE is actually one of the r...

**Source stance:** suggestion

**Context:**

> PR 8619 (Resolve INV-2765: Endpoint to derive advisory questionnaire for a given set of instruments.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateValidationBehaviour.scala; original row 1524.

**Concern stated in the source:** [person] I asked [person] to call `getAdvisoryQuestionnaire` again here and cross check that specified response from FE is actually one of the returned eligible questionnaire

**Source-preserving request, proposal, or question:**

> [person] I asked [person] to call `getAdvisoryQuestionnaire` again here and cross check that specified response from FE is actually one of the returned eligible questionnaire

**Conditions and limits:**

- Requery getAdvisoryQuestionnaire to verify FE-selected response belongs to returned eligible questionnaires.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1524 · comment 481755556 · PR 8619 · 2024-03-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateValidationBehaviour.scala`

> I asked

**Evidence:** anon-2.jsonl:1524 · comment 481755556 · PR 8619 · 2024-03-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateValidationBehaviour.scala`

> to call `getAdvisoryQuestionnaire` again here and cross check that specified response from FE is actually one of the returned eligible questionnaire

**Evidence:** anon-2.jsonl:1524 · comment 481755556 · PR 8619 · 2024-03-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateValidationBehaviour.scala`

**Explicit source context (pr_title):**

> Resolve INV-2765: Endpoint to derive advisory questionnaire for a given set of instruments.

## A2-1530 — SgGoalCreateSummaryBehaviour: I think this one doesn’t have to be productline, cuz it’s very specific to single fund FundSmart. Maybe just put a simple helper trait and extends ...

**Source stance:** suggestion

**Context:**

> PR 8488 (Resolve INV-2640: Changes to include estimation for multi-fund goal access fee for single fund goal creation.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateSummaryBehaviour.scala; original row 1530.

**Concern stated in the source:** I think this one doesn’t have to be productline, cuz it’s very specific to single fund FundSmart. Maybe just put a simple helper trait and extends only for the `FundSmartInvestmentSummary` trait?

**Source-preserving request, proposal, or question:**

> I think this one doesn’t have to be productline, cuz it’s very specific to single fund FundSmart. Maybe just put a simple helper trait and extends only for the `FundSmartInvestmentSummary` trait?

**Conditions and limits:**

- Single-fund FundSmart fee-estimation helper need not be productline-wide.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1530 · comment 482634982 · PR 8488 · 2024-03-18

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateSummaryBehaviour.scala`

**Evidence:** anon-2.jsonl:1530 · comment 482634982 · PR 8488 · 2024-03-18

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateSummaryBehaviour.scala`

**Explicit source context (pr_title):**

> Resolve INV-2640: Changes to include estimation for multi-fund goal access fee for single fund goal creation.

## A2-1533 — FundSmartHelper: fee <- `estimateAccessFee`

**Source stance:** suggestion

**Context:**

> PR 8488 (Resolve INV-2640: Changes to include estimation for multi-fund goal access fee for single fund goal creation.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala; original row 1533.

**Concern stated in the source:** fee <- `estimateAccessFee`

maybeMulti <- if\(special\) `estimateAccessFeeSpecial` else Future\(None\)

yield case class

‌

**Source-preserving request, proposal, or question:**

> fee <- `estimateAccessFee`
> 
> maybeMulti <- if\(special\) `estimateAccessFeeSpecial` else Future\(None\)
> 
> yield case class
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1533 · comment 483363691 · PR 8488 · 2024-03-20

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala`

**Evidence:** anon-2.jsonl:1533 · comment 483363691 · PR 8488 · 2024-03-20

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala`

**Explicit source context (pr_title):**

> Resolve INV-2640: Changes to include estimation for multi-fund goal access fee for single fund goal creation.

## A2-1558 — FxWalletQuotationServiceImplSpec: It’s more about scaffeine behaviour, but I think it’s useful to capture this in a test

**Source stance:** suggestion

**Context:**

> PR 8496 (TT-3906 New API to get cached indicative FX rates), fxwallet-impl/src/test/scala/com/endowus/silver/fxwallet/impl/logic/service/FxWalletQuotationServiceImplSpec.scala; original row 1558.

**Concern stated in the source:** It’s more about scaffeine behaviour, but I think it’s useful to capture this in a test

‌

```
when(fxBrokerMock.createQuotation)
  .thenReturn(_ => Future.failed(new Exception("some error")))
  .thenReturn(_ => Future.successful(fxQuotation))
```

then make 2 calls to `getIndicativeFxQuotation` and verify the error is not cached, and that 2nd call will get successful response

**Source-preserving request, proposal, or question:**

> It’s more about scaffeine behaviour, but I think it’s useful to capture this in a test
> 
> ‌
> 
> ```
> when(fxBrokerMock.createQuotation)
>   .thenReturn(_ => Future.failed(new Exception("some error")))
>   .thenReturn(_ => Future.successful(fxQuotation))
> ```
> 
> then make 2 calls to `getIndicativeFxQuotation` and verify the error is not cached, and that 2nd call will get successful response

**Conditions and limits:**

- Sequential mock first fails then succeeds; two getIndicativeFxQuotation calls should prove Scaffeine does not cache failures.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1558 · comment 479880342 · PR 8496 · 2024-03-08

Source path: `fxwallet-impl/src/test/scala/com/endowus/silver/fxwallet/impl/logic/service/FxWalletQuotationServiceImplSpec.scala`

**Evidence:** anon-2.jsonl:1558 · comment 479880342 · PR 8496 · 2024-03-08

Source path: `fxwallet-impl/src/test/scala/com/endowus/silver/fxwallet/impl/logic/service/FxWalletQuotationServiceImplSpec.scala`

**Explicit source context (pr_title):**

> TT-3906 New API to get cached indicative FX rates

## A2-1574 — D56 redemption threshold tests: 97% full flag and 10% MV tolerance; final example has inconsistent request flag

**Source stance:** reported-verification

**Context:**

> PR 8598 ([INV-2125] feat(redemption): Cross check against plan balance if not full redemption), no inline path; original row 1574.

**Source-preserving request, proposal, or question:**

> Reported wealth-admin D56 redemption checks: amount 10000 without full flag returns 400 requiring full flag; with full flag returns 400 because requested 10000 differs from market value 8098.81 by >10%; amount 8000 (>97%) without flag returns 400 requiring full flag. Final section is titled >97% with full flag and reports successful full redemption, but the displayed request says isFullRedemption=false while returned result says true; the source is internally inconsistent.

**Conditions and limits:**

- Reported final >97%-with-flag case has an internal inconsistency: heading says with full redemption flag but request JSON shows isFullRedemption=false; result isFullRedemption=true. Preserve uncertainty instead of silently correcting payload.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> Tested in wealth-admin d56

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> ### Too large amount without full redemption flag

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> ### Too large amount with full redemption flag

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> ### >97% amount without full redemption flag

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> ### >97% amount with full redemption flag

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> "requestedAmount": 10000

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> "requestedAmount": 8000

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> "isFullRedemption": false

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> "isFullRedemption": true

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> gives 400 BadRequest

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> Requires isFullRedemption = true to proceed with specified redemption request

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> Requested amount (10000) and market value of units (8098.81) differ by more than 10%

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> and it goes through creating full redemption correctly

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

> "status": "TRADE_ORDERS_GENERATED_WAITING_FOR_EXTERNAL_SUBMISSION"

**Evidence:** anon-2.jsonl:1574 · comment 479871570 · PR 8598 · 2024-03-08

**Explicit source context (pr_title):**

> [INV-2125] feat(redemption): Cross check against plan balance if not full redemption

## A2-1580 — RebateDistributionRequestJdbcRepositoryTest: Is it duplicate test? It’s not mockDb btw, it’s real embedded pg

**Source stance:** open-question

**Context:**

> PR 8587 ([INV-1996] feat(rebate): dry run fixes), rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepositoryTest.scala; original row 1580.

**Source-preserving request, proposal, or question:**

> Is it duplicate test? It’s not mockDb btw, it’s real embedded pg

**Conditions and limits:**

- Test uses actual embedded Postgres, not mockDb; duplication is a question.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1580 · comment 479855723 · PR 8587 · 2024-03-08

Source path: `rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepositoryTest.scala`

**Evidence:** anon-2.jsonl:1580 · comment 479855723 · PR 8587 · 2024-03-08

Source path: `rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepositoryTest.scala`

**Explicit source context (pr_title):**

> [INV-1996] feat(rebate): dry run fixes

## A2-1581 — RebateDistributionCommunicationsManagerTest: I haven’t figured out exactly why yet, but this extra whitespace here gonna mess with the test run

**Source stance:** explanation

**Context:**

> PR 8587 ([INV-1996] feat(rebate): dry run fixes), rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManagerTest.scala; original row 1581.

**Source-preserving request, proposal, or question:**

> I haven’t figured out exactly why yet, but this extra whitespace here gonna mess with the test run

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- The whitespace issue is observed but explicitly unexplained; hunk removes trailing space in test-suite name.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1581 · comment 479856941 · PR 8587 · 2024-03-08

Source path: `rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManagerTest.scala`

**Evidence:** anon-2.jsonl:1581 · comment 479856941 · PR 8587 · 2024-03-08

Source path: `rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManagerTest.scala`

**Explicit source context (hunk):**

>    }
>  
> -  "triggerRebateDistributionCommunications " should {
> +  "triggerRebateDistributionCommunications" should {
>  
>      val sgdInstrument = sgInstrument(UUID.randomUUID.toString)
>        .withName("SGD Retail instrument")

**Evidence:** anon-2.jsonl:1581 · comment 479856941 · PR 8587 · 2024-03-08

Source path: `rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManagerTest.scala`

**Explicit source context (pr_title):**

> [INV-1996] feat(rebate): dry run fixes

## A2-1582 — RebateDistributionCommunicationsManagerTest: I’m not sure about this test, cuz this in fact would trigger the `require` guard to fail.

**Source stance:** open-question

**Context:**

> PR 8587 ([INV-1996] feat(rebate): dry run fixes), rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManagerTest.scala; original row 1582.

**Concern stated in the source:** I’m not sure about this test, cuz this in fact would trigger the `require` guard to fail.

`setupCustomerMocks` should not return customer 2 and 3 if they don’t have rebates

**Source-preserving request, proposal, or question:**

> I’m not sure about this test, cuz this in fact would trigger the `require` guard to fail.
> 
> `setupCustomerMocks` should not return customer 2 and 3 if they don’t have rebates

**Conditions and limits:**

- setupCustomerMocks should not return customers without rebates because the new require would reject them.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1582 · comment 479857051 · PR 8587 · 2024-03-08

Source path: `rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManagerTest.scala`

**Evidence:** anon-2.jsonl:1582 · comment 479857051 · PR 8587 · 2024-03-08

Source path: `rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManagerTest.scala`

**Explicit source context (pr_title):**

> [INV-1996] feat(rebate): dry run fixes

## A2-1590 — package: As in we should only serdes the individual case class via the trait `FundingInstructionsDto` only. No one should serdes `SpecifiedAccountFundingInstructionsDto` directl...

**Source stance:** suggestion

**Context:**

> PR 7947 (TT-3480 Add funding instructions to investment request), investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala; original row 1590.

**Concern stated in the source:** As in we should only serdes the individual case class via the trait `FundingInstructionsDto` only. No one should serdes `SpecifiedAccountFundingInstructionsDto` directly, hence its formatter should stay private

**Source-preserving request, proposal, or question:**

> As in we should only serdes the individual case class via the trait `FundingInstructionsDto` only. No one should serdes `SpecifiedAccountFundingInstructionsDto` directly, hence its formatter should stay private

**Conditions and limits:**

- Serialize through sealed FundingInstructionsDto only; subtype SpecifiedAccountFundingInstructionsDto formatter remains private.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1590 · comment 477278503 · PR 7947 · 2024-03-01

Source path: `investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala`

**Evidence:** anon-2.jsonl:1590 · comment 477278503 · PR 7947 · 2024-03-01

Source path: `investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala`

**Explicit source context (pr_title):**

> TT-3480 Add funding instructions to investment request

## A2-1641 — AdvisoryDataTranslationManagerSpec: We prefer to keep the fake translated value, e.g. `Translated Template Description` so that tests are readable. Translation is actually just ...

**Source stance:** suggestion

**Context:**

> PR 8302 ([EN-2909] feat(advisory): Update recommended model portfolio names), advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/AdvisoryDataTranslationManagerSpec.scala; original row 1641.

**Concern stated in the source:** We prefer to keep the fake translated value, e.g. `Translated Template Description` so that tests are readable. Translation is actually just a generic setter

**Source-preserving request, proposal, or question:**

> We prefer to keep the fake translated value, e.g. `Translated Template Description` so that tests are readable. Translation is actually just a generic setter

**Conditions and limits:**

- Readable fake translated values are preferred in tests because translation is a generic setter.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1641 · comment 473663166 · PR 8302 · 2024-02-20

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/AdvisoryDataTranslationManagerSpec.scala`

**Evidence:** anon-2.jsonl:1641 · comment 473663166 · PR 8302 · 2024-02-20

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/AdvisoryDataTranslationManagerSpec.scala`

**Explicit source context (pr_title):**

> [EN-2909] feat(advisory): Update recommended model portfolio names

## A2-1643 — UpdateTemplateDisplayName: You can do sth like this

**Source stance:** suggestion

**Context:**

> PR 8302 ([EN-2909] feat(advisory): Update recommended model portfolio names), amend-scripts/src/main/scala/advisory/UpdateTemplateDisplayName.scala; original row 1643.

**Concern stated in the source:** You can do sth like this

```
  trait TokenProvider {
    def cfAccessToken: String = config.getString("CF_ACCESS_TOKEN")
  }

  trait AdvisoryServiceWithCf extends AdvisoryService with CloudflareFilterAddOn with TokenProvider
  
  private val advisoryService = serviceClient.implement[AdvisoryServiceWithCf]
```

‌

Then can just use `advisoryService` normally without having to specify the request header every time. `TokenProvider` probably can be moved to a common trait too, but we never moved for amend-scripts :sweat_smile:

**Source-preserving request, proposal, or question:**

> You can do sth like this
> 
> ```
>   trait TokenProvider {
>     def cfAccessToken: String = config.getString("CF_ACCESS_TOKEN")
>   }
> 
>   trait AdvisoryServiceWithCf extends AdvisoryService with CloudflareFilterAddOn with TokenProvider
>   
>   private val advisoryService = serviceClient.implement[AdvisoryServiceWithCf]
> ```
> 
> ‌
> 
> Then can just use `advisoryService` normally without having to specify the request header every time. `TokenProvider` probably can be moved to a common trait too, but we never moved for amend-scripts :sweat_smile:

**Conditions and limits:**

- Cloudflare token is read from config in trait; no credential literal is present. Use serviceClient.implement once rather than adding header on every call.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1643 · comment 473665298 · PR 8302 · 2024-02-20

Source path: `amend-scripts/src/main/scala/advisory/UpdateTemplateDisplayName.scala`

**Evidence:** anon-2.jsonl:1643 · comment 473665298 · PR 8302 · 2024-02-20

Source path: `amend-scripts/src/main/scala/advisory/UpdateTemplateDisplayName.scala`

**Explicit source context (pr_title):**

> [EN-2909] feat(advisory): Update recommended model portfolio names

## A2-1660 — enums: Maybe ask [person] and [person], but if unsure, I’d name them closer to the specs, e.g. TransactionClassification or sth.. at least people have been discussing about clas...

**Source stance:** suggestion

**Context:**

> PR 8193 (Feat/INV-2101 execution advisory transaction tagging), silver-commons/src/main/scala/com/endowus/silver/commons/models/enums.scala; original row 1660.

**Concern stated in the source:** Maybe ask [person] and [person], but if unsure, I’d name them closer to the specs, e.g. TransactionClassification or sth.. at least people have been discussing about classifying transaction, not “advisory level”

**Source-preserving request, proposal, or question:**

> Maybe ask [person] and [person], but if unsure, I’d name them closer to the specs, e.g. TransactionClassification or sth.. at least people have been discussing about classifying transaction, not “advisory level”

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1660 · comment 465917239 · PR 8193 · 2024-01-29

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/enums.scala`

> Maybe ask

**Evidence:** anon-2.jsonl:1660 · comment 465917239 · PR 8193 · 2024-01-29

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/enums.scala`

> and

**Evidence:** anon-2.jsonl:1660 · comment 465917239 · PR 8193 · 2024-01-29

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/enums.scala`

> , but if unsure, I’d name them closer to the specs, e.g. TransactionClassification or sth.. at least people have been discussing about classifying transaction, not “advisory level”

**Evidence:** anon-2.jsonl:1660 · comment 465917239 · PR 8193 · 2024-01-29

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/enums.scala`

**Explicit source context (pr_title):**

> Feat/INV-2101 execution advisory transaction tagging

## A2-1668 — AdvisoryServiceE4s: Don’t use this one. Locale has special formatter, so we want to use the implicit one in `ParameterSerializersE4s`

**Source stance:** suggestion

**Context:**

> PR 8161 (INV-2486: Add translation logic for fund smart templates.), advisory-api/src/main/scala/com/endowus/silver/advisory/api/AdvisoryServiceE4s.scala; original row 1668.

**Concern stated in the source:** Don’t use this one. Locale has special formatter, so we want to use the implicit one in `ParameterSerializersE4s`

```
  implicit val queryStringParamLocale: QueryStringParam[Locale] =
    stringQueryString.xmapWithCodec(localeUnitCodec)
```

‌

**Source-preserving request, proposal, or question:**

> Don’t use this one. Locale has special formatter, so we want to use the implicit one in `ParameterSerializersE4s`
> 
> ```
>   implicit val queryStringParamLocale: QueryStringParam[Locale] =
>     stringQueryString.xmapWithCodec(localeUnitCodec)
> ```
> 
> ‌

**Conditions and limits:**

- Locale must use ParameterSerializersE4s stringQueryString.xmapWithCodec(localeUnitCodec), not default serializer.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1668 · comment 465169414 · PR 8161 · 2024-01-26

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/AdvisoryServiceE4s.scala`

**Evidence:** anon-2.jsonl:1668 · comment 465169414 · PR 8161 · 2024-01-26

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/AdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> INV-2486: Add translation logic for fund smart templates.

## A2-1676 — AdvisoryDataTranslationManagerSpec: Maybe put the one needed for the test only. Now that we have the cache to mock, for readability, maybe use English instead :rofl: 

**Source stance:** suggestion

**Context:**

> PR 8161 (INV-2486: Add translation logic for fund smart templates.), advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/AdvisoryDataTranslationManagerSpec.scala; original row 1676.

**Concern stated in the source:** Maybe put the one needed for the test only. Now that we have the cache to mock, for readability, maybe use English instead :rofl: 

I used the below instrument.. so in a way, I also assert the key lookup when validating the result

```
doAnswer { answer =>
  val translationKeys = answer.getArgument(0, classOf[Set[String]])
  Future.successful {
    translationKeys.map { key =>
      key -> key
    }.toMap
  }
}.when(instrumentTranslationCache).getCachedInstrumentTranslations(any(), any())
```

‌

**Source-preserving request, proposal, or question:**

> Maybe put the one needed for the test only. Now that we have the cache to mock, for readability, maybe use English instead :rofl: 
> 
> I used the below instrument.. so in a way, I also assert the key lookup when validating the result
> 
> ```
> doAnswer { answer =>
>   val translationKeys = answer.getArgument(0, classOf[Set[String]])
>   Future.successful {
>     translationKeys.map { key =>
>       key -> key
>     }.toMap
>   }
> }.when(instrumentTranslationCache).getCachedInstrumentTranslations(any(), any())
> ```
> 
> ‌

**Conditions and limits:**

- Test translation cache can echo key→key to assert lookup while keeping readable English fixtures.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1676 · comment 465896014 · PR 8161 · 2024-01-29

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/AdvisoryDataTranslationManagerSpec.scala`

**Evidence:** anon-2.jsonl:1676 · comment 465896014 · PR 8161 · 2024-01-29

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/AdvisoryDataTranslationManagerSpec.scala`

**Explicit source context (pr_title):**

> INV-2486: Add translation logic for fund smart templates.

## A2-1679 — RedemptionRequestTopicSubscriberV3: Let’s make this specific to fee redemption only, and move the `request.feeChargeDetails.isDefined` to require clause

**Source stance:** suggestion

**Context:**

> PR 8071 ([INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala; original row 1679.

**Concern stated in the source:** Let’s make this specific to fee redemption only, and move the `request.feeChargeDetails.isDefined` to require clause

Let’s not make assumption about single cash reservation. Today we support taking cash balance from single account, but in future we might not.

**Source-preserving request, proposal, or question:**

> Let’s make this specific to fee redemption only, and move the `request.feeChargeDetails.isDefined` to require clause
> 
> Let’s not make assumption about single cash reservation. Today we support taking cash balance from single account, but in future we might not.

**Conditions and limits:**

- Initial fee-only require proposal is corrected in row 1682 after realizing call also serves other flows. The warning against assuming one cash reservation still remains source-specific.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1679 · comment 463752982 · PR 8071 · 2024-01-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1679 · comment 463752982 · PR 8071 · 2024-01-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> [INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge

## A2-1682 — RedemptionRequestTopicSubscriberV3: Right, sorry I missed that… somehow I thought we only call only for fee \(and hence even suggest making it specific with require clause :see_...

**Source stance:** explanation

**Context:**

> PR 8071 ([INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala; original row 1682.

**Concern stated in the source:** Right, sorry I missed that… somehow I thought we only call only for fee \(and hence even suggest making it specific with require clause :see_no_evil: \)

**Source-preserving request, proposal, or question:**

> Right, sorry I missed that… somehow I thought we only call only for fee \(and hence even suggest making it specific with require clause :see_no_evil: \)

**Conditions and limits:**

- Explicit correction: the helper was not fee-only, so earlier suggested require feeChargeDetails.isDefined should not become mandatory.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1682 · comment 464188269 · PR 8071 · 2024-01-24

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1682 · comment 464188269 · PR 8071 · 2024-01-24

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> [INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge

## A2-1697 — BaseRedemptionCommunicationV2Projection: [person] can you check with [person] on how this TAA field is used? Feels very wasteful to lookup portfolio service here, while `planDto...

**Source stance:** open-question

**Context:**

> PR 7858 (Feat/INV-2276/alt emails), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 1697.

**Concern stated in the source:** [person] can you check with [person] on how this TAA field is used? Feels very wasteful to lookup portfolio service here, while `planDto.targetAssetAllocation` has almost all the data required \(except for the urls\). From the test evidence, it seems we only need the instruments' name

**Source-preserving request, proposal, or question:**

> [person] can you check with [person] on how this TAA field is used? Feels very wasteful to lookup portfolio service here, while `planDto.targetAssetAllocation` has almost all the data required \(except for the urls\). From the test evidence, it seems we only need the instruments' name

**Conditions and limits:**

- Portfolio lookup appears unnecessary if only instrument names are needed; planDto.targetAssetAllocation lacks URLs but contains almost everything else. FE usage confirmation remains open.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1697 · comment 456744467 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

> can you check with

**Evidence:** anon-2.jsonl:1697 · comment 456744467 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

> on how this TAA field is used? Feels very wasteful to lookup portfolio service here, while `planDto.targetAssetAllocation` has almost all the data required \(except for the urls\). From the test evidence, it seems we only need the instruments' name

**Evidence:** anon-2.jsonl:1697 · comment 456744467 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-2276/alt emails

## A2-1708 — CustomerMigrationProcessorTest: Below we call plusDays\(2\) and plusDays\(3\) make 28Dec onwards crossing to next year

**Source stance:** explanation

**Context:**

> PR 7986 ([INV-2475] feat(charge): Exclude pending cashOnlyFee from ongoing redemption check + add flag to support ignoreOngoingRedemptions for Alts fee charge), transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/processors/CustomerMigrationProcessorTest.scala; original row 1708.

**Source-preserving request, proposal, or question:**

> Below we call plusDays\(2\) and plusDays\(3\) make 28Dec onwards crossing to next year

**Conditions and limits:**

- plusDays(2)/plusDays(3) causes Dec28-and-later dates to cross year; preserve boundary condition.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1708 · comment 457012158 · PR 7986 · 2023-12-28

Source path: `transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/processors/CustomerMigrationProcessorTest.scala`

**Evidence:** anon-2.jsonl:1708 · comment 457012158 · PR 7986 · 2023-12-28

Source path: `transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/processors/CustomerMigrationProcessorTest.scala`

**Explicit source context (pr_title):**

> [INV-2475] feat(charge): Exclude pending cashOnlyFee from ongoing redemption check + add flag to support ignoreOngoingRedemptions for Alts fee charge

## A2-1715 — AuroraJdbcSchema: Ah yes, creating them as empty is ok. My previous comment was in context of either the repository or the dbHandler having injected database.

**Source stance:** suggestion

**Context:**

> PR 7899 (PLATFORM-1097: Rebalance service pg readside migration), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/db/AuroraJdbcSchema.scala; original row 1715.

**Concern stated in the source:** Ah yes, creating them as empty is ok. My previous comment was in context of either the repository or the dbHandler having injected database.

‌

Good examples:

```
_ <- database.run(someDbHandlerOrRepositoryInstanceWithoutInjectedDatabase.createTable)
_ <- database.run(SomeDbHandlerOrRepositoryCompanionObject.createTable)
```

In these cases, the Schema class with its injected database will decide where to create these tables. Hence we will create them in correct place \(even tho non-read-side ones will be empty cuz we haven’t migrated\)

‌

Potentially confusing example \(previous version of this PR\):

```
_ <- someDbHandlerOrRepositoryInstanceWithInjectedDatabase.createTable
```

Here, the injected database of Schema is ignored, and the dbHandler/repository will use its own injected database. And in this specific case, `rpcCommunicationDetailsJdbcRepository` and `planMarketValueJdbcHandler` both have only 1 instance using GCP jdbcDatabase.

‌

Either way, current PR looks good to me!

**Source-preserving request, proposal, or question:**

> Ah yes, creating them as empty is ok. My previous comment was in context of either the repository or the dbHandler having injected database.
> 
> ‌
> 
> Good examples:
> 
> ```
> _ <- database.run(someDbHandlerOrRepositoryInstanceWithoutInjectedDatabase.createTable)
> _ <- database.run(SomeDbHandlerOrRepositoryCompanionObject.createTable)
> ```
> 
> In these cases, the Schema class with its injected database will decide where to create these tables. Hence we will create them in correct place \(even tho non-read-side ones will be empty cuz we haven’t migrated\)
> 
> ‌
> 
> Potentially confusing example \(previous version of this PR\):
> 
> ```
> _ <- someDbHandlerOrRepositoryInstanceWithInjectedDatabase.createTable
> ```
> 
> Here, the injected database of Schema is ignored, and the dbHandler/repository will use its own injected database. And in this specific case, `rpcCommunicationDetailsJdbcRepository` and `planMarketValueJdbcHandler` both have only 1 instance using GCP jdbcDatabase.
> 
> ‌
> 
> Either way, current PR looks good to me!

**Conditions and limits:**

- The database controlling createTable matters: Schema.database.run(action) creates in chosen schema DB even if tables are empty, whereas child.createTable with injected DB silently targets child GCP. Current PR is accepted after that clarification.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1715 · comment 456713630 · PR 7899 · 2023-12-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/db/AuroraJdbcSchema.scala`

**Evidence:** anon-2.jsonl:1715 · comment 456713630 · PR 7899 · 2023-12-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/db/AuroraJdbcSchema.scala`

**Explicit source context (pr_title):**

> PLATFORM-1097: Rebalance service pg readside migration

## A2-1733 — SgFundSmartManagerV3: Yeah `performanceMap` already contains only that specific period type \(if any\)

**Source stance:** suggestion

**Context:**

> PR 7719 (Resolve INV-2348: support bulk look up of performance), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala; original row 1733.

**Concern stated in the source:** Yeah `performanceMap` already contains only that specific period type \(if any\)

```
val commonPerformancesFut = instrumentPerformanceCache.getCachedInstrumentPerformances(instrumentCcyMap, COMMON)
val fundInceptionPerformancesFut = instrumentPerformanceCache.getCachedInstrumentPerformances(instrumentCcyMap, FUND_INCEPTION)
....
lazy val commonPeriodPerformanceFut = createFuture(instrument.id, COMMON, commonPerformances)
lazy val fundInceptionPerformanceFut = createFuture(instrument.id, FUND_INCEPTION, fundInceptionPerformances)
```

‌

**Source-preserving request, proposal, or question:**

> Yeah `performanceMap` already contains only that specific period type \(if any\)
> 
> ```
> val commonPerformancesFut = instrumentPerformanceCache.getCachedInstrumentPerformances(instrumentCcyMap, COMMON)
> val fundInceptionPerformancesFut = instrumentPerformanceCache.getCachedInstrumentPerformances(instrumentCcyMap, FUND_INCEPTION)
> ....
> lazy val commonPeriodPerformanceFut = createFuture(instrument.id, COMMON, commonPerformances)
> lazy val fundInceptionPerformanceFut = createFuture(instrument.id, FUND_INCEPTION, fundInceptionPerformances)
> ```
> 
> ‌

**Conditions and limits:**

- Common/fund-inception performance Maps are already scoped by period type; lazy per-instrument Future lookup need not check cross-period data.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1733 · comment 452604255 · PR 7719 · 2023-12-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Evidence:** anon-2.jsonl:1733 · comment 452604255 · PR 7719 · 2023-12-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Explicit source context (pr_title):**

> Resolve INV-2348: support bulk look up of performance

## A2-1756 — ServiceLogicImpl: Existing impl doesn’t require ccy. If not specified, use default ccy of marketdata. Maybe we use the ccy of returned monthly changes instead to follow previous...

**Source stance:** suggestion

**Context:**

> PR 7674 (Resolve INV-2230: Update performance calculation for custom taa to return instrument performance for single fund portfolios.), performance-impl/src/main/scala/com/endowus/silver/performance/impl/logic/service/impl/ServiceLogicImpl.scala; original row 1756.

**Concern stated in the source:** Existing impl doesn’t require ccy. If not specified, use default ccy of marketdata. Maybe we use the ccy of returned monthly changes instead to follow previous logic? If no monthly changes, then it’s a not found

**Source-preserving request, proposal, or question:**

> Existing impl doesn’t require ccy. If not specified, use default ccy of marketdata. Maybe we use the ccy of returned monthly changes instead to follow previous logic? If no monthly changes, then it’s a not found

**Conditions and limits:**

- Preserve previous optional-currency behavior using returned MC currency/default marketdata currency; absent MC is NotFound.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1756 · comment 448577234 · PR 7674 · 2023-11-29

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1756 · comment 448577234 · PR 7674 · 2023-11-29

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Resolve INV-2230: Update performance calculation for custom taa to return instrument performance for single fund portfolios.

## A2-1769 — CalculationMatrix: Ah ok, for alts we still need a specifc impl, cuz we need score \+ aggressive answer flag

**Source stance:** suggestion

**Context:**

> PR 7673 (Resolve INV-2277: Add alts suitability check for instruments using LCO match.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/hk/cra/CalculationMatrix.scala; original row 1769.

**Concern stated in the source:** Ah ok, for alts we still need a specifc impl, cuz we need score \+ aggressive answer flag

**Source-preserving request, proposal, or question:**

> Ah ok, for alts we still need a specifc impl, cuz we need score \+ aggressive answer flag

**Conditions and limits:**

- Alts still needs specific criteria for score plus aggressive-answer flag.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1769 · comment 448597269 · PR 7673 · 2023-11-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/hk/cra/CalculationMatrix.scala`

**Evidence:** anon-2.jsonl:1769 · comment 448597269 · PR 7673 · 2023-11-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/hk/cra/CalculationMatrix.scala`

**Explicit source context (pr_title):**

> Resolve INV-2277: Add alts suitability check for instruments using LCO match.

## A3-0013 — InstrumentServiceImplTest.scala: We have replacement for these tests in v2 already right?

**Source stance:** open-question

**Context:**

> instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/InstrumentServiceImplTest.scala; PR: Resolve INV-2224: Switch to logic v2, wire producer.

**Source-preserving request, proposal, or question:**

> We have replacement for these tests in v2 already right?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1820 · comment 443149229 · PR 7465 · 2023-11-09

Source path: `instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/InstrumentServiceImplTest.scala`

**Evidence:** anon-2.jsonl:1820 · comment 443149229 · PR 7465 · 2023-11-09

Source path: `instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/InstrumentServiceImplTest.scala`

**Explicit source context (hunk):**

> "Instrument Service" when {
>  
> -    "getting diy instruments" should {
> -      "filter only GWA instruments correctly #1" in {
> -        val instrument1 = createInstrument("id-1", fundSmartGwa = true, fundSmartCma = false, InvestorType.SINGAPORE_CASH_RETAIL_INVESTOR)
> -        val instrument2 = createInstrument("id-2", fundSmartGwa = true, fundSmartCma = false, InvestorType.SINGAPORE_CASH_RETAIL_INVESTOR)
> -        val instrument3 = createInstrument("id-3", fundSmartGwa = true, fundSmartCma = false, InvestorType.SINGAPORE_CASH_RETAIL_INVESTOR)
> -        val instrumentsGwa = ServiceLogicImpl.filterInstruments(
> -          List(instrument1, instrument2, instrument3.copy(configDetails = None)),
> -

## A3-0026 — InstrumentV2JdbcDbHandler.scala: We don’t really need transaction for readside so we can inject db here, and return Future… it’s easier to use and mock in test if needed

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcDbHandler.scala; PR: Resolve INV-2127: New read side table instrument entity v2

**Source-preserving request, proposal, or question:**

> We don’t really need transaction for readside so we can inject db here, and return Future… it’s easier to use and mock in test if needed

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1834 · comment 439499719 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcDbHandler.scala`

**Evidence:** anon-2.jsonl:1834 · comment 439499719 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcDbHandler.scala`

**Explicit source context (hunk):**

> +  private val instruments = TableQuery[InstrumentV2Table]
> +
> +  def upsert(instrument: Instrument): Future[Unit] = {
> +    db.run(instruments.insertOrUpdate(instrument)).flatMap {
> +      case 0 | 1 => Future.unit
> +      case n     => Future.failed(new Exception(s"Expected 0 or 1 updated, but got $n"))
> +    }

## A3-0048 — Compliance retry test: trust FutureUtils or override backoff for short unit tests

**Source stance:** suggestion

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImplTest.scala; PR: [ONB-2877] feature(advisory): Added a retry mechanism for CKA checks during SG goal summary creation

**Concern stated in the source:** Otherwise you should provide a way to override the retry settings to make it way shorter in a unit test

**Source-preserving request, proposal, or question:**

> This will be very slow test… in compliance svc code, you can trust the behaviour of `FutureUtils.futureWithRetry`… no need to add this test I think.
> 
> Otherwise you should provide a way to override the retry settings to make it way shorter in a unit test

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1861 · comment 439578348 · PR 7314 · 2023-10-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImplTest.scala`

> This will be very slow test… in compliance svc code, you can trust the behaviour of `FutureUtils.futureWithRetry`… no need to add this test I think.
> 
> Otherwise you should provide a way to override the retry settings to make it way shorter in a unit test
> 
> ‌

**Evidence:** anon-2.jsonl:1861 · comment 439578348 · PR 7314 · 2023-10-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImplTest.scala`

**Explicit source context (hunk):**

> +        }.map { _ =>
> +          verify(customerService, times(1)).getCustomerV2(mockRegionalCustomerDto.customerId)
> +          // 1 invocation with 5 retries
> +          verify(customerKnowledgeAssessmentRepository, times(6)).getByCustomerId(mockRegionalCustomerDto.customerId)
> +          succeed
> +        }
> +      }

## A3-0058 — DividendTopicSubscriberV3.scala: The problem with this is it’s a bit harder to unit test just the logic, cuz you will need to mock the topic.subscriber chain We can potentially add a 

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Concern stated in the source:** The problem with this is it’s a bit harder to unit test just the logic, cuz you will need to mock the topic.subscriber chain

**Source-preserving request, proposal, or question:**

> The problem with this is it’s a bit harder to unit test just the logic, cuz you will need to mock the topic.subscriber chain
> 
> We can potentially add a `start` method to make it lazy, and only call it in Application class, similar to `SubscriberMetricsWithKamon`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1872 · comment 439563077 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1872 · comment 439563077 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +import scala.concurrent.{ExecutionContext, Future}
> +
> +class DividendTopicSubscriberV3(
> +  dividendService: DividendService,
> +  dateTimeProvider: DateTimeProvider,
> +  refProvider: PersistentEntityRefProvider
> +)(

## A3-0064 — DividendTopicSubscriberV3.scala: but you will need to mock the whole chain… doable but just boiler plate ``` dividendService .dividendTopic .subscribe .withGroupId(groupId) .atLeastOn

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Source-preserving request, proposal, or question:**

> Yes but you will need to mock the whole chain… doable but just boiler plate
> 
> ```
> dividendService
>     .dividendTopic
>     .subscribe
>     .withGroupId(groupId)
>     .atLeastOnce
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1879 · comment 439593281 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

> Yes but you will need to mock the whole chain… doable but just boiler plate
> 
> ```
> dividendService
>     .dividendTopic
>     .subscribe
>     .withGroupId(groupId)
>     .atLeastOnce
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:1879 · comment 439593281 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +import scala.concurrent.{ExecutionContext, Future}
> +
> +class DividendTopicSubscriberV3(
> +  dividendService: DividendService,
> +  dateTimeProvider: DateTimeProvider,
> +  refProvider: PersistentEntityRefProvider
> +)(

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

## A3-0078 — InstrumentV2EntityTest.scala: I don’t know exactly why yet, just these whitespace can cause the test not running if you try to run it individually

**Source stance:** explanation

**Context:**

> instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/instrument/v2/InstrumentV2EntityTest.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Concern stated in the source:** I don’t know exactly why yet, just these whitespace can cause the test not running if you try to run it individually

**Source-preserving request, proposal, or question:**

> I don’t know exactly why yet, just these whitespace can cause the test not running if you try to run it individually

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1895 · comment 437306962 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/instrument/v2/InstrumentV2EntityTest.scala`

**Evidence:** anon-2.jsonl:1895 · comment 437306962 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/instrument/v2/InstrumentV2EntityTest.scala`

**Explicit source context (hunk):**

> +      )
>  
> +      "update instrument id map successfully" in withEntitySetup(instrumentId) { driver =>
> +        val outcome = driver.runCommand(updateInstrumentIdCmd)
> +        outcome.state.instrument.get shouldBe updatedInstrument
> +        outcome.reply shouldBe InstrumentReply(updatedInstrument).success
> +        outcome.events should contain only InstrumentDetailsUpdatedEvt(updatedInstrument, "prodOps2@endowus.com")

## A3-0079 — InstrumentDataUpdateManagerV2Test.scala: We don’t need to keep recreating these every test right?

**Source stance:** open-question

**Context:**

> instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2Test.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Source-preserving request, proposal, or question:**

> We don’t need to keep recreating these every test right?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1896 · comment 437319950 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2Test.scala`

**Evidence:** anon-2.jsonl:1896 · comment 437319950 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2Test.scala`

**Explicit source context (hunk):**

> +    "addInstrumentId" should {
> +      "succeed" in withSut(creator) { sut =>
> +        val driver = sut.mockInstrumentEntity(instrumentId, Some(instrument), entityToTest)
> +
> +        val addInstrumentIdRequest = AddInstrumentIdRequest(
> +          instrumentId = instrumentId,
> +          requestBy = prodOps,

## A3-0096 — d56 RPC verification: goal modification, threshold breach, acceptance and race outcomes

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1504] feat(goal)(rebalance): Avoid race condition for TAA update between goal modification vs RPC acceptance

**Concern stated in the source:** * single goal modification
* single threshold breach
* single RPC acceptance
* race between goal modification and RPC acceptance: goal modification is rejected if RPC reaches goal svc first, otherwise RPC is ignored and overridden by goal modification

**Source-preserving request, proposal, or question:**

> Tested in d56 the following scenarios, all are working as expected
> 
> * single goal modification
> * single threshold breach
> * single RPC acceptance
> * race between goal modification and RPC acceptance: goal modification is rejected if RPC reaches goal svc first, otherwise RPC is ignored and overridden by goal modification

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The four scenarios and RPC/goal-modification race outcomes are reported verification only.

**Evidence:** anon-2.jsonl:1913 · comment 438089407 · PR 6953 · 2023-10-23

> Tested in d56 the following scenarios, all are working as expected
> 
> * single goal modification
> * single threshold breach
> * single RPC acceptance
> * race between goal modification and RPC acceptance: goal modification is rejected if RPC reaches goal svc first, otherwise RPC is ignored and overridden by goal modification
> 
> ‌

## A3-0103 — TransactionTypes.scala: Can we add tests for this too :pray:

**Source stance:** requested-change

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: [INV-1141] Fix transaction L1 dates for v2

**Source-preserving request, proposal, or question:**

> Can we add tests for this too :pray:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1920 · comment 434761909 · PR 7114 · 2023-10-11

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:1920 · comment 434761909 · PR 7114 · 2023-10-11

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> case sd: ConfirmedOrdersStatusDetailsDto =>
> +      val settledDate = sd.orders
> +        .collect {
> +          case order: SettledOrderDto if !order.isAssumed => order.settledDate
> +        }
> +        .maxByOption(_.toEpochDay)
> +        .map(_.atStartOfDay(dateTimeProvider.zoneId))

## A3-0147 — : Examples from d56 * `HARRYSFRIEND` is absolute percentage, applicable for all accounts * `HARRYCHEAP` is $10 fixed amount for SGD cash only \(fully ut

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-2014] feat(voucher)(charge): Support discount + tax simulation in fee query endpoint

**Source-preserving request, proposal, or question:**

> Examples from d56
> 
> * `HARRYSFRIEND` is absolute percentage, applicable for all accounts
> * `HARRYCHEAP` is $10 fixed amount for SGD cash only \(fully utilized\)
> 
> The following rendered response excerpt omits only customerId/goalId/planId and the incidental calculation timestamp; each plan object retains its original field/value associations:
> 
> ```json
> {
>   "planFees": [
>     {
>       "tradingAccountType": "SINGAPORE_CPF_OA_ACCOUNT",
>       "planCcy": "SGD",
>       "accumulatedFee": 49,
>       "averageFeeRatio": 0.004,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 18.37
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 30.63,
>         "taxRate": 0.08,
>         "taxAmount": 2.45
>       },
>       "totalChargeableFee": 33.08
>     },
>     {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "accumulatedFee": 12.46,
>       "averageFeeRatio": 0.005,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYCHEAP",
>           "discountedAmount": 6.23
>         },
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 6.23
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 0,
>         "taxRate": 0.08,
>         "taxAmount": 0
>       },
>       "totalChargeableFee": 0
>     },
>     {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "accumulatedFee": 0.13,
>       "averageFeeRatio": 0.005,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYCHEAP",
>           "discountedAmount": 0.06
>         },
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 0.07
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 0,
>         "taxRate": 0.08,
>         "taxAmount": 0
>       },
>       "totalChargeableFee": 0
>     },
>     {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "accumulatedFee": 0.25,
>       "averageFeeRatio": 0.0005,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYCHEAP",
>           "discountedAmount": 0.25
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 0,
>         "taxRate": 0.08,
>         "taxAmount": 0
>       },
>       "totalChargeableFee": 0
>     },
>     {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "accumulatedFee": 3.93,
>       "averageFeeRatio": 0.003,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYCHEAP",
>           "discountedAmount": 3.27
>         },
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 0.66
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 0,
>         "taxRate": 0.08,
>         "taxAmount": 0
>       },
>       "totalChargeableFee": 0
>     },
>     {
>       "tradingAccountType": "SINGAPORE_USD_CASH_ACCOUNT",
>       "planCcy": "USD",
>       "accumulatedFee": 8.96,
>       "averageFeeRatio": 0.005,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 4.48
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 4.48,
>         "taxRate": 0.08,
>         "taxAmount": 0.36
>       },
>       "totalChargeableFee": 4.84
>     },
>     {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "accumulatedFee": 3.87,
>       "averageFeeRatio": 0.003,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYCHEAP",
>           "discountedAmount": 0.19
>         },
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 0.65
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 3.03,
>         "taxRate": 0.08,
>         "taxAmount": 0.24
>       },
>       "totalChargeableFee": 3.27
>     },
>     {
>       "tradingAccountType": "SINGAPORE_USD_CASH_ACCOUNT",
>       "planCcy": "USD",
>       "accumulatedFee": 338.11,
>       "averageFeeRatio": 0.005,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 169.06
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 169.05,
>         "taxRate": 0.08,
>         "taxAmount": 13.52
>       },
>       "totalChargeableFee": 182.57
>     }
>   ]
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- This is reported d56 test output. All eight plan-local account/currency/fee-rate/voucher-discount/DiscountedPrice-base/tax/total associations are retained; no global field-line deduplication is used. Incidental customer/goal/plan IDs and calculatedAt timestamp are omitted.

**Evidence:** anon-2.jsonl:1966 · comment 431834084 · PR 7042 · 2023-09-29

> Examples from d56
> 
> * `HARRYSFRIEND` is absolute percentage, applicable for all accounts
> * `HARRYCHEAP` is $10 fixed amount for SGD cash only \(fully utilized\)

**Evidence:** anon-2.jsonl:1966 · comment 431834084 · PR 7042 · 2023-09-29

> "tradingAccountType": "SINGAPORE_CPF_OA_ACCOUNT",
>       "planCcy": "SGD",
>       "accumulatedFee": 49,
>       "averageFeeRatio": 0.004,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 18.37
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 30.63,
>         "taxRate": 0.08,
>         "taxAmount": 2.45
>       },
>       "totalChargeableFee": 33.08

**Evidence:** anon-2.jsonl:1966 · comment 431834084 · PR 7042 · 2023-09-29

> "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "accumulatedFee": 12.46,
>       "averageFeeRatio": 0.005,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYCHEAP",
>           "discountedAmount": 6.23
>         },
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 6.23
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 0,
>         "taxRate": 0.08,
>         "taxAmount": 0
>       },
>       "totalChargeableFee": 0

**Evidence:** anon-2.jsonl:1966 · comment 431834084 · PR 7042 · 2023-09-29

> "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "accumulatedFee": 0.13,
>       "averageFeeRatio": 0.005,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYCHEAP",
>           "discountedAmount": 0.06
>         },
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 0.07
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 0,
>         "taxRate": 0.08,
>         "taxAmount": 0
>       },
>       "totalChargeableFee": 0

**Evidence:** anon-2.jsonl:1966 · comment 431834084 · PR 7042 · 2023-09-29

> "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "accumulatedFee": 0.25,
>       "averageFeeRatio": 0.0005,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYCHEAP",
>           "discountedAmount": 0.25
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 0,
>         "taxRate": 0.08,
>         "taxAmount": 0
>       },
>       "totalChargeableFee": 0

**Evidence:** anon-2.jsonl:1966 · comment 431834084 · PR 7042 · 2023-09-29

> "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "accumulatedFee": 3.93,
>       "averageFeeRatio": 0.003,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYCHEAP",
>           "discountedAmount": 3.27
>         },
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 0.66
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 0,
>         "taxRate": 0.08,
>         "taxAmount": 0
>       },
>       "totalChargeableFee": 0

**Evidence:** anon-2.jsonl:1966 · comment 431834084 · PR 7042 · 2023-09-29

> "tradingAccountType": "SINGAPORE_USD_CASH_ACCOUNT",
>       "planCcy": "USD",
>       "accumulatedFee": 8.96,
>       "averageFeeRatio": 0.005,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 4.48
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 4.48,
>         "taxRate": 0.08,
>         "taxAmount": 0.36
>       },
>       "totalChargeableFee": 4.84

**Evidence:** anon-2.jsonl:1966 · comment 431834084 · PR 7042 · 2023-09-29

> "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "accumulatedFee": 3.87,
>       "averageFeeRatio": 0.003,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYCHEAP",
>           "discountedAmount": 0.19
>         },
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 0.65
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 3.03,
>         "taxRate": 0.08,
>         "taxAmount": 0.24
>       },
>       "totalChargeableFee": 3.27

**Evidence:** anon-2.jsonl:1966 · comment 431834084 · PR 7042 · 2023-09-29

> "tradingAccountType": "SINGAPORE_USD_CASH_ACCOUNT",
>       "planCcy": "USD",
>       "accumulatedFee": 338.11,
>       "averageFeeRatio": 0.005,
>       "simulatedDiscounts": [
>         {
>           "voucherCode": "HARRYSFRIEND",
>           "discountedAmount": 169.06
>         }
>       ],
>       "simulatedTaxDetails": {
>         "_type": "ChargeableTaxDetailsDto",
>         "calculationTarget": "DiscountedPrice",
>         "baseAmount": 169.05,
>         "taxRate": 0.08,
>         "taxAmount": 13.52
>       },
>       "totalChargeableFee": 182.57

## A3-0151 — : Updated simplified response model ``` { "planFees": [ { "customerId": "", "goalId": "", "planId": "", "tradingAccountType": "SINGAPORE_CPF_OA_ACCOUNT"

**Source stance:** explanation

**Context:**

> None; PR: [INV-2014] feat(voucher)(charge): Support discount + tax simulation in fee query endpoint

**Source-preserving request, proposal, or question:**

> Updated simplified response model
> 
> ```
> {
>     "planFees": [
>         {
>             "customerId": "",
>             "goalId": "",
>             "planId": "",
>             "tradingAccountType": "SINGAPORE_CPF_OA_ACCOUNT",
>             "planCcy": "SGD",
>             "accumulatedFee": 49,
>             "averageFeeRatio": 0.004,
>             "simulatedDiscounts": [
>                 {
>                     "voucherCode": "HARRYSFRIEND",
>                     "discountedAmount": 18.37
>                 }
>             ],
>             "simulatedChargeableTax": 2.45,
>             "totalChargeableFee": 33.08
>         },
>         ...
>     ]
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Updated response example is a reported model simplification, not an independent verification of fee arithmetic.

**Evidence:** anon-2.jsonl:1970 · comment 432267903 · PR 7042 · 2023-10-02

> Updated simplified response model
> 
> ```
> {
>     "planFees": [
>         {
>             "customerId": "

**Evidence:** anon-2.jsonl:1970 · comment 432267903 · PR 7042 · 2023-10-02

> ",
>             "goalId": "

**Evidence:** anon-2.jsonl:1970 · comment 432267903 · PR 7042 · 2023-10-02

> ",
>             "planId": "

**Evidence:** anon-2.jsonl:1970 · comment 432267903 · PR 7042 · 2023-10-02

> ",
>             "tradingAccountType": "SINGAPORE_CPF_OA_ACCOUNT",
>             "planCcy": "SGD",
>             "accumulatedFee": 49,
>             "averageFeeRatio": 0.004,
>             "simulatedDiscounts": [
>                 {
>                     "voucherCode": "HARRYSFRIEND",
>                     "discountedAmount": 18.37
>                 }
>             ],
>             "simulatedChargeableTax": 2.45,
>             "totalChargeableFee": 33.08
>         },
>         ...
>     ]
> }
> ```
> 
> ‌

## A3-0187 — CustomerTransactionMigrationEventProcessor.scala: I guess if you already dry run everything, then maybe it’s ok

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> I guess if you already dry run everything, then maybe it’s ok

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Dry-run condition is the comment's explicit basis for accepting the approach.

**Evidence:** anon-2.jsonl:2007 · comment 426645896 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala`

**Evidence:** anon-2.jsonl:2007 · comment 426645896 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala`

**Explicit source context (hunk):**

> +          settledDate = o.assumedDate.get,
> +          contractDate = o.assumedContractDate,
> +          //TT-1060 can use assumed date
> +          settledPriceDate = o.assumedPriceDate.getOrElse(o.assumedDate.get),
> +          isAssumed = true
> +        )
> +      case (_, Some(confirmedAt)) => SettledOrder(

## A3-0218 — Lagom/removed-Lagom error-serdes, shared breaker, whitelist and request-timeout verification matrix

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1974] feat(all-services): Consolidate svc exception serdes + circuit breaker config

**Concern stated in the source:** Able to return custom error json \(so that other services can deserialize\) instead of the default text response.

**Source-preserving request, proposal, or question:**

> ## Test setup
> 
> instrument svc: Lagom-removed with test endpoint
> 
> * serialize error using ServiceErrorCompat
> * its client services deserialize error using `LagomCompatServiceExceptionSerializer`
> 
> ```
>   def testWater(testType: String): Future[Done] = {
>     testType match {
>       case "LagomBadRequest"  => Future.failed(lagomBadRequest("Invalid request"))
>       case "EndowusNotFound"  => Future.failed(apiNotFound("Entity id not found"))
>       case "SvcException"     => Future.failed(InstrumentSvcException("MorningStar down!", InstrumentSvcErrorType.MORNINGSTAR_API_CALL_FAILURE))
>       case "RuntimeException" => Future { Option.empty.get }
>       case "Slow"             => Future { Thread.sleep(20000) }.map(_ => Done)
>       case _                  => Future.successful(Done)
>     }
>   }
> ```
> 
> ```
> restCall(Method.GET, "/api/internal/instrument/test-water?testType", testWater _)
>     .withCircuitBreaker(CircuitBreaker.identifiedBy("shared-testing")),
> ```
> 
>  
> 
> marketdata svc: Lagom with test endpoint
> 
> * serialize error using `LagomServiceExceptionSerializer`
> * its client services also deserialize error using `LagomServiceExceptionSerializer`
> 
> ```
>   override def testWater(testType: String): ServiceCall[NotUsed, Done] = ServiceCall { _ =>
>     testType match {
>       case "LagomBadRequest"  => Future.failed(BadRequest("Invalid request"))
>       case "EndowusNotFound"  => Future.failed(NotFound("Entity id not found"))
>       case "SvcException"     => Future.failed(MarketDataSvcException("MAS down!", MarketDataSvcErrorType.MAS_MAINTENANCE))
>       case "RuntimeException" => Future { List.empty(1) }
>       case "Slow"             => Future { Thread.sleep(20000) }.map(_ => Done)
>       case _                  => Future.successful(Done)
>     }
>   }
> ```
> 
> ```
> restCall(Method.GET, "/api/internal/marketdata/test-water?testType", testWater _)
>     .withCircuitBreaker(CircuitBreaker.identifiedBy("shared-testing")),
> ```
> 
>  
> 
> goal svc: Lagom-removed with test endpoint calling either instrument / marketdata svc
> 
> * serialize error using ServiceErrorCompat
> 
> ```
>   def testWater(service: String, testType: String, handleSvcErr: Boolean): Future[Done] = {
>     service match {
>       case "marketdata" =>
>         marketDataService.testWater(testType).invoke().recover {
>           case e: MarketDataSvcException =>
>             if (handleSvcErr)
>               throw GoalSvcException("Something wrong with MarketData svc", GoalSvcErrorType.SOMETHING_WRONG)
>             else throw e
>         }
>       case "instrument" =>
>         instrumentService.testWater(testType).invoke().recover {
>           case e: InstrumentSvcException =>
>             if (handleSvcErr)
>               throw GoalSvcException("Something wrong with Instrument svc", GoalSvcErrorType.SOMETHING_WRONG)
>             else throw e
>         }
>       case _ => Future.successful(Done)
>     }
>   }
> ```
> 
>  
> 
> advisory svc: Lagom with test endpoint calling either instrument / marketdata svc
> 
> * serialize error using `LagomServiceExceptionSerializer`
> * also wrap 4xx to Lagom BadRequest to avoid error logging, but this is optional \(also not in scope of this PR\)
> 
> ```
>   override def testWater(service: String, testType: String, handleSvcErr: Boolean): ServiceCall[NotUsed, Done] = {
>     LagomExceptionWrappedServiceCall { _ =>
>       service match {
>         case "marketdata" =>
>           marketDataService.testWater(testType).invoke().recover {
>             case e: MarketDataSvcException =>
>               if (handleSvcErr)
>                 throw AdvisorySvcException("Something wrong with MarketData svc", AdvisorySvcErrorType.SOMETHING_WRONG)
>               else throw e
>           }
>         case "instrument" =>
>           instrumentService.testWater(testType).invoke().recover {
>             case e: InstrumentSvcException =>
>               if (handleSvcErr)
>                 throw AdvisorySvcException("Something wrong with Instrument svc", AdvisorySvcErrorType.SOMETHING_WRONG)
>               else throw e
>           }
>         case _ => Future.successful(Done)
>       }
>     }
> ```
> 
>  
> 
> instrument svc: Lagom-removed with test heavy endpoints
> 
> ```
>   def testHeavy: Future[Done] = {
>     Future { Thread.sleep(15000) }.map(_ => Done)
>   }
>   
>   Api.testHeavy impl { _ => testHeavy },
>   Api.testHeavyWithShortTimeout impl (_ => testHeavy, CustomTimeoutProcess(10.seconds)),
> ```
> 
> ## Test scenarios
> 
> Verified that error serdes works as expected \(as per `LagomServiceExceptionSerializerSpec` / `LagomCompatServiceExceptionSerializerSpec` / `ServiceErrorCompatSpec` \) for all combinations of:
> 
> * calling various testType in test endpoint of instrument/marketdata
> * calling various testType \+ option to handle underlying SvcException in test endpoint of advisory/goal \(forwarding to instrument/marketdata\)
> 
> Verified that if we use same `CircuitBreaker.identifiedBy("shared-testing")` in both instrument and marketdata endpoints, if one triggers circuit breaker, it will affect the other.
> 
> Verified that exception whitelist works as expected. No circuit breaker triggered for BadRequest/NotFound
> 
> Verified that endpoint specific request timeout works as expected. Able to return custom error json \(so that other services can deserialize\) instead of the default text response.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Full test matrix retained: Lagom/compat serializers, handled and forwarded service exceptions, shared breaker coupling, whitelist, endpoint timeout and custom JSON response. Source snippets are test setup, not production recommendations.
- Related source rows 2038, 2040, 2041: Keep uncertain getClass observation, reported compatibility test matrix and service-prefixed breaker correction distinct.

**Evidence:** anon-2.jsonl:2040 · comment 424733479 · PR 6845 · 2023-09-04

## A3-0221 — InstrumentDailyReturnIndexDaoJdbc.scala: Change this so that we actually test the clause limit in test

**Source stance:** requested-change

**Context:**

> performance-impl/src/main/scala/com/endowus/silver/performance/impl/db/marketdata/jdbc/InstrumentDailyReturnIndexDaoJdbc.scala; PR: feat(performance): Fix flaky InstrumentDailyReturnIndexDaoJdbcTest

**Concern stated in the source:** Change this so that we actually test the clause limit in test

**Source-preserving request, proposal, or question:**

> Change this so that we actually test the clause limit in test

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2043 · comment 823818136 · PR 14248 · 2026-07-09

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/db/marketdata/jdbc/InstrumentDailyReturnIndexDaoJdbc.scala`

**Evidence:** anon-2.jsonl:2043 · comment 823818136 · PR 14248 · 2026-07-09

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/db/marketdata/jdbc/InstrumentDailyReturnIndexDaoJdbc.scala`

**Explicit source context (hunk):**

> def findMany(instrumentId: String, dates: Set[LocalDate], sort: Option[SortOrder]): Future[List[InstrumentDailyReturnIndex]] = {
>      Source(dates)
> -      .grouped(InClauseLimit)
> +      .grouped(inClauseLimit)
>        .flatMapConcat(Source.single(_).mapAsync(parallelism = 1)(findIn(instrumentId, _, sort)).mapConcat(identity))
>        .runWith(Sink.collection[InstrumentDailyReturnIndex, List[InstrumentDailyReturnIndex]])
>    }

## A3-0222 — randomizeLocalDate within10years clashes make clause-limit test flaky

**Source stance:** observed-defect

**Context:**

> performance-impl/src/test/scala/com/endowus/silver/performance/impl/db/marketdata/jdbc/InstrumentDailyReturnIndexDaoJdbcTest.scala; PR: feat(performance): Fix flaky InstrumentDailyReturnIndexDaoJdbcTest

**Concern stated in the source:** randomizeLocalDate generates within 10years, very often this generates clashes causing the test to be flaky

**Source-preserving request, proposal, or question:**

> randomizeLocalDate generates within 10years, very often this generates clashes causing the test to be flaky

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2044 · comment 823818518 · PR 14248 · 2026-07-09

Source path: `performance-impl/src/test/scala/com/endowus/silver/performance/impl/db/marketdata/jdbc/InstrumentDailyReturnIndexDaoJdbcTest.scala`

**Evidence:** anon-2.jsonl:2044 · comment 823818518 · PR 14248 · 2026-07-09

Source path: `performance-impl/src/test/scala/com/endowus/silver/performance/impl/db/marketdata/jdbc/InstrumentDailyReturnIndexDaoJdbcTest.scala`

**Explicit source context (hunk):**

> val instrumentId: String = random
> -      val items = (1 to 20).map(_ => randomItem.copy(instrumentId = instrumentId)).toList
> +      val items = (1 to 20).map(i => randomItem(date = t0d(i)).copy(instrumentId = instrumentId)).toList
>  
>        for {
>          _ <- createTable(db)

## A3-0251 — BaseChargePgTest.scala: I default to Sg for now, cuz all our tests are for SG. In here, multiple methods we also use Sg classes directly

**Source stance:** explanation

**Context:**

> charge-impl/src/test/scala/com/endowus/silver/charge/impl/utils/BaseChargePgTest.scala; PR: [INV-2012] feat(charge): Support Alts quarterly fee charge with exact amount

**Concern stated in the source:** I default to Sg for now, cuz all our tests are for SG.

**Source-preserving request, proposal, or question:**

> I default to Sg for now, cuz all our tests are for SG. In here, multiple methods we also use Sg classes directly

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2074 · comment 425183490 · PR 6856 · 2023-09-06

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/utils/BaseChargePgTest.scala`

**Evidence:** anon-2.jsonl:2074 · comment 425183490 · PR 6856 · 2023-09-06

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/utils/BaseChargePgTest.scala`

**Explicit source context (hunk):**

> -  val region: SilverRegion
> -  val timeZoneHelper: DateTimeProvider
> +  implicit val region: SilverRegion.Sg.type = SilverRegion.Sg
> +  val timeZoneHelper: DateTimeProvider = new SingaporeDateTimeProvider
> +
> +  val goalService: GoalService

## A3-0252 — TwilioSvcManagerV2.scala: cover all these cases in `TwilioSvcManagerV2Spec` otherwise it’s impossible to remember all these combinations in SG vs HK

**Source stance:** requested-change

**Context:**

> communication-impl/src/main/scala/com/endowus/silver/communication/impl/managers/TwilioSvcManagerV2.scala; PR: [EN-1989] Add handling for both one time and recurring for INVESTMENT otp

**Concern stated in the source:** let’s cover all these cases in `TwilioSvcManagerV2Spec` otherwise it’s impossible to remember all these combinations in SG vs HK

**Source-preserving request, proposal, or question:**

> let’s cover all these cases in `TwilioSvcManagerV2Spec` otherwise it’s impossible to remember all these combinations in SG vs HK

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2075 · comment 422255113 · PR 6682 · 2023-08-25

Source path: `communication-impl/src/main/scala/com/endowus/silver/communication/impl/managers/TwilioSvcManagerV2.scala`

**Evidence:** anon-2.jsonl:2075 · comment 422255113 · PR 6682 · 2023-08-25

Source path: `communication-impl/src/main/scala/com/endowus/silver/communication/impl/managers/TwilioSvcManagerV2.scala`

**Explicit source context (hunk):**

> +          currencyCode: String
> +        ): String = {
> +          (Some(oneTimeInvestmentAmount), maybeRecurringAmount.filter(_ > BigDecimal(0))) match {
> +            case (_, Some(recurring)) =>
> +              s"invest in $goalName ($accountName) and set up a recurring investment $currencyCode ${recurring.toString()}"
> +            case (_, None) => s"invest in $goalName ($accountName)"
> +          }

## A3-0259 — : Can we add tests too please, for both processor and repository

**Source stance:** requested-change

**Context:**

> None; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> Can we add tests too please, for both processor and repository

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2083 · comment 422184060 · PR 6740 · 2023-08-25

## A3-0280 — RegionalDataTest.scala: just assert on this field instead of printing and succeeded

**Source stance:** requested-change

**Context:**

> silver-commons/src/test/scala/com/endowus/silver/commons/models/data/RegionalDataTest.scala; PR: Adding base traits for regional data separation.

**Source-preserving request, proposal, or question:**

> Let’s just assert on this field instead of printing and succeeded

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2105 · comment 419986794 · PR 6698 · 2023-08-17

Source path: `silver-commons/src/test/scala/com/endowus/silver/commons/models/data/RegionalDataTest.scala`

**Evidence:** anon-2.jsonl:2105 · comment 419986794 · PR 6698 · 2023-08-17

Source path: `silver-commons/src/test/scala/com/endowus/silver/commons/models/data/RegionalDataTest.scala`

**Explicit source context (hunk):**

> +
> +        sgData.regional.stringValue shouldBe "Some Value"
> +      }
> +
> +      val json = Json
> +        .parse(
> +          """

## A3-0283 — SgRegionalData singleton SilverRegion.Sg.type makes wrong-region construction compile-time safe

**Source stance:** suggestion

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/models/data/RegionalData.scala; PR: Adding base traits for regional data separation.

**Source-preserving request, proposal, or question:**

> We can force this to be compile safe rather than runtime safe \(no need to rely on require check\)
> 
> ```
> trait RegionalData {
>   implicit def region: SilverRegion
> }
> 
> trait SgRegionalData extends RegionalData {
>   implicit def region: SilverRegion.Sg.type
> }
> 
>  --
>  
> case class SgTestRegionalData(stringValue: String)(implicit val region: SilverRegion.Sg.type) extends TestRegionalData with SgRegionalData
> 
> object SgTestRegionalData {
>   implicit val SgConvert: Convert[TestRegionalData, SilverRegion.Sg.type, SgTestRegionalData] = new SgConvert[TestRegionalData, SgTestRegionalData] {
>     override def convert(testRegionalData: TestRegionalData)(region: SilverRegion.Sg.type): SgTestRegionalData =
>       testRegionalData.asInstanceOf[SgTestRegionalData]
>   }
> 
>   implicit def format(implicit region: SilverRegion.Sg.type): Format[SgTestRegionalData] = Json.format
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Source proposes compile-time singleton SilverRegion.Sg.type requirements instead of runtime require checks.
- Related source rows 1821, 2107, 2108: Read together for Lagom Service val implementation and later regional-data singleton implicit refinements.
- Related source rows 2107, 2108: Initial broad SilverRegion implicit is refined to singletonSilverRegion.Sg.type compile-time contract.

**Evidence:** anon-2.jsonl:2108 · comment 421546456 · PR 6698 · 2023-08-23

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/data/RegionalData.scala`

> We can force this to be compile safe rather than runtime safe \(no need to rely on require check\)
> 
> ```
> trait RegionalData {
>   implicit def region: SilverRegion
> }
> 
> trait SgRegionalData extends RegionalData {
>   implicit def region: SilverRegion.Sg.type
> }
> 
>  --
>  
> case class SgTestRegionalData(stringValue: String)(implicit val region: SilverRegion.Sg.type) extends TestRegionalData with SgRegionalData
> 
> object SgTestRegionalData {
>   implicit val SgConvert: Convert[TestRegionalData, SilverRegion.Sg.type, SgTestRegionalData] = new SgConvert[TestRegionalData, SgTestRegionalData] {
>     override def convert(testRegionalData: TestRegionalData)(region: SilverRegion.Sg.type): SgTestRegionalData =
>       testRegionalData.asInstanceOf[SgTestRegionalData]
>   }
> 
>   implicit def format(implicit region: SilverRegion.Sg.type): Format[SgTestRegionalData] = Json.format
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2108 · comment 421546456 · PR 6698 · 2023-08-23

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/data/RegionalData.scala`

**Explicit source context (hunk):**

> +import play.api.libs.json.{Format, JsResult, JsValue}
> +
> +trait RegionalData
> +
> +object RegionalData {
> +
> +  class Convert[D, R <: SilverRegion, T <: RegionSpecific[R]] {

## A3-0300 — PlanCommunicationV2EventProcessorTest.scala: Can we put exact expected string these? Otherwise we’re just repeating the impl but not testing the values. Let’s also cover at least weekly/biweekly 

**Source stance:** requested-change

**Context:**

> goal-impl/src/test/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessorTest.scala; PR: [EN-2023][EN-2007](invest) Upcoming recurring investment, recurring investment cancel email/platform notifications

**Concern stated in the source:** Otherwise we’re just repeating the impl but not testing the values.

**Source-preserving request, proposal, or question:**

> Can we put exact expected string these? Otherwise we’re just repeating the impl but not testing the values. Let’s also cover at least weekly/biweekly too. You can use table driven property checks [<url> data-inline-card='' }

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2125 · comment 421209034 · PR 6724 · 2023-08-22

Source path: `goal-impl/src/test/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessorTest.scala`

**Evidence:** anon-2.jsonl:2125 · comment 421209034 · PR 6724 · 2023-08-22

Source path: `goal-impl/src/test/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessorTest.scala`

**Explicit source context (hunk):**

> currencySymbol shouldBe CurrencyUtils.getCurrencySymbol(plan.planCcy)
>                  amount shouldBe "1,000.00"
> -                detailedFrequency shouldBe s"Monthly on the ${preSchedule.startingFrom.getDayOfMonth}th"
> +                detailedFrequency shouldBe s"Monthly on the ${FormatterUtils.generateDayOrdinal(preSchedule.startingFrom.getDayOfMonth)}"
>                  stoppedReason shouldBe RecurringInvestmentStoppedReason(isFullRedemption = isFullRedemption, isManualCancellation = !isFullRedemption)
>              }
>          }

## A3-0301 — PlanCommunicationV2EventProcessorTest.scala: Or have separate unit test for `RecurringInvestmentFrequencyDetailUtil` that cover more cases

**Source stance:** suggestion

**Context:**

> goal-impl/src/test/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessorTest.scala; PR: [EN-2023][EN-2007](invest) Upcoming recurring investment, recurring investment cancel email/platform notifications

**Source-preserving request, proposal, or question:**

> Or have separate unit test for `RecurringInvestmentFrequencyDetailUtil` that cover more cases

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2126 · comment 421209196 · PR 6724 · 2023-08-22

Source path: `goal-impl/src/test/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessorTest.scala`

**Evidence:** anon-2.jsonl:2126 · comment 421209196 · PR 6724 · 2023-08-22

Source path: `goal-impl/src/test/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessorTest.scala`

**Explicit source context (hunk):**

> currencySymbol shouldBe CurrencyUtils.getCurrencySymbol(plan.planCcy)
>                  amount shouldBe "1,000.00"
> -                detailedFrequency shouldBe s"Monthly on the ${preSchedule.startingFrom.getDayOfMonth}th"
> +                detailedFrequency shouldBe s"Monthly on the ${FormatterUtils.generateDayOrdinal(preSchedule.startingFrom.getDayOfMonth)}"
>                  stoppedReason shouldBe RecurringInvestmentStoppedReason(isFullRedemption = isFullRedemption, isManualCancellation = !isFullRedemption)
>              }
>          }

## A3-0304 — RecurringInvestmentFrequencyDetailUtilTest.scala: No future so you can just use AnyWordSpec

**Source stance:** requested-change

**Context:**

> goal-impl/src/test/scala/com/endowus/silver/goal/impl/helpers/RecurringInvestmentFrequencyDetailUtilTest.scala; PR: [EN-2023][EN-2007](invest) Upcoming recurring investment, recurring investment cancel email/platform notifications

**Source-preserving request, proposal, or question:**

> No future so you can just use AnyWordSpec

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2129 · comment 421223639 · PR 6724 · 2023-08-22

Source path: `goal-impl/src/test/scala/com/endowus/silver/goal/impl/helpers/RecurringInvestmentFrequencyDetailUtilTest.scala`

**Evidence:** anon-2.jsonl:2129 · comment 421223639 · PR 6724 · 2023-08-22

Source path: `goal-impl/src/test/scala/com/endowus/silver/goal/impl/helpers/RecurringInvestmentFrequencyDetailUtilTest.scala`

**Explicit source context (hunk):**

> +
> +import java.time.LocalDate
> +
> +class RecurringInvestmentFrequencyDetailUtilTest extends AsyncWordSpec with Matchers {
> +
> +  "constructUserFriendlyFrequencyDetail" should {
> +    "construct frequency detail for weekly interval without endDetails" in {

## A3-0385 — InvestmentScheduleActivePeriod.scala: I’m surprised this works in your testing as `recurringInterval` is an option….

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/models/InvestmentScheduleActivePeriod.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> I’m surprised this works in your testing as `recurringInterval` is an option….

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2212 · comment 416496743 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/models/InvestmentScheduleActivePeriod.scala`

**Evidence:** anon-2.jsonl:2212 · comment 416496743 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/models/InvestmentScheduleActivePeriod.scala`

**Explicit source context (hunk):**

> +object InvestmentScheduleActivePeriod {
> +  implicit val format: Format[InvestmentScheduleActivePeriod] = Json.format
> +
> +  def deriveTransactedDates(activePeriod: InvestmentScheduleActivePeriod, dateToday: LocalDate): List[LocalDate] = {
> +    val endDateToUse = activePeriod.endingDate.getOrElse(dateToday)
> +
> +    Iterator.iterate(activePeriod.startingDate)(_.plus(CashflowInterval.toTemporalAmount(activePeriod.recurringInterval)))

## A3-0404 — TransactionQueryLogic.scala: HK Web query all and then filter in FE. This was spotted in e2e tests

**Source stance:** reported-verification

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala; PR: [INV-1868] fix(transaction): Support proper filter by transactionTypes for V2. Keeping it at DTO level for now.

**Source-preserving request, proposal, or question:**

> HK Web query all and then filter in FE. This was spotted in e2e tests

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2232 · comment 415975628 · PR 6615 · 2023-08-01

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Evidence:** anon-2.jsonl:2232 · comment 415975628 · PR 6615 · 2023-08-01

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (hunk):**

> -        .fold[Seq[TransactionDto]] { transactions } { t =>
> -          transactions.filter(s => s.getClass.getTypeName.contains(t))
> +        .map(_.toSet)
> +        .fold(transactions) { actualTransactionTypes =>
> +          transactions.filter(t => actualTransactionTypes.contains(t.transactionType))
>          }
>          .filterNot(_.statusDetails.transactionStatus == TransactionStatus.DELETED)

## A3-0431 — : WIP: * tested the backfill endpoint itself → works * pending: * wait for new version of readside → update query to filter * in prod it’s huge amount o

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1710] feat(amend-scripts): Add GST charge amend-scripts

**Source-preserving request, proposal, or question:**

> WIP:
> 
> * tested the backfill endpoint itself → works
> * pending:
> 
>     * wait for new version of readside → update query to filter
>     * in prod it’s huge amount of requests → slice the query / stream the result / kafka task topic?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Backfill endpoint tested; new readside/filter and production request slicing/streaming/Kafka task remain pending alternatives.

**Evidence:** anon-2.jsonl:2261 · comment 407560671 · PR 6328 · 2023-06-30

> WIP:
> 
> * tested the backfill endpoint itself → works
> * pending:
> 
>     * wait for new version of readside → update query to filter
>     * in prod it’s huge amount of requests → slice the query / stream the result / kafka task topic?
>     
> 
> ‌

## A3-0463 — StatementDataGenerator.scala: We would need to remove the absorbed tax details at transaction level in this method `calculateIfSameStatementDataExists` to avoid reprinting old stat

**Source stance:** requested-change

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala; PR: [INV-1425] feat(report): Added tax details to instrumentTransactionDto and refactor accessFeeTax statement calculation

**Source-preserving request, proposal, or question:**

> We would need to remove the absorbed tax details at transaction level in this method `calculateIfSameStatementDataExists` to avoid reprinting old statement as well.
> 
> I’ll have a query to cross check the data we backfill matches the existing data in old statements.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2296 · comment 407994107 · PR 6309 · 2023-07-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Evidence:** anon-2.jsonl:2296 · comment 407994107 · PR 6309 · 2023-07-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Explicit source context (hunk):**

> isReprint = maybeOldStatement.nonEmpty
>  
> -          sameStatementDataExists = calculateIfSameStatementDataExists(maybeOldStatement = maybeOldStatement, statementData = statementData)
> +          sameStatementDataExists = calculateIfSameStatementDataExists(maybeOldStatement = maybeOldStatement, statementData = statementData, startDateOfStatement)
>            statementInfo = StatementInfoDto(
>              statementPeriod = request.statementPeriod,
>              yearMonth = request.yearMonth,

## A3-0491 — RebalanceMsgLogicImpl.scala: Also let’s capture this logic in test

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala; PR: Resolve INV-1745: Rebalance transaction to show netted sell orders if rebalance completed without buy orders.

**Source-preserving request, proposal, or question:**

> Also let’s capture this logic in test

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2327 · comment 407562924 · PR 6322 · 2023-06-30

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala`

**Evidence:** anon-2.jsonl:2327 · comment 407562924 · PR 6322 · 2023-06-30

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala`

**Explicit source context (hunk):**

> orderAmounts.foldLeft(BigDecimal(0))((a, r) => a + r.getOrElse(BigDecimal(0)))
>    }
> +
> +  private def calculateSettledAmount(orders: List[OrderV2]): BigDecimal = {
> +    val orderAmounts = orders.collect {
> +      case settledOrder: SettledOrder => settledOrder.settledAmount
> +    }

## A3-0493 — RebalanceMsgLogicImpl.scala: And let’s capture this behaviour in tests, if not already there

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala; PR: Resolve INV-1745: Rebalance transaction to show netted sell orders if rebalance completed without buy orders.

**Source-preserving request, proposal, or question:**

> And let’s capture this behaviour in tests, if not already there

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2329 · comment 407981254 · PR 6322 · 2023-07-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala`

**Evidence:** anon-2.jsonl:2329 · comment 407981254 · PR 6322 · 2023-07-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala`

**Explicit source context (hunk):**

> // Logging to sentry so we can detect if it actually ever happens else we can get rid of this.
>        // TODO: convert to warn log or remove log once have more information on this case
> -      logger.error(s"Received RebalanceRequestDeletedMsg but marking transactionID (${msg.rebalanceRequest.rebalanceRequestId}) as confirmed as it has confirmed sell orders")
> +      logger.error(
> +        s"Received RebalanceRequestDeletedMsg but marking transactionID (${msg.rebalanceRequest.rebalanceRequestId}) as confirmed as it has confirmed sell orders"
> +      )
>        val sellOrders = getOrders(msg.rebalanceRequest.sellOrders)

## A3-0502 — RebalancePlanEntityTest.scala: check exactly new new TAA matches what provided in cmd? Also let’s verify the emitted events contain only the TAA updated evt, and nothing else. Do yo

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/test/scala/com/endowus/silver/rebalance/impl/entities/RebalancePlanEntityTest.scala; PR: Resolve INV-1750: Add cmd to manually update the TAA of the rebalance plan entity.

**Source-preserving request, proposal, or question:**

> Maybe check exactly new new TAA matches what provided in cmd?
> 
> Also let’s verify the emitted events contain only the TAA updated evt, and nothing else.
> 
> Do you want to add a few more cases in which the cmd is skipped/rejected when existing state doesn’t allow change TAA?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2338 · comment 407980732 · PR 6323 · 2023-07-03

Source path: `rebalance-impl/src/test/scala/com/endowus/silver/rebalance/impl/entities/RebalancePlanEntityTest.scala`

**Evidence:** anon-2.jsonl:2338 · comment 407980732 · PR 6323 · 2023-07-03

Source path: `rebalance-impl/src/test/scala/com/endowus/silver/rebalance/impl/entities/RebalancePlanEntityTest.scala`

**Explicit source context (hunk):**

> +
> +    val updatedTaa = driver.runCommand(cmd).state.plan.get.currentTaa
> +
> +    originalState.plan.get.currentTaa.instrumentWeights shouldNot equal(updatedTaa.instrumentWeights)
> +  }
>  }

## A3-0505 — d56 fee-withdrawal deletion test: error-before,200-after, reservation/events/DELETED checks

**Source stance:** reported-verification

**Context:**

> None; PR: [TT-2544] fix(broker)(trading): Allow deleting FeeWithdrawal request/transaction

**Source-preserving request, proposal, or question:**

> Tested the below in d56
> 
> ## Existing state
> 
> ### Transaction
> 
> "requestedAmount": 25.78,
> 
> "status": "SUBMITTED_INTERNALLY_AND_PENDING_EXTERNAL_BROKER_SUBMISSION",
> 
> ### TradingAccountEntity
> 
> Cash reservation
> 
> Withdrawal
> 
> ### Broker transaction \(contain many other fee withdrawals\)
> 
> ## Trigger withdrawal request deletion
> 
> Before fix deployment:
> 
> "error_code": "INVALID_TRANSACTION_TYPE"
> 
> After fix deployment: 200 OK
> 
> ![](<url>
> ## State after deletion
> 
> ### Broker transaction \(has deletedAt populated for corresponding `withdrawalRequestId`\)
> 
> "deletedAt": "2023-07-04T21:15:41.445097+08:00[Asia/Singapore]",
> 
> ### TradingAccountEntity
> 
> Cash reservation is deleted from state
> 
> Withdrawal \(deletedAt populated for both `brokerAccountCashWithdrawals` and withdrawalRequest\)
> 
> Events
> 
> ### Transaction
> 
> Fee withdrawal txn is deleted from A&B query. Status is updated to deleted in entity
> 
> "status": "DELETED",
> 
> 
> 
> Events (exact retained source list):
> 
> ```
> CashReservationDeletedEvt
> BrokerAccountCashBalanceUpdatedEvt
> BrokerAccountWithdrawalRequestUpdatedEvt
> CashWithdrawalRequestDeletedEvt
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Reported d56 fee-withdrawal deletion test: before INVALID_TRANSACTION_TYPE; after200; deletedAt on matching withdrawal and nested cash withdrawal, reservation removed, balance-update event emitted, four named events, transaction DELETED and absent A&B. Incidental IDs/account numbers and verbose repeated JSON omitted.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.
- Related source row2342 qualifies the balance claim: d56 cash balance was affected by test setup; only attempted recalculation and the emitted BrokerAccountCashBalanceUpdatedEvt are established, not validated balance arithmetic.

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> Tested the below in d56

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ‌
> 
> ## Existing state
> 
> ### Transaction

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> "requestedAmount": 25.78,

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> "status": "SUBMITTED_INTERNALLY_AND_PENDING_EXTERNAL_BROKER_SUBMISSION",

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ### TradingAccountEntity
> 
> Cash reservation

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> Withdrawal

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ### Broker transaction \(contain many other fee withdrawals\)

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ‌
> 
> ## Trigger withdrawal request deletion

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> Before fix deployment:

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> "error_code": "INVALID_TRANSACTION_TYPE"

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> After fix deployment: 200 OK
> 
> ![](<url>
> ## State after deletion
> 
> ### Broker transaction \(has deletedAt populated for corresponding `withdrawalRequestId`\)

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> "deletedAt": "2023-07-04T21:15:41.445097+08:00[Asia/Singapore]",

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ### TradingAccountEntity
> 
> Cash reservation is deleted from state
> 
> Withdrawal \(deletedAt populated for both `brokerAccountCashWithdrawals` and withdrawalRequest\)

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> Events

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ### Transaction
> 
> Fee withdrawal txn is deleted from A&B query. Status is updated to deleted in entity

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> "status": "DELETED",

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ‌

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> CashReservationDeletedEvt
> BrokerAccountCashBalanceUpdatedEvt
> BrokerAccountWithdrawalRequestUpdatedEvt
> CashWithdrawalRequestDeletedEvt

**Evidence:** anon-2.jsonl:2342 · comment 408504744 · PR 6354 · 2023-07-04

> The cash balance is a bit messed up due to testing in d56, but it did try to recalculate the balance.

## A3-0506 — : The cash balance is a bit messed up due to testing in d56, but it did try to recalculate the balance. The warning in transaction svc about missing fee

**Source stance:** reported-verification

**Context:**

> None; PR: [TT-2544] fix(broker)(trading): Allow deleting FeeWithdrawal request/transaction

**Source-preserving request, proposal, or question:**

> The cash balance is a bit messed up due to testing in d56, but it did try to recalculate the balance.
> 
> The warning in transaction svc about missing feeDetails is what fixed in trading, released today \(this one is old charge\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Cash balance in d56 was affected by testing; only recalculation attempt is asserted. Missing feeDetails warning relates to old charge and separate released trading fix.
- Related source row2341 contains the event/deletion test. This row limits any claim there to attempted balance recalculation; it does not verify the resulting balance amount.

**Evidence:** anon-2.jsonl:2342 · comment 408504744 · PR 6354 · 2023-07-04

## A3-0520 — SgServiceLogicImpl.scala: I’ll test this backfilling logic a bit with existing fee charge request in d56, then will drop this nested field

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala; PR: [INV-1710] feat(charge): Add endpoint to support back-filling absorbed GST in completed fee charge

**Source-preserving request, proposal, or question:**

> I’ll test this backfilling logic a bit with existing fee charge request in d56, then will drop this nested field

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2357 · comment 406623758 · PR 6306 · 2023-06-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2357 · comment 406623758 · PR 6306 · 2023-06-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      *
> +      * If full redemption fee charge crossed two quarters, e.g. 2022Q4 and beginning of 2023Q1, it was agreed that we
> +      * tax (and absorb) following tax rate of 2023Q1.
> +      */
> +    def extractTaxDate(request: FeeChargeRequest): LocalDate = {
> +      request.endDate
> +    }

## A3-0523 — SgTaxCalculator.scala: This is tested as part of the SgFeeManagerProjectionSpec and BackfillAbsorbedTaxDetailsLogicSpec.

**Source stance:** reported-verification

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/SgTaxCalculator.scala; PR: [INV-1710] feat(charge): Add endpoint to support back-filling absorbed GST in completed fee charge

**Source-preserving request, proposal, or question:**

> This is tested as part of the SgFeeManagerProjectionSpec and BackfillAbsorbedTaxDetailsLogicSpec.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2360 · comment 406979834 · PR 6306 · 2023-06-28

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/SgTaxCalculator.scala`

**Evidence:** anon-2.jsonl:2360 · comment 406979834 · PR 6306 · 2023-06-28

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/SgTaxCalculator.scala`

**Explicit source context (hunk):**

> +import java.time.LocalDate
> +import scala.math.BigDecimal.RoundingMode
> +
> +object SgTaxCalculator {
> +
> +  /**
> +    * Identify when we first capture GST in Endowus system

## A3-0575 — InvestmentPlanEntityTest.scala: please name this test

**Source stance:** requested-change

**Context:**

> investment-impl/src/test/scala/com/endowus/silver/investment/impl/entities/entities/InvestmentPlanEntityTest.scala; PR: [EN-982] fix(investment): ignore if there is no pending investment

**Source-preserving request, proposal, or question:**

> Nit: please name this test

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2422 · comment 401786054 · PR 6162 · 2023-06-08

Source path: `investment-impl/src/test/scala/com/endowus/silver/investment/impl/entities/entities/InvestmentPlanEntityTest.scala`

**Evidence:** anon-2.jsonl:2422 · comment 401786054 · PR 6162 · 2023-06-08

Source path: `investment-impl/src/test/scala/com/endowus/silver/investment/impl/entities/entities/InvestmentPlanEntityTest.scala`

**Explicit source context (hunk):**

> ex.toString shouldBe s"Unable to handleUpdateCashDividendDetailsCmd - InvestmentPlan [$entityId] does not have investment request with cashDividendId [$dividendId]"
>      }
> +
> +    "GetPendingInitialInvestmentRequestCmd return empty list when there is no initial investment" in withNoEntitySetup { driver =>
> +      val initWithNoInitialInvestment = CreateInvestmentPlanCmd(
> +        _,
> +        customerId = customerId,

## A3-0576 — Alts cashOnlyFee test:1.5M holding,10K pending,5K cash,12381.46 fee waits for funding

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1300] feat(charge)(redemption)(trading)(investment): Cash reservation for Alts fee charge

**Source-preserving request, proposal, or question:**

> Created new Alts-B3 plan:
> 
> * customerId = ``
> * goalId = ``
> * planId = ``
> 
> 
> 
> Setup existing investment \(1.5M\) \+ one pending \(10K\) with insufficient cash balance \(5K\)
> 
> Trigger Q1 charge. Calculated amount = `12381.46`
> 
> Observe that both the investment and fee redemption are in PENDING\_SUBMISSION status, and their corresponding trades are in WAITING\_FOR\_FUNDING status.
> 
> 
> 
> Fee redemption: feeChargeDetails has new field `cashOnlyFee` = true
> 
> "cashOnlyFee": true
> 
> "requestedAmount": 12381.46,
> 
> "status": "PENDING_SUBMISSION",
> 

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Alts-B3 scenario retains1.5M existing+10K pending investment,5K cash, Q1 fee12381.46, PENDING_SUBMISSION/WAITING_FOR_FUNDING and cashOnlyFee=true. Incidental IDs and verbose JSON omitted.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> Created new Alts-B3 plan:
> 
> * customerId = `

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> `
> * goalId = `

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> `
> * planId = `

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> `
> 
> ‌
> 
> Setup existing investment \(1.5M\) \+ one pending \(10K\) with insufficient cash balance \(5K\)
> 
> Trigger Q1 charge. Calculated amount = `12381.46`
> 
> Observe that both the investment and fee redemption are in PENDING\_SUBMISSION status, and their corresponding trades are in WAITING\_FOR\_FUNDING status.
> 
> ‌
> 
> Fee redemption: feeChargeDetails has new field `cashOnlyFee` = true

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> "cashOnlyFee": true

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> "requestedAmount": 12381.46,

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> "status": "PENDING_SUBMISSION",

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> ‌
> 
> ‌

## A3-0577 — CashSmartUSD cashOnlyFee=false test:173.74 fee eagerly reserves cash and completes

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1300] feat(charge)(redemption)(trading)(investment): Cash reservation for Alts fee charge

**Source-preserving request, proposal, or question:**

> Trigger charge for another normal CashSmart USD plan
> 
> * goalId = ``
> * planId = ``
> * feeAmount = `173.74`
> 
> 
> 
> Observe that this fee charge is still using eager cash reservation as existing logic. Since charge amount is under cash balance, the fee charge completed right away
> 
> 
> 
> FeeChargeRequest \(new field `cashOnlyFee` = false\)
> 
> "cashOnlyFee": false
> 
> "status": "FEE_CHARGE_COMPLETED",
> 
> Fee redemption \(new field `cashOnlyFee` = false\)
> 
> "status": "COMPLETED",
> 
> "reservedAmount": 173.74
> 
> Trade
> 

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- CashSmartUSD comparison retains173.74 fee, existing eager reservation, immediate completion under cash balance and cashOnlyFee=false. Incidental IDs and repeated JSON omitted.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> Trigger charge for another normal CashSmart USD plan
> 
> * goalId = `

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> `
> * planId = `

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> `
> * feeAmount = `173.74`
> 
> ‌
> 
> Observe that this fee charge is still using eager cash reservation as existing logic. Since charge amount is under cash balance, the fee charge completed right away
> 
> ‌
> 
> FeeChargeRequest \(new field `cashOnlyFee` = false\)

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> "cashOnlyFee": false

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> "status": "FEE_CHARGE_COMPLETED",

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> ‌
> 
> Fee redemption \(new field `cashOnlyFee` = false\)

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> "status": "COMPLETED",

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> "reservedAmount": 173.74

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> ‌
> 
> Trade

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> ‌

## A3-0578 — 15K top-up funds Alts fee before earlier investment;12381.46 fee completes

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1300] feat(charge)(redemption)(trading)(investment): Cash reservation for Alts fee charge

**Source-preserving request, proposal, or question:**

> Top up balance to 15K - which is sufficient to fund either the fee redemption / investment
> 
> 
> 
> Observe that even though investment was created first, fee redemption takes priority
> 
> 
> 
> FeeChargeRequest
> 
> "cashOnlyFee": true
> 
> "status": "FEE_CHARGE_COMPLETED",
> 
> "redeemedAmount": 12381.46,
> 
> Fee redemption
> 
> "status": "COMPLETED",
> 
> Trade
> 

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- 15K top-up can fund either investment or fee; fee redemption takes priority despite later creation. Fee12381.46 reaches completed status with cashOnlyFee=true. Repeated JSON omitted.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> Top up balance to 15K - which is sufficient to fund either the fee redemption / investment
> 
> ‌
> 
> Observe that even though investment was created first, fee redemption takes priority
> 
> ‌
> 
> FeeChargeRequest

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> "cashOnlyFee": true

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> "status": "FEE_CHARGE_COMPLETED",

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> "redeemedAmount": 12381.46,

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> ‌
> 
> Fee redemption

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> "status": "COMPLETED",

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> ‌
> 
> Trade

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> ‌

## A3-0600 — BrokerAccountTopicSubscriberTest.scala: Name should `BrokerAccountTopicSubscriberCommunicationLogic`Test/Spec

**Source stance:** requested-change

**Context:**

> investment-impl/src/test/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberTest.scala; PR: Feat/EN-982 migrate one time platform notification

**Source-preserving request, proposal, or question:**

> Name should `BrokerAccountTopicSubscriberCommunicationLogic`Test/Spec

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2447 · comment 400997709 · PR 5862 · 2023-06-07

Source path: `investment-impl/src/test/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberTest.scala`

## A3-0625 — Alts/non-Alts/SRS fee tiers stay separate when Alts goal added

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1299] feat(charge): Support Atls Fee charge calculation & trigger

**Concern stated in the source:** * SRS plan still follows flat rate 0.004
* USD Cash and SGD Cash plans still follow non-Alts tier of <= 1m at rate 0.005
* USD Cash Alts plan follows Alts tier of <= 5m at rate 0.005
* Alts and non-Alts tier are not mixed \(otherwise both would have crossed to next tier\)

**Source-preserving request, proposal, or question:**

> Tested the below in d56 using customerId = ``
> 
> ## Fee estimate in A&B
> 
> Before adding Alts goal
> 
> * SRS plan follows flat rate 0.004
> * USD Cash and SGD Cash plans are merged together for tier calculation, hence follow rate at 0.005 \(200k < AUM <= 1m\)
> 
> After adding an Alts goal
> 
> * SRS plan still follows flat rate 0.004
> * USD Cash and SGD Cash plans still follow non-Alts tier of <= 1m at rate 0.005
> * USD Cash Alts plan follows Alts tier of <= 5m at rate 0.005
> * Alts and non-Alts tier are not mixed \(otherwise both would have crossed to next tier\)
> 

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Keep exact tier comparisons: SRS flat0.004; non-Alts cash merged200k<AUM<=1m at0.005; Alts<=5m at0.005; tiers isolated before/after Alts goal.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.

**Evidence:** anon-2.jsonl:2474 · comment 395114476 · PR 5977 · 2023-05-17

> Tested the below in d56 using customerId = `

**Evidence:** anon-2.jsonl:2474 · comment 395114476 · PR 5977 · 2023-05-17

> `
> 
> ## Fee estimate in A&B
> 
> Before adding Alts goal
> 
> * SRS plan follows flat rate 0.004
> * USD Cash and SGD Cash plans are merged together for tier calculation, hence follow rate at 0.005 \(200k < AUM <= 1m\)

**Evidence:** anon-2.jsonl:2474 · comment 395114476 · PR 5977 · 2023-05-17

> ‌
> 
> After adding an Alts goal
> 
> * SRS plan still follows flat rate 0.004
> * USD Cash and SGD Cash plans still follow non-Alts tier of <= 1m at rate 0.005
> * USD Cash Alts plan follows Alts tier of <= 5m at rate 0.005
> * Alts and non-Alts tier are not mixed \(otherwise both would have crossed to next tier\)

**Evidence:** anon-2.jsonl:2474 · comment 395114476 · PR 5977 · 2023-05-17

> ‌

## A3-0626 — : ## Fee estimate in goal creation Alts MV does not interfere with non-Alts * 5000 amt → same tier → 0.005 * 500000 amt → cross to next tier → 0.0035 If

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1299] feat(charge): Support Atls Fee charge calculation & trigger

**Source-preserving request, proposal, or question:**

> ## Fee estimate in goal creation
> 
> Alts MV does not interfere with non-Alts
> 
> * 5000 amt → same tier → 0.005
> * 500000 amt → cross to next tier → 0.0035
> 
> If change to CMA, correctly use flat rate 0.0005 regardless of amount
> 
> ```
> POST <url>
> {
>     "_type": "FundSmartGoalCreateRequest",
>     "customerId": "{{customerId}}",
>     "riskTolerance": 0.3,
>     "goalType": "GENERAL_WEALTH_ACCUMULATION",
>     "tradingAccountType": "SINGAPORE_USD_CASH_ACCOUNT",
>     "targetWeights": {
>         "LU1217871216": 0.3,
>         "IE00B2PC0153": 0.7
> 
>     },
>     "initialInvestmentAmount": 5000
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2475 · comment 395115730 · PR 5977 · 2023-05-17

> ## Fee estimate in goal creation
> 
> Alts MV does not interfere with non-Alts
> 
> * 5000 amt → same tier → 0.005
> * 500000 amt → cross to next tier → 0.0035
> 
> If change to CMA, correctly use flat rate 0.0005 regardless of amount
> 
> ```
> POST <url>
> {
>     "_type": "FundSmartGoalCreateRequest",
>     "customerId": "{{customerId}}",
>     "riskTolerance": 0.3,
>     "goalType": "GENERAL_WEALTH_ACCUMULATION",
>     "tradingAccountType": "SINGAPORE_USD_CASH_ACCOUNT",
>     "targetWeights": {
>         "LU1217871216": 0.3,
>         "IE00B2PC0153": 0.7
> 
>     },
>     "initialInvestmentAmount": 5000
> }
> ```
> 
> ‌

## A3-0627 — : ## Charge for Alts ``` POST <url> { "year": 2023, "quarter": "Q1", "reason": "QUARTERLY_SCHEDULED_FEE_CHARGE", "simulateOnly": true } ``` ### Explicit

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1299] feat(charge): Support Atls Fee charge calculation & trigger

**Source-preserving request, proposal, or question:**

> ## Charge for Alts
> 
> ```
> POST <url>
> {
>     "year": 2023,
>     "quarter": "Q1",
>     "reason": "QUARTERLY_SCHEDULED_FEE_CHARGE",
>     "simulateOnly": true
> }
> ```
> 
> ### Explicitly specifying customerId and/or planId
> 
> * Correctly identify the Alts plan
> * Fee amt roughly matches \(0.005 annual rate / 365 \* 88 days\) \* 4.7m MV
> 
> ![](<url>
> ### Charge for all
> 
> * Correctly identify all Alts plans
> 
> ![](<url>
> 
> 
> Will test real charge in next task when we implement enforcement to use cash balance

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Simulation only: identified individual/all Alts plans; approx0.005/365*88*4.7m. Real cash-enforced charge remains future testing.

**Evidence:** anon-2.jsonl:2476 · comment 395120524 · PR 5977 · 2023-05-17

> ## Charge for Alts
> 
> ```
> POST <url>
> {
>     "year": 2023,
>     "quarter": "Q1",
>     "reason": "QUARTERLY_SCHEDULED_FEE_CHARGE",
>     "simulateOnly": true
> }
> ```
> 
> ### Explicitly specifying customerId and/or planId
> 
> * Correctly identify the Alts plan
> * Fee amt roughly matches \(0.005 annual rate / 365 \* 88 days\) \* 4.7m MV
> 
> ![](<url>
> ### Charge for all
> 
> * Correctly identify all Alts plans
> 
> ![](<url>
> ‌
> 
> Will test real charge in next task when we implement enforcement to use cash balance

## A3-0628 — : ## Charge for non-Alts ``` POST <url> { "year": 2023, "quarter": "Q1", "reason": "QUARTERLY_SCHEDULED_FEE_CHARGE" } ``` Fee charge request * Fee amt r

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1299] feat(charge): Support Atls Fee charge calculation & trigger

**Source-preserving request, proposal, or question:**

> ## Charge for non-Alts
> 
> Fee charge request
> 
> * Fee amt roughly matches \(0.005 annual rate / 365 \* 88 days\) \* 270k MV
> 
> "accumulatedChargeableFee": 324.19,
> 
> "totalHoldingPeriodInDays": 90,
> 
> "yearlyHoldingPeriodRatio": 0.2466,
> 
> "status": "FEE_CHARGE_COMPLETED",
> 

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.
- The source rough formula uses88days while its JSON totalHoldingPeriodInDays is90. Both literals are preserved; the source is internally inconsistent, so do not treat the rough formula as independently verified exact fee arithmetic.

**Evidence:** anon-2.jsonl:2477 · comment 395122637 · PR 5977 · 2023-05-17

> ## Charge for non-Alts

**Evidence:** anon-2.jsonl:2477 · comment 395122637 · PR 5977 · 2023-05-17

> ‌
> 
> Fee charge request
> 
> * Fee amt roughly matches \(0.005 annual rate / 365 \* 88 days\) \* 270k MV

**Evidence:** anon-2.jsonl:2477 · comment 395122637 · PR 5977 · 2023-05-17

> "accumulatedChargeableFee": 324.19,

**Evidence:** anon-2.jsonl:2477 · comment 395122637 · PR 5977 · 2023-05-17

> "totalHoldingPeriodInDays": 90,

**Evidence:** anon-2.jsonl:2477 · comment 395122637 · PR 5977 · 2023-05-17

> "yearlyHoldingPeriodRatio": 0.2466,

**Evidence:** anon-2.jsonl:2477 · comment 395122637 · PR 5977 · 2023-05-17

> "status": "FEE_CHARGE_COMPLETED",

**Evidence:** anon-2.jsonl:2477 · comment 395122637 · PR 5977 · 2023-05-17

> ‌

## A3-0629 — : Tested triggering charge via admin too. The service queries and start the charge process for all applicable plans

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1299] feat(charge): Support Atls Fee charge calculation & trigger

**Source-preserving request, proposal, or question:**

> Tested triggering charge via admin too. The service queries and start the charge process for all applicable plans

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2478 · comment 395123604 · PR 5977 · 2023-05-17

## A3-0631 — : Tested in d34. ### Invest manually with one instrument in an existing plan with 2 instruments 50-50 After investment settles, MV is updated and thresh

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1212] feat(rebalance): HK Rebalance communication for threshold breach

**Source-preserving request, proposal, or question:**

> Tested in d34.
> 
> ### Invest manually with one instrument in an existing plan with 2 instruments 50-50
> 
> After investment settles, MV is updated and threshold breach is triggered automatically
> 
> "status": "REBALANCING_SUGGESTED_PENDING_ACCEPTANCE",
> 
> "reason": "THRESHOLD_BREACH",
> 
> "instrumentWeights": {
> 
> Email communication is trigger
> 
> [<url> data-inline-card='' } 
> 
> ![](<url>
> Verified customer name, goal name, account name, action by timestamp, CTA url is correct
> 
> Clicked CTA, login and it brings to Preferences page correctly

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Manual one-instrument investment in50/50 two-instrument HK plan triggers breach after settlement/MV; notification values and Preferences CTA tested.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.
- HK scope in the authored title/constraint comes from the explicitly quoted PR title, not from the comment prose or an unavailable hunk.

**Evidence:** anon-2.jsonl:2480 · comment 391448129 · PR 5904 · 2023-05-03

> Tested in d34.
> 
> ### Invest manually with one instrument in an existing plan with 2 instruments 50-50
> 
> After investment settles, MV is updated and threshold breach is triggered automatically

**Evidence:** anon-2.jsonl:2480 · comment 391448129 · PR 5904 · 2023-05-03

> "status": "REBALANCING_SUGGESTED_PENDING_ACCEPTANCE",

**Evidence:** anon-2.jsonl:2480 · comment 391448129 · PR 5904 · 2023-05-03

> "reason": "THRESHOLD_BREACH",

**Evidence:** anon-2.jsonl:2480 · comment 391448129 · PR 5904 · 2023-05-03

> "instrumentWeights": {

**Evidence:** anon-2.jsonl:2480 · comment 391448129 · PR 5904 · 2023-05-03

> Email communication is trigger
> 
> [<url> data-inline-card='' } 
> 
> ![](<url>
> Verified customer name, goal name, account name, action by timestamp, CTA url is correct
> 
> Clicked CTA, login and it brings to Preferences page correctly
> 
> ‌

**Evidence:** anon-2.jsonl:2480 · comment 391448129 · PR 5904 · 2023-05-03

**Explicit source context (pr_title):**

> [INV-1212] feat(rebalance): HK Rebalance communication for threshold breach

## A3-0632 — : Trigger the endpoint to accept all threshold breach requests And settle the rebalance trade ``` { "rebalanceRequestId": "", "status": "REBALANCING_COM

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1212] feat(rebalance): HK Rebalance communication for threshold breach

**Source-preserving request, proposal, or question:**

> Trigger the endpoint to accept all threshold breach requests
> 
> And settle the rebalance trade
> 
> "status": "REBALANCING_COMPLETED",
> 
> "totalSoldAmount": 2003.01,
> 
> "totalPurchasedAmount": 2003.01,
> 
> Email communication is triggered
> 
> [<url> data-inline-card='' } 
> 
> ![](<url>
> Verified customer name, goal name, account name, CTA url is correct
> 
> Clicked CTA, login and it brings to A&B page correctly

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Acceptance and settlement completes rebalance; notification A&B CTA tested. Preserve reported test only, not mandate.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.

**Evidence:** anon-2.jsonl:2481 · comment 391451997 · PR 5904 · 2023-05-03

> Trigger the endpoint to accept all threshold breach requests
> 
> And settle the rebalance trade

**Evidence:** anon-2.jsonl:2481 · comment 391451997 · PR 5904 · 2023-05-03

> "status": "REBALANCING_COMPLETED",

**Evidence:** anon-2.jsonl:2481 · comment 391451997 · PR 5904 · 2023-05-03

> "totalSoldAmount": 2003.01,

**Evidence:** anon-2.jsonl:2481 · comment 391451997 · PR 5904 · 2023-05-03

> "totalPurchasedAmount": 2003.01,

**Evidence:** anon-2.jsonl:2481 · comment 391451997 · PR 5904 · 2023-05-03

> Email communication is triggered
> 
> [<url> data-inline-card='' } 
> 
> ![](<url>
> Verified customer name, goal name, account name, CTA url is correct
> 
> Clicked CTA, login and it brings to A&B page correctly

## A3-0633 — : Retested the advised template after correcting the datetime formatter \+ latest template being active [<url> data-inline-card='' } ![](<url>

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1212] feat(rebalance): HK Rebalance communication for threshold breach

**Source-preserving request, proposal, or question:**

> Retested the advised template after correcting the datetime formatter \+ latest template being active
> 
> [<url> data-inline-card='' } 
> 
> ![](<url>

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2482 · comment 391704598 · PR 5904 · 2023-05-04

> Retested the advised template after correcting the datetime formatter \+ latest template being active
> 
> [<url> data-inline-card='' } 
> 
> ![](<url>
> ‌

## A3-0638 — EmailDataFactory.scala: makes sense. I realized this when testing for rebalance communication too. I ported the same into FormatterUtils

**Source stance:** explanation

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala; PR: [INV-1353] feat(one-time email): add ONE_TIME_REQUEST_CREATED_AT field

**Source-preserving request, proposal, or question:**

> Yeah makes sense. I realized this when testing for rebalance communication too. I ported the same into FormatterUtils

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2487 · comment 391708942 · PR 5784 · 2023-05-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

## A3-0659 — : Triggered in d56 \(many instruments would have missing DistributionStatus, but that’s ok\) ![](<url>

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1528] feat(marketdata): Sync annual yield for only distributing funds

**Concern stated in the source:** Triggered in d56 \(many instruments would have missing DistributionStatus, but that’s ok\)

**Source-preserving request, proposal, or question:**

> Triggered in d56 \(many instruments would have missing DistributionStatus, but that’s ok\)
> 
> ![](<url>

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2509 · comment 391373110 · PR 5894 · 2023-05-03

> Triggered in d56 \(many instruments would have missing DistributionStatus, but that’s ok\)
> 
> ![](<url>
> ‌

## A3-0693 — : Reprocess already-processed distribution with same file name will error ![](<url>

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1484] feat(dividend)(admin): Add forceReprocess flag to trigger reprocessing of already processed dividend distribution

**Source-preserving request, proposal, or question:**

> Reprocess already-processed distribution with same file name will error
> 
> ![](<url>

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2544 · comment 390121725 · PR 5859 · 2023-04-27

> Reprocess already-processed distribution with same file name will error
> 
> ![](<url>
> ‌

## A3-0694 — : Reprocess already-processed distribution with different file name and no force flag will also error ![](<url> ![](<url>

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1484] feat(dividend)(admin): Add forceReprocess flag to trigger reprocessing of already processed dividend distribution

**Source-preserving request, proposal, or question:**

> Reprocess already-processed distribution with different file name and no force flag will also error
> 
> ![](<url>
> ![](<url>

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2545 · comment 390122735 · PR 5859 · 2023-04-27

> Reprocess already-processed distribution with different file name and no force flag will also error
> 
> ![](<url>
> ![](<url>
> ‌

## A3-0695 — : Reprocess already-processed distribution with different file name and force flag will go thru \(assuming POps knows what they are doing\) ![](<url> Sa

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1484] feat(dividend)(admin): Add forceReprocess flag to trigger reprocessing of already processed dividend distribution

**Source-preserving request, proposal, or question:**

> Reprocess already-processed distribution with different file name and force flag will go thru \(assuming POps knows what they are doing\)
> 
> ![](<url>
> Same distribution will be updated with new file name instead of creating new distribution
> 
> ![](<url>

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2546 · comment 390123322 · PR 5859 · 2023-04-27

> Reprocess already-processed distribution with different file name and force flag will go thru \(assuming POps knows what they are doing\)
> 
> ![](<url>
> Same distribution will be updated with new file name instead of creating new distribution
> 
> ![](<url>
> ‌

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

## A3-0727 — services.list: Not sure but definitely didn’t work in d34 :sweat_drops:

**Source stance:** reported-verification

**Context:**

> kubernetes/services.list; PR: [INV-1361] feat(investment)(redemption)(rebalance)(transaction): Consume order level assumed settlement msg and update trade request + transaction accordingly

**Source-preserving request, proposal, or question:**

> Not sure but definitely didn’t work in d34 :sweat_drops:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2579 · comment 384589010 · PR 5651 · 2023-04-05

Source path: `kubernetes/services.list`

**Evidence:** anon-2.jsonl:2579 · comment 384589010 · PR 5651 · 2023-04-05

Source path: `kubernetes/services.list`

**Explicit source context (hunk):**

> -advisory charge transaction
> \ No newline at end of file
> +advisory charge communication compliance dividend goal investment projection rebalance redemption referral trading transaction
> \ No newline at end of file

## A3-0734 — SellOrderGeneratorTest.scala: This is the new test. The rest is just moving the code to companion object

**Source stance:** explanation

**Context:**

> trading-impl/src/test/scala/com/endowus/silver/trading/imp/entities/plan/utils/SellOrderGeneratorTest.scala; PR: [INV-1269] feat(trading): Buffer pending amount-based sell units when calculating sell orders

**Source-preserving request, proposal, or question:**

> This is the new test. The rest is just moving the code to companion object

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2586 · comment 378817040 · PR 5516 · 2023-03-16

Source path: `trading-impl/src/test/scala/com/endowus/silver/trading/imp/entities/plan/utils/SellOrderGeneratorTest.scala`

**Evidence:** anon-2.jsonl:2586 · comment 378817040 · PR 5516 · 2023-03-16

Source path: `trading-impl/src/test/scala/com/endowus/silver/trading/imp/entities/plan/utils/SellOrderGeneratorTest.scala`

**Explicit source context (hunk):**

> +      orders.find(_.instrumentId == "HYG").get.orderUnits.get shouldBe 2.5
> +    }
> +
> +    "generate unit-based sell orders with pending amount-based sell orders" in {
> +      val pendingSellTradeId = UUID.randomUUID()
> +      val pendingSellSpyOrder = createPendingAmountBasedSellOrder(pendingSellTradeId, "SPY", orderUnits = 8)
> +      val pendingSellHygOrder = createPendingAmountBasedSellOrder(pendingSellTradeId, "HYG", orderUnits = 0.005)

## A3-0803 — SftpMetadataChecker.scala: Why don’t we just diff always, in case the count is same but ids mismatch?

**Source stance:** open-question

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala; PR: Feat/EN-870 sg auto generate report meta data

**Source-preserving request, proposal, or question:**

> Why don’t we just diff always, in case the count is same but ids mismatch?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2658 · comment 379043264 · PR 5350 · 2023-03-17

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala`

**Evidence:** anon-2.jsonl:2658 · comment 379043264 · PR 5350 · 2023-03-17

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala`

**Explicit source context (hunk):**

> +          (maybeCustomerId, documentId) <- documentService
> +            .getDocumentInfoById(documentId)
> +            .invoke()
> +            .map(document => (document.documentInfo.customerId, documentId))
> +          info <- maybeCustomerId.fold {
> +            logger.info(s"maybeCustomerId: [$maybeCustomerId], status: None, documentId: [$documentId] ")
> +            Future.successful(maybeCustomerId, Option.empty[CustomerStatus], documentId)

## A3-0805 — SftpMetadataChecker.scala: it’s good to separate these 2 list * One is missing in metadata file but pdf exists → less critical, can be checked if customer is deactivated etc * O

**Source stance:** suggestion

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala; PR: Feat/EN-870 sg auto generate report meta data

**Source-preserving request, proposal, or question:**

> I think it’s good to separate these 2 list
> 
> * One is missing in metadata file but pdf exists → less critical, can be checked if customer is deactivated etc
> * One is in metadata but pdf missing → more critical, meaning the upload task was missed during generation… but as long as statement is generated, we can easily re-upload

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2660 · comment 379043789 · PR 5350 · 2023-03-17

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala`

> I think it’s good to separate these 2 list
> 
> * One is missing in metadata file but pdf exists → less critical, can be checked if customer is deactivated etc
> * One is in metadata but pdf missing → more critical, meaning the upload task was missed during generation… but as long as statement is generated, we can easily re-upload
> 
> ‌

**Evidence:** anon-2.jsonl:2660 · comment 379043789 · PR 5350 · 2023-03-17

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala`

**Explicit source context (hunk):**

> +      }
> +    }
> +
> +    val documentIdsInSftpButNotInCsv = (pdfFileNames.toSet diff documentIdsInCsvFile.toSet).map(removeFileExtensionName).map(UUID.fromString)
> +    val documentIdsInCsvButNotInSftp = (documentIdsInCsvFile.toSet diff pdfFileNames.toSet).map(removeFileExtensionName).map(UUID.fromString)
> +
> +    logger.info(s"documentIdsInSftpButNotInCsv: [$documentIdsInSftpButNotInCsv]")

## A3-0834 — : can we put unit test for serdes to make sure the default logic is doing what we expect it to do? Especially if someone explicitly set the field to nul

**Source stance:** requested-change

**Context:**

> None; PR: fix(advisory): INV-1247 Make dividend distributionPreference mandatory with defaults

**Source-preserving request, proposal, or question:**

> can we put unit test for serdes to make sure the default logic is doing what we expect it to do? Especially if someone explicitly set the field to null?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2692 · comment 374519922 · PR 5393 · 2023-03-03

## A3-0835 — : the test, if any, is more like a feature discovery of play json serdes haha. I guess so far we didn’t think about this as we expect no one would send 

**Source stance:** explanation

**Context:**

> None; PR: fix(advisory): INV-1247 Make dividend distributionPreference mandatory with defaults

**Source-preserving request, proposal, or question:**

> Yeah the test, if any, is more like a feature discovery of play json serdes haha. I guess so far we didn’t think about this as we expect no one would send null to an optional field :grimacing:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2693 · comment 374523776 · PR 5393 · 2023-03-03

## A3-0885 — : You’ll need services.list… I suppose you’ll need to test this in some of the dynamic env too

**Source stance:** requested-change

**Context:**

> None; PR: Feat/INV-913 fx rates projection

**Source-preserving request, proposal, or question:**

> You’ll need services.list… I suppose you’ll need to test this in some of the dynamic env too

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2744 · comment 354582999 · PR 4915 · 2022-12-19

## A3-0921 — CraManagerTest.scala: assert `vcStateChangeDailyTriggerTopicProducerDirect` not called?

**Source stance:** suggestion

**Context:**

> advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/hk/CraManagerTest.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Maybe assert `vcStateChangeDailyTriggerTopicProducerDirect` not called?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2780 · comment 367136755 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/hk/CraManagerTest.scala`

**Evidence:** anon-2.jsonl:2780 · comment 367136755 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/hk/CraManagerTest.scala`

**Explicit source context (hunk):**

> +        when(customerProjectionDataJdbcRepository.findNonVCWithMaybeAdvisoryProfile(currentDate(ZoneHongKong).minusYears(65)))
> +          .thenReturn(Source(List((customerProjectionData, Some(profileDataUpdated)))))
> +
> +        service.publishDailyCustomerVCTriggerMsg(Some(currentDate(ZoneHongKong))).map(res => {
> +          verify(vcStateChangeDailyTriggerTopicProducerDirect, times(0)).publish(any())
> +          res shouldBe akka.Done
> +        })

## A3-0973 — TransactionJdbcRepositoryV2Test.scala: We typically keep these in companion object. You can extend it with `TestData` which provides some handy helpers to randomize data. Essentially, we ju

**Source stance:** suggestion

**Context:**

> transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2Test.scala; PR: [EN-674] feat(transaction) create an api to get transactions for a customer id with goal id and statuses filter

**Source-preserving request, proposal, or question:**

> We typically keep these in companion object. You can extend it with `TestData` which provides some handy helpers to randomize data.
> 
> Essentially, we just want to keep the test uncluttered :thumbsup:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2833 · comment 357769793 · PR 5028 · 2023-01-05

Source path: `transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2Test.scala`

**Evidence:** anon-2.jsonl:2833 · comment 357769793 · PR 5028 · 2023-01-05

Source path: `transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2Test.scala`

**Explicit source context (hunk):**

> +    "return filtered when using findAll" in withDb { db =>
> +      val repository = new TransactionJdbcRepositoryV2(db, new SingaporeDateTimeProvider)
> +
> +      for {
> +        _ <- repository.createTableIfNotExists
> +        _ <- repository.upsert(TransactionJdbcRepositoryV2Test.tx1)
> +        _ <- repository.upsert(TransactionJdbcRepositoryV2Test.tx2)

## A3-0974 — TransactionJdbcRepositoryV2Test.scala: Good idea to truncate the table at the end. Save yourself some head scratching when you add the next test

**Source stance:** suggestion

**Context:**

> transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2Test.scala; PR: [EN-674] feat(transaction) create an api to get transactions for a customer id with goal id and statuses filter

**Source-preserving request, proposal, or question:**

> Good idea to truncate the table at the end. Save yourself some head scratching when you add the next test

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2834 · comment 357770225 · PR 5028 · 2023-01-05

Source path: `transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2Test.scala`

**Evidence:** anon-2.jsonl:2834 · comment 357770225 · PR 5028 · 2023-01-05

Source path: `transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2Test.scala`

**Explicit source context (hunk):**

> +            )
> +          )
> +        _ <- db.run(truncateTable(TransactionTableV2.tableName))
> +      } yield {
> +        result1.size shouldBe 1
> +        result2.size shouldBe 1
> +        result3.size shouldBe 0

## A3-0993 — : can we also make sure the subscriber for new model doesn’t have the same bug? Then we can add services.list and release :thumbsup:

**Source stance:** requested-change

**Context:**

> None; PR: INV-654 Fix TradeTopicSubscriber.convertToSellOrder for assumedPrice

**Source-preserving request, proposal, or question:**

> can we also make sure the subscriber for new model doesn’t have the same bug? Then we can add services.list and release :thumbsup:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Related source row2854 corrects the affected service to redemption svc, not transaction svc. Keep this target correction when checking the new-model subscriber and services.list release.

**Evidence:** anon-2.jsonl:2853 · comment 348070050 · PR 4765 · 2022-11-23

> can we also make sure the subscriber for new model doesn’t have the same bug? Then we can add services.list and release :thumbsup: 
> 
> ‌

**Evidence:** anon-2.jsonl:2854 · comment 348072799 · PR 4765 · 2022-11-23

> Ah yeah my bad. It’s redemption svc, not transaction svc :pray: 

## A3-1002 — StateUpdatedSpec.scala: This will be in UTC. Depending on when the test runs, it might be flaky

**Source stance:** observed-defect

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/stateUpdated/StateUpdatedSpec.scala; PR: Feat/INV-891 cancel investment pi to retail

**Concern stated in the source:** Depending on when the test runs, it might be flaky

**Source-preserving request, proposal, or question:**

> This will be in UTC. Depending on when the test runs, it might be flaky

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2863 · comment 353199101 · PR 4867 · 2022-12-13

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/stateUpdated/StateUpdatedSpec.scala`

**Evidence:** anon-2.jsonl:2863 · comment 353199101 · PR 4867 · 2022-12-13

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/stateUpdated/StateUpdatedSpec.scala`

**Explicit source context (hunk):**

> +        planId = planId1,
> +        investmentRequestId = investmentRequestId,
> +        status = PENDING_SUBMISSION,
> +        lastUpdated = StateUpdatedSpec.t3.toInstant
> +      )
> +
> +      And("Calls cancel investment API")

## A3-1012 — Error-contract tests: missing CRA, concurrent invest retry, instrument-down propagation

**Source stance:** reported-verification

**Context:**

> None; PR: Extract common Lagom exception helper

**Source-preserving request, proposal, or question:**

> Tested in `advisory`: query CRA with invalid customerId returns expected error json, but no error logs
> 
> ```
> GET <url>
> {
>     "error_code": "CUSTOMER_NOT_FOUND",
>     "name": "com.endowus.silver.advisory.api.exceptions.AdvisorySvcException",
>     "detail": "Customer advisory profile not found"
> }
> ```
> 
> 
> 
> Tested in `investment` and `compliance`: submit concurrent invest-once
> 
> * `investment` is able to retry automatically when `compliance` returns concurrent modification error
> * no error logs on `compliance` side
> 
> ![](<url>
> Tested in `investment` and `compliance`: invest-once when `instrument` svc is down
> 
> * `investment` is able to check exception type from `compliance` and abort the request
> * error is logged on `compliance` side as TransportException due to uncaught exception
> * error is logged on `investment` side as wrapped InvestmentSvcException and propagate accordingly to caller
> 
> ```
> {
>     "error_code":"COMPLIANCE_SERVICE_ERROR",
>     "name":"com.endowus.silver.investment.api.exceptions.InvestmentSvcException",
>     "detail":"Compliance check for one-time investment for Customer[] InvestmentRequestId[] errored due to compliance service exception"
> }
> ```
> 
> ![](<url>

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Preserve invalid CRA CUSTOMER_NOT_FOUND/no-error-log; concurrent invest compliance retry/no-compliance-log; instrument-down abort with TransportException log in compliance and wrapped InvestmentSvcException log in investment.

**Evidence:** anon-2.jsonl:2874 · comment 353206494 · PR 4896 · 2022-12-13

> Tested in `advisory`: query CRA with invalid customerId returns expected error json, but no error logs
> 
> ```
> GET <url>
> {
>     "error_code": "CUSTOMER_NOT_FOUND",
>     "name": "com.endowus.silver.advisory.api.exceptions.AdvisorySvcException",
>     "detail": "Customer advisory profile not found"
> }
> ```
> 
> ‌
> 
> Tested in `investment` and `compliance`: submit concurrent invest-once
> 
> * `investment` is able to retry automatically when `compliance` returns concurrent modification error
> * no error logs on `compliance` side
> 
> ![](<url>
> Tested in `investment` and `compliance`: invest-once when `instrument` svc is down
> 
> * `investment` is able to check exception type from `compliance` and abort the request
> * error is logged on `compliance` side as TransportException due to uncaught exception
> * error is logged on `investment` side as wrapped InvestmentSvcException and propagate accordingly to caller
> 
> ```
> {
>     "error_code":"COMPLIANCE_SERVICE_ERROR",
>     "name":"com.endowus.silver.investment.api.exceptions.InvestmentSvcException",
>     "detail":"Compliance check for one-time investment for Customer[

**Evidence:** anon-2.jsonl:2874 · comment 353206494 · PR 4896 · 2022-12-13

> ] InvestmentRequestId[

**Evidence:** anon-2.jsonl:2874 · comment 353206494 · PR 4896 · 2022-12-13

> ] errored due to compliance service exception"
> }
> ```
> 
> ![](<url>
> ‌

## A3-1023 — RedeemOnceEdgeLogic.scala: Can we add test for these cases? * unit-based request should use the provided units as is * amount-based request should calculate and call the BE API 

**Source stance:** requested-change

**Context:**

> redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/edge/RedeemOnceEdgeLogic.scala; PR: EN-569 Calculate units from amount for redemption request

**Source-preserving request, proposal, or question:**

> Can we add test for these cases?
> 
> * unit-based request should use the provided units as is
> * amount-based request should calculate and call the BE API as unit-based

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2887 · comment 351260385 · PR 4851 · 2022-12-06

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/edge/RedeemOnceEdgeLogic.scala`

> Can we add test for these cases?
> 
> * unit-based request should use the provided units as is
> * amount-based request should calculate and call the BE API as unit-based
> 
> ‌

**Evidence:** anon-2.jsonl:2887 · comment 351260385 · PR 4851 · 2022-12-06

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/edge/RedeemOnceEdgeLogic.scala`

**Explicit source context (hunk):**

> +      calculateRedemptionUnitsResponse <- redemptionServiceLogic
> +        .calculateRedemptionUnits(
> +          CalculateRedemptionUnitsRequest(planId = plan.planId, requestedAmount = request.requestedAmount, isFullRedemption = request.isFullRedemption)
> +        )
> +        .map { r =>
> +          if (r.units.isEmpty)

## A3-1054 — TransactionEntityTest.scala: Can just new `SingaporeDateTimeProvider` I think.. we don’t need to control time in this test right?

**Source stance:** suggestion

**Context:**

> transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/entities/TransactionEntityTest.scala; PR: INV-869 fix(transaction): add requestedAmount to cancelling and cancel status

**Source-preserving request, proposal, or question:**

> Can just new `SingaporeDateTimeProvider` I think.. we don’t need to control time in this test right?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2918 · comment 350434482 · PR 4824 · 2022-12-02

Source path: `transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/entities/TransactionEntityTest.scala`

**Evidence:** anon-2.jsonl:2918 · comment 350434482 · PR 4824 · 2022-12-02

Source path: `transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/entities/TransactionEntityTest.scala`

**Explicit source context (hunk):**

> override def serializationRegistry: JsonSerializerRegistry = TransactionJsonSerializerRegistry
>  
> +  val dtp: SingaporeDateTimeProvider = mock[SingaporeDateTimeProvider]
> +
>    override def entityToTest: Any => PersistentEntity {
>      type Command = TransactionCmd

## A3-1055 — TransactionEntityTest.scala: ok but this is as good as just use the real provider right? :stuck_out_tongue: ``` val date = ZonedDateTime.now() when(dtp.now).thenReturn(date) ```

**Source stance:** open-question

**Context:**

> transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/entities/TransactionEntityTest.scala; PR: INV-869 fix(transaction): add requestedAmount to cancelling and cancel status

**Source-preserving request, proposal, or question:**

> ok but this is as good as just use the real provider right? :stuck_out_tongue: 
> 
> ```
>         val date = ZonedDateTime.now()
>         when(dtp.now).thenReturn(date)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2919 · comment 350435308 · PR 4824 · 2022-12-02

Source path: `transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/entities/TransactionEntityTest.scala`

> ok but this is as good as just use the real provider right? :stuck_out_tongue: 
> 
> ```
>         val date = ZonedDateTime.now()
>         when(dtp.now).thenReturn(date)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2919 · comment 350435308 · PR 4824 · 2022-12-02

Source path: `transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/entities/TransactionEntityTest.scala`

**Explicit source context (hunk):**

> override def serializationRegistry: JsonSerializerRegistry = TransactionJsonSerializerRegistry
>  
> +  val dtp: SingaporeDateTimeProvider = mock[SingaporeDateTimeProvider]
> +
>    override def entityToTest: Any => PersistentEntity {
>      type Command = TransactionCmd

## A3-1167 — ConcentrationRiskValidator.scala: Yeah, either works I guess. We didn’t throw here, so we still can test the CR validation logic without locking down earmark prematurely.

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala; PR: [INV-715] feat(compliance): Update warning/ack logic for Save goal / Upsert recurring schedule scenarios

**Source-preserving request, proposal, or question:**

> Yeah, either works I guess. We didn’t throw here, so we still can test the CR validation logic without locking down earmark prematurely.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3040 · comment 342246088 · PR 4575 · 2022-11-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala`

**Evidence:** anon-2.jsonl:3040 · comment 342246088 · PR 4575 · 2022-11-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala`

**Explicit source context (hunk):**

> +    }
> +  }
> +
> +  private def `applyEarmarkFn / forGoalModification`(): ApplyEarmarkFn = _ => Future.successful(Done)
> +  private def `applyEarmarkFn / forGoalTransfer`(): ApplyEarmarkFn = _ => Future.successful(Done)
>  }

## A3-1212 — RecurringInvestmentRestrictionSpec.scala: Can we add a test case that fails CR for this flow?

**Source stance:** requested-change

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/RecurringInvestmentRestrictionSpec.scala; PR: Feat/INV-560 recurring and ack persistence

**Source-preserving request, proposal, or question:**

> Can we add a test case that fails CR for this flow?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3087 · comment 338186923 · PR 4477 · 2022-10-17

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/RecurringInvestmentRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:3087 · comment 338186923 · PR 4477 · 2022-10-17

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/RecurringInvestmentRestrictionSpec.scala`

**Explicit source context (hunk):**

> +
> +            Then("request is permitted")
> +            responseFut.map { response =>
> +              response shouldBe Permitted
> +            }
> +          }
> +

## A3-1216 — CPF investor mismatch rejected at goal admission before compliance after fix

**Source stance:** reported-verification

**Context:**

> None; PR: fix(goal): Validate tradingAccount against portfolio's allowedInvestorTypes during goal modification

**Concern stated in the source:** Before fix: request goes thru \(it failed compliance check because I pick unlucky customer\)

**Source-preserving request, proposal, or question:**

> Before fix: request goes thru \(it failed compliance check because I pick unlucky customer\)
> 
> ```json
> {
>     "error_code": "COMPLIANCE_RESTRICTION",
>     "name": "com.endowus.silver.goal.api.exceptions.GoalSvcException",
>     "detail": "compliance check failed for modify goal  and plan  rebalanceId  for customer "
> }
> ```
> 
> After fix: rejected earlier
> 
> ```json
> {
>     "error_code": "INVALID_GOAL_CREATION_ATTEMPT",
>     "name": "com.endowus.silver.goal.api.exceptions.GoalSvcException",
>     "detail": "Customer with trading account type [SINGAPORE_CPF_OA_ACCOUNT] cannot be assigned to the plan with portfolio [] with name [Fund Smart portfolio for  for goal FS SP500 1 (seed )] - portfolio's allowed investor types [SINGAPORE_SRS_INVESTOR,SINGAPORE_CASH_RETAIL_INVESTOR,SINGAPORE_CASH_ACCREDITED_INVESTOR] does not contain [SINGAPORE_CPF_OA_INVESTOR]"
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- CPF portfolio-investor mismatch before flowed to compliance, after rejected earlier INVALID_GOAL_CREATION_ATTEMPT; literal customer/goal/portfolio IDs omitted.

**Evidence:** anon-2.jsonl:3091 · comment 338802616 · PR 4524 · 2022-10-19

> Before fix: request goes thru \(it failed compliance check because I pick unlucky customer\)
> 
> ```json
> {
>     "error_code": "COMPLIANCE_RESTRICTION",
>     "name": "com.endowus.silver.goal.api.exceptions.GoalSvcException",
>     "detail": "compliance check failed for modify goal

**Evidence:** anon-2.jsonl:3091 · comment 338802616 · PR 4524 · 2022-10-19

> and plan

**Evidence:** anon-2.jsonl:3091 · comment 338802616 · PR 4524 · 2022-10-19

> rebalanceId

**Evidence:** anon-2.jsonl:3091 · comment 338802616 · PR 4524 · 2022-10-19

> for customer

**Evidence:** anon-2.jsonl:3091 · comment 338802616 · PR 4524 · 2022-10-19

> "
> }
> ```
> 
> After fix: rejected earlier
> 
> ```json
> {
>     "error_code": "INVALID_GOAL_CREATION_ATTEMPT",
>     "name": "com.endowus.silver.goal.api.exceptions.GoalSvcException",
>     "detail": "Customer with trading account type [SINGAPORE_CPF_OA_ACCOUNT] cannot be assigned to the plan with portfolio [

**Evidence:** anon-2.jsonl:3091 · comment 338802616 · PR 4524 · 2022-10-19

> ] with name [Fund Smart portfolio for

**Evidence:** anon-2.jsonl:3091 · comment 338802616 · PR 4524 · 2022-10-19

> for goal FS SP500 1 (seed

**Evidence:** anon-2.jsonl:3091 · comment 338802616 · PR 4524 · 2022-10-19

> )] - portfolio's allowed investor types [SINGAPORE_SRS_INVESTOR,SINGAPORE_CASH_RETAIL_INVESTOR,SINGAPORE_CASH_ACCREDITED_INVESTOR] does not contain [SINGAPORE_CPF_OA_INVESTOR]"
> }
> ```
> 
> ‌

## A3-1228 — LocalConfig.scala: Added for testing in d34 only. Will remove after region split

**Source stance:** explanation

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/config/LocalConfig.scala; PR: [INV-638] feat(marketdata): Support MAS FxRate for HKD

**Source-preserving request, proposal, or question:**

> Added for testing in d34 only. Will remove after region split

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:3103 · comment 337782485 · PR 4488 · 2022-10-14

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/config/LocalConfig.scala`

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

## A3-1245 — GoalCreationRestrictionSpec.scala: The GWT blocks are free text, and needs to be updated manually if anything is change - they are bounded to glue code, like Cucumber

**Source stance:** explanation

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalCreationRestrictionSpec.scala; PR: Feat/INV-560 cra2 complex ack

**Source-preserving request, proposal, or question:**

> The GWT blocks are free text, and needs to be updated manually if anything is change - they are bounded to glue code, like Cucumber

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3125 · comment 336814990 · PR 4449 · 2022-10-11

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalCreationRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:3125 · comment 336814990 · PR 4449 · 2022-10-11

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalCreationRestrictionSpec.scala`

**Explicit source context (hunk):**

> )
>  
> -          Then("request is permitted")
> +          Then("request is blocked")
>            responseFut.map { response =>
>              response shouldBe Blocked(Set(CraExpired))
>            }

## A3-1257 — ReleaseEarmarkSpec.scala: Should we add another assertion checking the earmark state? Otherwise, we would always get a Done as result - whether the earmark is found or not

**Source stance:** open-question

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala; PR: Feat/INV-551 release earmark

**Concern stated in the source:** Otherwise, we would always get a Done as result - whether the earmark is found or not

**Source-preserving request, proposal, or question:**

> Should we add another assertion checking the earmark state? Otherwise, we would always get a Done as result - whether the earmark is found or not

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3138 · comment 335026059 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala`

**Evidence:** anon-2.jsonl:3138 · comment 335026059 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala`

**Explicit source context (hunk):**

> +
> +          Then("Process is successful")
> +          responseFut.map { response =>
> +            response shouldBe Done
> +          }
> +        }
> +

## A3-1258 — Earmark-release e2e: simulate failure, release, simulate success

**Source stance:** suggestion

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala; PR: Feat/INV-551 release earmark

**Concern stated in the source:** * setup state so that CR would fail
* call simulate and assert rejection
* call release earmark and assert success
* call simulate again and assert success

Otherwise I feel this test a bit useless by itself…

**Source-preserving request, proposal, or question:**

> Right ok, then maybe a better e2e is to do:
> 
> * setup state so that CR would fail
> * call simulate and assert rejection
> * call release earmark and assert success
> * call simulate again and assert success
> 
> 
> 
> Otherwise I feel this test a bit useless by itself…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3139 · comment 335026962 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala`

> Right ok, then maybe a better e2e is to do:
> 
> * setup state so that CR would fail
> * call simulate and assert rejection
> * call release earmark and assert success
> * call simulate again and assert success
> 
> ‌
> 
> Otherwise I feel this test a bit useless by itself…
> 
> ‌

**Evidence:** anon-2.jsonl:3139 · comment 335026962 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala`

**Explicit source context (hunk):**

> +
> +          Then("Process is successful")
> +          responseFut.map { response =>
> +            response shouldBe Done
> +          }
> +        }
> +

## A3-1259 — ReleaseEarmarkSpec.scala: it’s up to us really. The e2e test is really to do scenario testing, so I don’t think it’s too big - the test should run fairly fast anyway.

**Source stance:** explanation

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala; PR: Feat/INV-551 release earmark

**Source-preserving request, proposal, or question:**

> Yeah it’s up to us really. The e2e test is really to do scenario testing, so I don’t think it’s too big - the test should run fairly fast anyway.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3140 · comment 335029525 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala`

**Evidence:** anon-2.jsonl:3140 · comment 335029525 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala`

**Explicit source context (hunk):**

> +
> +          Then("Process is successful")
> +          responseFut.map { response =>
> +            response shouldBe Done
> +          }
> +        }
> +

## A3-1276 — Json.format still requires acknowledgements array; WithDefaultValues is discouraged here

**Source stance:** explanation

**Context:**

> compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionRequest.scala; PR: Feat/INV-560 acknowledegement API Contract

**Source-preserving request, proposal, or question:**

> If called via REST, still need to specify `acknowledgements: []` in the json, unless we use `Json.using[Json.WithDefaultValues].format` instead of just `Json.format`…. which is another thing I’d recommend avoid…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3157 · comment 335607537 · PR 4423 · 2022-10-06

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionRequest.scala`

**Evidence:** anon-2.jsonl:3157 · comment 335607537 · PR 4423 · 2022-10-06

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionRequest.scala`

**Explicit source context (hunk):**

> initialInvestmentAmount: Option[BigDecimal],
> -  recurringInvestmentAmount: Option[BigDecimal]
> +  recurringInvestmentAmount: Option[BigDecimal],
> +  acknowledgements: Set[TradingAcknowledgementDto]
>  ) extends GoalCreationIntention
>      with TradingRestrictionRequest

## A3-1308 — CustomerTradingEarmarkEntityTest.scala: I think test is a bit clearer if we do this step 1 as state setup instead. Can use `withCustomizedEntitySetup`

**Source stance:** suggestion

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/cr/CustomerTradingEarmarkEntityTest.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Nit: I think test is a bit clearer if we do this step 1 as state setup instead. Can use `withCustomizedEntitySetup`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3190 · comment 334017714 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/cr/CustomerTradingEarmarkEntityTest.scala`

**Evidence:** anon-2.jsonl:3190 · comment 334017714 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/cr/CustomerTradingEarmarkEntityTest.scala`

**Explicit source context (hunk):**

> +      driver.initialize(snapshotState = Some(
> +        initialState.copy(buyEarmarks = initialState.buyEarmarks :+ BuyEarmark(
> +          id = InitialInvestmentEarmarkId(
> +            goalId = goalId1,
> +            planId = planId1
> +          ),
> +          amount = 1000

## A3-1310 — GoalCreationRestrictionSpec.scala: Just curious why we need this setup if customer is VC? I know skipping setup because we know it won’t be checked is a little white-box… but I purposel

**Source stance:** open-question

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalCreationRestrictionSpec.scala; PR: Feat/INV-486 add goal earmark

**Concern stated in the source:** I know skipping setup because we know it won’t be checked is a little white-box… but I purposely skip because the test was already too long :see_no_evil:

**Source-preserving request, proposal, or question:**

> Just curious why we need this setup if customer is VC? I know skipping setup because we know it won’t be checked is a little white-box… but I purposely skip because the test was already too long :see_no_evil:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3192 · comment 334018000 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalCreationRestrictionSpec.scala`

## A3-1311 — GoalCreationRestrictionSpec.scala: The comments don’t seem to fit the actual setup? 0.1 of TLNW is not “large”?

**Source stance:** open-question

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalCreationRestrictionSpec.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> The comments don’t seem to fit the actual setup? 0.1 of TLNW is not “large”?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:3193 · comment 334018156 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingRestriction/GoalCreationRestrictionSpec.scala`

## A3-1344 — TransactionTypes.scala: Can we add a simple json serialization test to ensure that serdes would work? E.g. create an instance of `DepositTransactionDto` and see if the json m

**Source stance:** requested-change

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: INV-235 feat: Transaction types modelling

**Source-preserving request, proposal, or question:**

> Can we add a simple json serialization test to ensure that serdes would work?
> 
> E.g. create an instance of `DepositTransactionDto` and see if the json matches, and vice versa

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3229 · comment 331137308 · PR 4256 · 2022-09-16

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:3229 · comment 331137308 · PR 4256 · 2022-09-16

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> +
> +    private implicit val depositTransaction: Format[DepositTransactionDto] =  DepositTransactionDto.format
> +
> +    implicit val format: Format[TransactionDto] = Json.format[TransactionDto]
> +  }
> +
> +  def toTransactionDtoV1(transactionV2: TransactionDto): models.TransactionDto = {

## A3-1383 — application.conf: this was to test the config update only that should only change the last layer. I’ll remove the circleci config.yml hacks too

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/resources/application.conf; PR: docker layered image

**Source-preserving request, proposal, or question:**

> Yes this was to test the config update only that should only change the last layer. I’ll remove the circleci config.yml hacks too

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3275 · comment 317457450 · PR 3862 · 2022-07-20

Source path: `advisory-impl/src/main/resources/application.conf`

## A3-1384 — d10 Docker layer/label/env/build-info smoke verification

**Source stance:** reported-verification

**Context:**

> None; PR: docker layered image

**Source-preserving request, proposal, or question:**

> Built and deployed `advisory` to d10. Retained exact source excerpts for deployment labels, Docker label lookups, the build-info endpoint/JSON keys, and the printed relative layer sequence. Registry/project/pod identifiers and unrelated older base-image history are omitted.
> 
> ```
> appGitBranch=d10-docker-layered-image,appGitHash=74d0565,appNameVersion=advisory-11-0-1,appVersion=11.0.1
> ```
> 
> ```
> .Config.Labels.GIT_BRANCH_NAME  }}'
> d10/docker-layered-image
> ```
> 
> ```
> .Config.Labels.SHORT_GIT_HASH  }}'
> 74d0565
> ```
> 
> ```
> localhost:10002/config/info/build
> ```
> 
> ```
> {"git-branch-name":"d10/docker-layered-image","short-git-hash":"74d0565"}
> ```
> 
> ```
> /bin/sh -c #(nop)  CMD []                       0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  ENTRYPOINT ["/opt/docker/…   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  USER [1001:0]                0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  ENV GIT_BRANCH_NAME=d10/d…   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  ENV SHORT_GIT_HASH=74d0565   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  LABEL GIT_BRANCH_NAME=d10…   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  LABEL SHORT_GIT_HASH=74d0…   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop) COPY --chown=endowus:rootd…   8.64MB
> <missing>      20 hours ago     /bin/sh -c #(nop) COPY --chown=endowus:rootd…   155MB
> <missing>      20 hours ago     /bin/sh -c #(nop) COPY --chown=endowus:rootd…   5.75MB
> <missing>      20 hours ago     /bin/sh -c #(nop) WORKDIR /opt/docker           0B
> <missing>      20 hours ago     /bin/sh -c id -u endowus 1>/dev/null 2>&1 ||…   2.82kB
> <missing>      2 days ago       /bin/sh -c #(nop)  USER [root]                  0B
> <missing>      2 days ago       /bin/sh -c microdnf update -y && microdnf cl…   156MB
> ```
> 
> ```
> Smoke-tested advisory endpoints in d10, and they’re working fine.
> ```

**Conditions and limits:**

- Reported d10 smoke verification retains Docker label keys GIT_BRANCH_NAME/SHORT_GIT_HASH, corresponding ENV/LABEL history entries, /config/info/build and git-branch-name/short-git-hash JSON keys. The history excerpt preserves the printed CMD/ENTRYPOINT/USER, app ENV/LABEL, three COPY layers, WORKDIR/user-creation and microdnf-update sequence. It does not establish performance improvement.

**Evidence:** anon-2.jsonl:3276 · comment 317551731 · PR 3862 · 2022-07-20

> appGitBranch=d10-docker-layered-image,appGitHash=74d0565,appNameVersion=advisory-11-0-1,appVersion=11.0.1

**Evidence:** anon-2.jsonl:3276 · comment 317551731 · PR 3862 · 2022-07-20

> .Config.Labels.GIT_BRANCH_NAME  }}'
> d10/docker-layered-image

**Evidence:** anon-2.jsonl:3276 · comment 317551731 · PR 3862 · 2022-07-20

> .Config.Labels.SHORT_GIT_HASH  }}'
> 74d0565

**Evidence:** anon-2.jsonl:3276 · comment 317551731 · PR 3862 · 2022-07-20

> localhost:10002/config/info/build

**Evidence:** anon-2.jsonl:3276 · comment 317551731 · PR 3862 · 2022-07-20

> {"git-branch-name":"d10/docker-layered-image","short-git-hash":"74d0565"}

**Evidence:** anon-2.jsonl:3276 · comment 317551731 · PR 3862 · 2022-07-20

> /bin/sh -c #(nop)  CMD []                       0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  ENTRYPOINT ["/opt/docker/…   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  USER [1001:0]                0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  ENV GIT_BRANCH_NAME=d10/d…   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  ENV SHORT_GIT_HASH=74d0565   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  LABEL GIT_BRANCH_NAME=d10…   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  LABEL SHORT_GIT_HASH=74d0…   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
> <missing>      27 minutes ago   /bin/sh -c #(nop) COPY --chown=endowus:rootd…   8.64MB
> <missing>      20 hours ago     /bin/sh -c #(nop) COPY --chown=endowus:rootd…   155MB
> <missing>      20 hours ago     /bin/sh -c #(nop) COPY --chown=endowus:rootd…   5.75MB
> <missing>      20 hours ago     /bin/sh -c #(nop) WORKDIR /opt/docker           0B
> <missing>      20 hours ago     /bin/sh -c id -u endowus 1>/dev/null 2>&1 ||…   2.82kB
> <missing>      2 days ago       /bin/sh -c #(nop)  USER [root]                  0B
> <missing>      2 days ago       /bin/sh -c microdnf update -y && microdnf cl…   156MB

**Evidence:** anon-2.jsonl:3276 · comment 317551731 · PR 3862 · 2022-07-20

> Smoke-tested advisory endpoints in d10, and they’re working fine.

## A3-1391 — EstimateAccessFeeGoalCreateBehaviourTest.scala: Can we add case for single fund \+ CMA goal? Similarly, single fund \+ CPF/SRS

**Source stance:** open-question

**Context:**

> charge-impl/src/test/scala/com/endowus/silver/charge/impl/goalcreate/EstimateAccessFeeGoalCreateBehaviourTest.scala; PR: IAO-56 FundSmart ProductLine Plan Upsert

**Source-preserving request, proposal, or question:**

> Can we add case for single fund \+ CMA goal? Similarly, single fund \+ CPF/SRS

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3284 · comment 319112715 · PR 3859 · 2022-07-27

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/goalcreate/EstimateAccessFeeGoalCreateBehaviourTest.scala`

**Evidence:** anon-2.jsonl:3284 · comment 319112715 · PR 3859 · 2022-07-27

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/goalcreate/EstimateAccessFeeGoalCreateBehaviourTest.scala`

**Explicit source context (hunk):**

> +        behaviour.fundSmartCreateRequest(baseRequest.copy(initialInvestmentAmount = 5000000), Unit).map { _ shouldBe 0.0025 }
> +      }
> +
> +      "return flat fee for a single instrument" in {
> +        behaviour.fundSmartCreateRequest(baseRequest.copy(targetWeights = Map("a" -> 1.0)), Unit).map { _ shouldBe 0.003 }
> +        behaviour.fundSmartCreateRequest(baseRequest.copy(targetWeights = Map("a" -> 1.0), initialInvestmentAmount = 100000), Unit).map { _ shouldBe 0.003 }
> +      }

## A3-1392 — EstimateFeeGoalModifyBehaviourTest.scala: Should we add another goal here, to ensure that the rank is checked across all cash plans?

**Source stance:** open-question

**Context:**

> charge-impl/src/test/scala/com/endowus/silver/charge/impl/productline/EstimateFeeGoalModifyBehaviourTest.scala; PR: IAO-56 FundSmart ProductLine Plan Upsert

**Source-preserving request, proposal, or question:**

> Should we add another goal here, to ensure that the rank is checked across all cash plans?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3285 · comment 319114339 · PR 3859 · 2022-07-27

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/productline/EstimateFeeGoalModifyBehaviourTest.scala`

**Evidence:** anon-2.jsonl:3285 · comment 319114339 · PR 3859 · 2022-07-27

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/productline/EstimateFeeGoalModifyBehaviourTest.scala`

**Explicit source context (hunk):**

> +      }
> +
> +      "return ranked fee 2 according to investment amount + pending investment" in {
> +        // 100k (from this goal) + 1k (from this goal's pending investment)
> +        setupTimeSeriesService_queryLatestPlanMarketValues(List(fundSmartCashPlanId), Map(fundSmartCashPlanId -> 100000), Map(fundSmartCashPlanId -> 1000))
> +        behaviour.fundSmartProduct(fundSmartProduct, InputWithGoal(request, fundSmartGoal)).map { _ shouldBe 0.005 }
> +      }

## R-3337 — safeRenewProjectionForCustomer is started with a value binding and not awaited

**Source stance:** explanation

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala; PR 3767: projection service kafka message throttling optimization

**Source-preserving request, proposal, or question:**

> Ah I missed this line in the processing logic - which does not wait for simulation call to return
> 
> ```
> _ = multiCcySimulationBatchManager.safeRenewProjectionForCustomer(msg.customerId) 
> ```
> 
> ‌
> 
> Ok this makes sense now :thumbsup: 

**Conditions and limits:**

- Read together: the throttle-removal suggestion is followed by discovery of an unawaited simulation call and a separate-topic proposal. It is not a settled rule to remove throttling. Source rows: anon-2.jsonl:3336, anon-2.jsonl:3337, anon-2.jsonl:3338.

**Evidence:** anon-2.jsonl:3337 · comment 313175068 · PR 3767 · 2022-07-01

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala`

## R-3341 — Yeah it works… I probably should have added the test cases… But I did test it with these, and it works.. No comments about looking odd though :grimacing: `

**Source stance:** reported-verification

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/models/enums.scala; PR 3694: Add SilverRegion in LocalConfig

**Source-preserving request, proposal, or question:**

> [incidental identifier omitted] Yeah it works… I probably should have added the test cases…
> 
> But I did test it with these, and it works.. No comments about looking odd though :grimacing: 
> 
> ```scala
> "test" in {
>   var localConfig = new LocalConfig(Configuration(ConfigFactory.parseString("")))
>   assertThrows[Exception] {
>     localConfig.getSilverRegion
>   }
> 
>   localConfig = new LocalConfig(Configuration(ConfigFactory.parseString("silver.region=blah")))
>   assertThrows[Exception] {
>     localConfig.getSilverRegion
>   }
> 
>   localConfig = new LocalConfig(Configuration(ConfigFactory.parseString("silver.region=SG")))
>   localConfig.getSilverRegion shouldBe SilverRegion.Sg
> 
>   localConfig = new LocalConfig(Configuration(ConfigFactory.parseString("silver.region=sG")))
>   localConfig.getSilverRegion shouldBe SilverRegion.Sg
> 
>   localConfig = new LocalConfig(Configuration(ConfigFactory.parseString("silver.region=HK")))
>   localConfig.getSilverRegion shouldBe SilverRegion.Hk
> 
>   localConfig = new LocalConfig(Configuration(ConfigFactory.parseString("silver.region=Hk")))
>   localConfig.getSilverRegion shouldBe SilverRegion.Hk
> }
> ```
> 
> ‌

**Conditions and limits:**

- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3341 · comment 311039625 · PR 3694 · 2022-06-22

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/enums.scala`

>  Yeah it works… I probably should have added the test cases…
> 
> But I did test it with these, and it works.. No comments about looking odd though :grimacing: 
> 
> ```scala
> "test" in {
>   var localConfig = new LocalConfig(Configuration(ConfigFactory.parseString("")))
>   assertThrows[Exception] {
>     localConfig.getSilverRegion
>   }
> 
>   localConfig = new LocalConfig(Configuration(ConfigFactory.parseString("silver.region=blah")))
>   assertThrows[Exception] {
>     localConfig.getSilverRegion
>   }
> 
>   localConfig = new LocalConfig(Configuration(ConfigFactory.parseString("silver.region=SG")))
>   localConfig.getSilverRegion shouldBe SilverRegion.Sg
> 
>   localConfig = new LocalConfig(Configuration(ConfigFactory.parseString("silver.region=sG")))
>   localConfig.getSilverRegion shouldBe SilverRegion.Sg
> 
>   localConfig = new LocalConfig(Configuration(ConfigFactory.parseString("silver.region=HK")))
>   localConfig.getSilverRegion shouldBe SilverRegion.Hk
> 
>   localConfig = new LocalConfig(Configuration(ConfigFactory.parseString("silver.region=Hk")))
>   localConfig.getSilverRegion shouldBe SilverRegion.Hk
> }
> ```
> 
> ‌

## R-3367 — Withdrawn EXPLAIN result for instrument_holdings_v1 SUM/MIN join

**Source stance:** reported-verification

**Context:**

> rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/db/jdbc/InstrumentHoldingDaoJdbc.scala; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> This query is translated into
> 
> ```sql
> SELECT
>     x2."plan_id", x2."instrument_id", x2."business_date", x2."ccy", x2."goal_id", x2."customer_id", x2."broker", x2."account_number", x2."market_value", x2."holding_units",
>     x3.x4
> FROM
>     (SELECT "plan_id" AS x5, SUM("market_value") AS x4
>      FROM "rebate"."instrument_holdings_v1"
>      WHERE ((((("broker" = 'UOBKH_SGD_CASH')
>                    AND ("instrument_id" = 'Vargan'))
>                   AND ("business_date" >= ?))
>                  AND ("business_date" <= ?))
>                 AND ("ccy" = 'SGD'))
>        AND ("market_value" >= 0)
>      GROUP BY "plan_id") x3,
> 
>     (SELECT "plan_id" AS x6, MIN("business_date") AS x7
>      FROM "rebate"."instrument_holdings_v1"
>      WHERE ((((("broker" = 'UOBKH_SGD_CASH')
>                    AND ("instrument_id" = 'Vargan'))
>                   AND ("business_date" >= ?))
>                  AND ("business_date" <= ?))
>                 AND ("ccy" = 'SGD'))
>        AND ("market_value" >= 0)
>      GROUP BY "plan_id") x8,
> 
>     "rebate"."instrument_holdings_v1" x2
> 
> WHERE
>     ((((((((x2."broker" = 'UOBKH_SGD_CASH')
>                AND (x2."instrument_id" = 'Vargan'))
>               AND (x2."business_date" >= ?))
>              AND (x2."business_date" <= ?))
>             AND (x2."ccy" = 'SGD'))
>            AND (x2."market_value" >= 0))
>           AND (x2."plan_id" = x8.x6))
>          AND (x2."business_date" = x8.x7))
>         AND (x2."plan_id" = x3.x5)
> ```
> 
> ‌
> 
> ~~Query analysis looks ok, with correct index being used~~
> 
> ```
> Hash Join  (cost=2325.98..3477.82 rows=1 width=134) (actual time=0.198..0.200 rows=0 loops=1)
>   Hash Cond: ((x2.plan_id = instrument_holdings_v1_1.plan_id) AND (x2.business_date = (min(instrument_holdings_v1_1.business_date))))
>   ->  Hash Join  (cost=1163.27..2315.09 rows=4 width=150) (never executed)
>         Hash Cond: (x2.plan_id = x3.x5)
>         ->  Index Scan using instrument_holdings_v1_instrument_id_broker_id_business_date_pl on instrument_holdings_v1 x2  (cost=0.56..1151.66 rows=278 width=102) (never executed)
>               Index Cond: (((instrument_id)::text = 'Vargan'::text) AND ((broker)::text = 'UOBKH_SGD_CASH'::text) AND (business_date >= '2021-10-01'::date) AND (business_date <= '2021-12-31'::date) AND ((ccy)::text = 'SGD'::text))
>               Filter: (market_value >= '0'::numeric)
>         ->  Hash  (cost=1159.26..1159.26 rows=276 width=48) (never executed)
>               ->  Subquery Scan on x3  (cost=1153.05..1159.26 rows=276 width=48) (never executed)
>                     ->  HashAggregate  (cost=1153.05..1156.50 rows=276 width=48) (never executed)
>                           Group Key: instrument_holdings_v1.plan_id
>                           ->  Index Scan using instrument_holdings_v1_instrument_id_broker_id_business_date_pl on instrument_holdings_v1  (cost=0.56..1151.66 rows=278 width=22) (never executed)
>                                 Index Cond: (((instrument_id)::text = 'Vargan'::text) AND ((broker)::text = 'UOBKH_SGD_CASH'::text) AND (business_date >= '2021-10-01'::date) AND (business_date <= '2021-12-31'::date) AND ((ccy)::text = 'SGD'::text))
>                                 Filter: (market_value >= '0'::numeric)
>   ->  Hash  (cost=1158.57..1158.57 rows=276 width=20) (actual time=0.149..0.149 rows=0 loops=1)
>         Buckets: 1024  Batches: 1  Memory Usage: 8kB
>         ->  HashAggregate  (cost=1153.05..1155.81 rows=276 width=20) (actual time=0.149..0.149 rows=0 loops=1)
>               Group Key: instrument_holdings_v1_1.plan_id
>               ->  Index Scan using instrument_holdings_v1_instrument_id_broker_id_business_date_pl on instrument_holdings_v1 instrument_holdings_v1_1  (cost=0.56..1151.66 rows=278 width=20) (actual time=0.146..0.146 rows=0 loops=1)
>                     Index Cond: (((instrument_id)::text = 'Vargan'::text) AND ((broker)::text = 'UOBKH_SGD_CASH'::text) AND (business_date >= '2021-10-01'::date) AND (business_date <= '2021-12-31'::date) AND ((ccy)::text = 'SGD'::text))
>                     Filter: (market_value >= '0'::numeric)
> Planning Time: 1.086 ms
> Execution Time: 0.399 ms
> ```
> 
> ‌
> 
> ^ Wrong query analysis. See below

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.

**Evidence:** anon-2.jsonl:3367 · comment 296868673 · PR 3438 · 2022-04-25

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/db/jdbc/InstrumentHoldingDaoJdbc.scala`

## R-3368 — Historical allocation/time comparison: in-memory versus DB holding aggregation at parallelism 4

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> Created [<url> data-inline-card='' } following method 1
> 
> ‌
> 
> Memory usage wise it’s working well. It uses more memory, since we are aggregating plan’s MV in logic \(instead of DB\), but we can control how much by adjusting the mapAsync parallelism.
> 
> With parallelism = 4:
> 
> |  | **from\_date** | **Memory allocation rate** | **Time taken** |
> | --- | --- | --- | --- |
> | Aggregate in memory | 2021-10-01 | ~100MB/s | ~155s |
> |  | 2021-01-01 | ~100MB/s | ~1,080s |
> | Aggregate in DB | 2021-10-01 | ~10MB/s | ~2s |
> |  | 2021-01-01 | ~10MB/s | ~15s |
> 
> ‌
> 
> In terms of time, it’s clear that using DB aggregate functions is faster, but I’m not sure if it can cope when we have more plans \(hence the suggestion to in method 1 to find the planIds only\)
> 
> In staging, with from\_date = 2021-01-01
> 
> * query with SUM \+ MIN aggregate function would take ~15s
> * query with DISTINCT plan would take ~6s, and afterwards, we would issue as many queries as plan count to get holdings per plan \(but these are all key fields, so should be fast\)
> 
> ‌

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.

**Evidence:** anon-2.jsonl:3368 · comment 297114159 · PR 3438 · 2022-04-26

## R-3369 — Corrected holdings EXPLAIN uses two roughly seven-second parallel sequential scans

**Source stance:** explanation

**Context:**

> rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/db/jdbc/InstrumentHoldingDaoJdbc.scala; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> I realized I executed explain analyse for wrong query previously. The correct analysis does not look too great
> 
> ```
> Merge Join  (cost=3249878.82..3407363.96 rows=108816 width=134) (actual time=15379.153..15464.994 rows=5966 loops=1)
>   Merge Cond: (x2.plan_id = instrument_holdings_v1_1.plan_id)
>   ->  Nested Loop  (cost=1624917.95..1777634.18 rows=1252 width=118) (actual time=7535.609..7599.196 rows=5966 loops=1)
>         ->  Finalize GroupAggregate  (cost=1624917.39..1629322.89 rows=17389 width=20) (actual time=7535.558..7546.409 rows=5966 loops=1)
>               Group Key: instrument_holdings_v1.plan_id
>               ->  Gather Merge  (cost=1624917.39..1628975.11 rows=34778 width=20) (actual time=7535.541..7541.183 rows=17881 loops=1)
>                     Workers Planned: 2
>                     Workers Launched: 2
>                     ->  Sort  (cost=1623917.37..1623960.84 rows=17389 width=20) (actual time=7530.338..7531.447 rows=5960 loops=3)
>                           Sort Key: instrument_holdings_v1.plan_id
>                           Sort Method: quicksort  Memory: 658kB
>                           Worker 0:  Sort Method: quicksort  Memory: 658kB
>                           Worker 1:  Sort Method: quicksort  Memory: 658kB
>                           ->  Partial HashAggregate  (cost=1622518.78..1622692.67 rows=17389 width=20) (actual time=7525.509..7527.290 rows=5960 loops=3)
>                                 Group Key: instrument_holdings_v1.plan_id
>                                 ->  Parallel Seq Scan on instrument_holdings_v1  (cost=0.00..1620104.33 rows=482889 width=20) (actual time=0.057..7210.369 rows=579172 loops=3)
>                                       Filter: ((business_date >= '2021-01-01'::date) AND (business_date <= '2021-12-31'::date) AND (market_value >= '0'::numeric) AND ((broker)::text = 'UOBKH_SGD_CASH'::text) AND ((instrument_id)::text = 'IE00BF20LB02'::text) AND ((ccy)::text = 'SGD'::text))
>                                       Rows Removed by Filter: 18646832
>         ->  Index Scan using instrument_holdings_v1_instrument_id_broker_id_business_date_pl on instrument_holdings_v1 x2  (cost=0.56..8.52 rows=1 width=102) (actual time=0.008..0.008 rows=1 loops=5966)
>               Index Cond: (((instrument_id)::text = 'IE00BF20LB02'::text) AND ((broker)::text = 'UOBKH_SGD_CASH'::text) AND (business_date = (min(instrument_holdings_v1.business_date))) AND (business_date >= '2021-01-01'::date) AND (business_date <= '2021-12-31'::date) AND (plan_id = instrument_holdings_v1.plan_id) AND ((ccy)::text = 'SGD'::text))
>               Filter: (market_value >= '0'::numeric)
>   ->  Finalize GroupAggregate  (cost=1624960.86..1629496.78 rows=17389 width=48) (actual time=7843.537..7862.449 rows=5966 loops=1)
>         Group Key: instrument_holdings_v1_1.plan_id
>         ->  Gather Merge  (cost=1624960.86..1629018.58 rows=34778 width=48) (actual time=7843.514..7849.588 rows=17879 loops=1)
>               Workers Planned: 2
>               Workers Launched: 2
>               ->  Sort  (cost=1623960.84..1624004.31 rows=17389 width=48) (actual time=7837.487..7838.726 rows=5960 loops=3)
>                     Sort Key: instrument_holdings_v1_1.plan_id
>                     Sort Method: quicksort  Memory: 1030kB
>                     Worker 0:  Sort Method: quicksort  Memory: 1030kB
>                     Worker 1:  Sort Method: quicksort  Memory: 1031kB
>                     ->  Partial HashAggregate  (cost=1622518.78..1622736.14 rows=17389 width=48) (actual time=7828.709..7833.764 rows=5960 loops=3)
>                           Group Key: instrument_holdings_v1_1.plan_id
>                           ->  Parallel Seq Scan on instrument_holdings_v1 instrument_holdings_v1_1  (cost=0.00..1620104.33 rows=482889 width=22) (actual time=0.068..7393.723 rows=579172 loops=3)
>                                 Filter: ((business_date >= '2021-01-01'::date) AND (business_date <= '2021-12-31'::date) AND (market_value >= '0'::numeric) AND ((broker)::text = 'UOBKH_SGD_CASH'::text) AND ((instrument_id)::text = 'IE00BF20LB02'::text) AND ((ccy)::text = 'SGD'::text))
>                                 Rows Removed by Filter: 18646832
> Planning Time: 0.701 ms
> Execution Time: 15466.966 ms
> ```
> 
> ‌
> 
> Table is “parallel seq scan”-ed 2 times - each takes 7s \(hence total ~15s\), without using index

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.

**Evidence:** anon-2.jsonl:3369 · comment 297130273 · PR 3438 · 2022-04-26

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/db/jdbc/InstrumentHoldingDaoJdbc.scala`

## R-3370 — Holdings index use differs between all-plan grouped and specific-plan queries

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> Updated the query analysis here [<url> data-inline-card='' }
> 
> But basically, when querying with broker, instrument, ccy and date range, with group by on planId: it uses parallel seq scan, no index used \(affect both approaches\)
> 
> ‌
> 
> When query with broker, instrument, ccy, date range and specific plan: it uses index created on the composite keys

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.

**Evidence:** anon-2.jsonl:3370 · comment 297134997 · PR 3438 · 2022-04-26

## R-3371 — October and January date ranges lead PostgreSQL to choose different scan plans

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> So it turns out that PG would switch to use sequential scan, instead of using index, if it \(somehow\) expects more rows to be returned \(I read [<url> data-inline-card='' } \)
> 
> ‌
> 
> In the above case:
> 
> * when querying with from\_date = 2021-10-01, both SUM \+ MIN and DISTINCT plans queries use index
> * when querying with from\_date = 2021-01-01, both use seq scan
> 
> So pg is doing its thing, and not an issue on our side.

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.

**Evidence:** anon-2.jsonl:3371 · comment 297392128 · PR 3438 · 2022-04-27

## R-3374 — Oops my bad: * Red and green box is approach in [<url> data-inline-card='' } , triggered with fromDate = 2021-10-01 \(not so much holding data\) and 2021-0

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> Oops my bad:
> 
> * Red and green box is approach in [<url> data-inline-card='' } , triggered with fromDate = 2021-10-01 \(not so much holding data\) and 2021-01-01 \(a lot holding data\)
> * Pink and blue box is approach in this PR, also triggered with fromDate = 2021-10-01 and 2021-01-01
> 
> ‌

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.

**Evidence:** anon-2.jsonl:3374 · comment 297460282 · PR 3438 · 2022-04-27

## R-3387 — Transaction override simulation returns diff without changing state or persisting events

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3529: IAO-156: Add internal endpoint to allow override transaction data

**Source-preserving request, proposal, or question:**

> ### Simulate only
> 
> Existing state \(via inspect\)
> 
> ```json
> {
>     "customerId": "[incidental identifier omitted]",
>     "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>     "transactionId": "[incidental identifier omitted]",
>     "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>     "ccy": "SGD",
>     "transactionType": "INVESTMENT",
>     "status": "CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION",
>     "goalId": "[incidental identifier omitted]",
>     "planId": "[incidental identifier omitted]",
>     "requestedAmount": 100,
>     "orders": []
> }
> ```
> 
> Request
> 
> ```json
> {
>     "transaction": {
>         "customerId": "[incidental identifier omitted]",
>         "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>         "transactionId": "[incidental identifier omitted]",
>         "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>         "ccy": "SGD",
>         "transactionType": "INVESTMENT",
>         "status": "SETTLEMENT_CONFIRMED",
>         "goalId": "[incidental identifier omitted]",
>         "planId": "[incidental identifier omitted]",
>         "requestedAmount": 100,
>         "settledAmount": 101.2,
>         "orders": [],
>         "convertedOrders": [],
>         "statusUpdatedDate": "2022-05-14T00:00:00Z"
>     },
>     "settledAt": "2022-05-14T22:10:00.000000+08:00[Asia/Singapore]",
>     "requestedBy": "<email>",
>     "reason": "Because I can",
>     "simulateOnly": true
> }
> ```
> 
> ‌
> 
> Response
> 
> ```json
> {
>     "simulateOnly": true,
>     "diff": [
>         {
>             "op": "add",
>             "path": "/settledAmount",
>             "value": 101.2
>         },
>         {
>             "op": "add",
>             "path": "/settledAt",
>             "value": "2022-05-14T22:10:00+08:00[Asia/Singapore]"
>         },
>         {
>             "op": "replace",
>             "path": "/status",
>             "value": "SETTLEMENT_CONFIRMED"
>         }
>     ]
> }
> ```
> 
> ‌
> 
> Results: State not change \+ no events
> 
> ‌

**Conditions and limits:**

- PR3529 sequence: simulation-only and real override evidence, identical/not-found errors, then a compare-and-set request/command check and the updated API/error response. Incidental UUIDs are omitted. Source rows: anon-2.jsonl:3387, anon-2.jsonl:3388, anon-2.jsonl:3389, anon-2.jsonl:3390, anon-2.jsonl:3391, anon-2.jsonl:3392.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3387 · comment 301724259 · PR 3529 · 2022-05-17

> ### Simulate only
> 
> Existing state \(via inspect\)
> 
> ```json
> {
>     "customerId": "

**Evidence:** anon-2.jsonl:3387 · comment 301724259 · PR 3529 · 2022-05-17

> ",
>     "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>     "transactionId": "

**Evidence:** anon-2.jsonl:3387 · comment 301724259 · PR 3529 · 2022-05-17

> ",
>     "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>     "ccy": "SGD",
>     "transactionType": "INVESTMENT",
>     "status": "CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION",
>     "goalId": "

**Evidence:** anon-2.jsonl:3387 · comment 301724259 · PR 3529 · 2022-05-17

> ",
>     "planId": "

**Evidence:** anon-2.jsonl:3387 · comment 301724259 · PR 3529 · 2022-05-17

> ",
>     "requestedAmount": 100,
>     "orders": []
> }
> ```
> 
> Request
> 
> ```json
> {
>     "transaction": {
>         "customerId": "

**Evidence:** anon-2.jsonl:3387 · comment 301724259 · PR 3529 · 2022-05-17

> ",
>         "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>         "transactionId": "

**Evidence:** anon-2.jsonl:3387 · comment 301724259 · PR 3529 · 2022-05-17

> ",
>         "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>         "ccy": "SGD",
>         "transactionType": "INVESTMENT",
>         "status": "SETTLEMENT_CONFIRMED",
>         "goalId": "

**Evidence:** anon-2.jsonl:3387 · comment 301724259 · PR 3529 · 2022-05-17

> ",
>         "planId": "

**Evidence:** anon-2.jsonl:3387 · comment 301724259 · PR 3529 · 2022-05-17

> ",
>         "requestedAmount": 100,
>         "settledAmount": 101.2,
>         "orders": [],
>         "convertedOrders": [],
>         "statusUpdatedDate": "2022-05-14T00:00:00Z"
>     },
>     "settledAt": "2022-05-14T22:10:00.000000+08:00[Asia/Singapore]",
>     "requestedBy": "<email>",
>     "reason": "Because I can",
>     "simulateOnly": true
> }
> ```
> 
> ‌
> 
> Response
> 
> ```json
> {
>     "simulateOnly": true,
>     "diff": [
>         {
>             "op": "add",
>             "path": "/settledAmount",
>             "value": 101.2
>         },
>         {
>             "op": "add",
>             "path": "/settledAt",
>             "value": "2022-05-14T22:10:00+08:00[Asia/Singapore]"
>         },
>         {
>             "op": "replace",
>             "path": "/status",
>             "value": "SETTLEMENT_CONFIRMED"
>         }
>     ]
> }
> ```
> 
> ‌
> 
> Results: State not change \+ no events
> 
> ‌

## R-3388 — Real transaction override changes state and persists CustomerTransactionOverriddenEvt

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3529: IAO-156: Add internal endpoint to allow override transaction data

**Source-preserving request, proposal, or question:**

> ### Real request
> 
> Existing state
> 
> ```json
> {
>     "customerId": "[incidental identifier omitted]",
>     "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>     "transactionId": "[incidental identifier omitted]",
>     "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>     "ccy": "SGD",
>     "transactionType": "INVESTMENT",
>     "status": "CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION",
>     "goalId": "[incidental identifier omitted]",
>     "planId": "[incidental identifier omitted]",
>     "requestedAmount": 100,
>     "orders": []
> }
> ```
> 
> ‌
> 
> Request
> 
> ```json
> {
>     "transaction": {
>         "customerId": "[incidental identifier omitted]",
>         "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>         "transactionId": "[incidental identifier omitted]",
>         "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>         "ccy": "SGD",
>         "transactionType": "INVESTMENT",
>         "status": "SETTLEMENT_CONFIRMED",
>         "goalId": "[incidental identifier omitted]",
>         "planId": "[incidental identifier omitted]",
>         "requestedAmount": 100,
>         "settledAmount": 101.2,
>         "orders": [],
>         "convertedOrders": [],
>         "statusUpdatedDate": "2022-05-14T00:00:00Z"
>     },
>     "settledAt": "2022-05-14T22:10:00.000000+08:00[Asia/Singapore]",
>     "requestedBy": "<email>",
>     "reason": "Because I can",
>     "simulateOnly": false
> }
> ```
> 
> ‌
> 
> Response
> 
> ```json
> {
>     "simulateOnly": false,
>     "diff": [
>         {
>             "op": "add",
>             "path": "/settledAmount",
>             "value": 101.2
>         },
>         {
>             "op": "add",
>             "path": "/settledAt",
>             "value": "2022-05-14T22:10:00+08:00[Asia/Singapore]"
>         },
>         {
>             "op": "replace",
>             "path": "/status",
>             "value": "SETTLEMENT_CONFIRMED"
>         }
>     ]
> }
> ```
> 
> ‌
> 
> Results:
> 
> New state
> 
> ```json
> {
>     "customerId": "[incidental identifier omitted]",
>     "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>     "transactionId": "[incidental identifier omitted]",
>     "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>     "ccy": "SGD",
>     "transactionType": "INVESTMENT",
>     "status": "SETTLEMENT_CONFIRMED",
>     "goalId": "[incidental identifier omitted]",
>     "planId": "[incidental identifier omitted]",
>     "requestedAmount": 100,
>     "settledAmount": 101.2,
>     "settledAt": "2022-05-14T22:10:00+08:00[Asia/Singapore]",
>     "orders": []
> }
> ```
> 
> ‌
> 
> New event
> 
> ```json
> {
>     "eventName": "package$CustomerTransactionOverriddenEvt",
>     "persistentId": "CustomerTransactionManagerEntity|[incidental identifier omitted]",
>     "partitionNumber": 0,
>     "sequenceNumber": 9,
>     "timeStamp": "2022-05-17T02:38:00.696Z",
>     "offSet": "[incidental identifier omitted]",
>     "event": {
>         "transaction": {
>             "customerId": "[incidental identifier omitted]",
>             "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>             "transactionId": "[incidental identifier omitted]",
>             "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>             "ccy": "SGD",
>             "transactionType": "INVESTMENT",
>             "status": "SETTLEMENT_CONFIRMED",
>             "goalId": "[incidental identifier omitted]",
>             "planId": "[incidental identifier omitted]",
>             "requestedAmount": 100,
>             "settledAmount": 101.2,
>             "settledAt": "2022-05-14T22:10:00+08:00[Asia/Singapore]",
>             "orders": []
>         },
>         "requestedBy": "<email>",
>         "reason": "Because I can"
>     },
>     "serializationManifest": "com.endowus.silver.transaction.impl.entities.customer.ces.events.package$CustomerTransactionOverriddenEvt"
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR3529 sequence: simulation-only and real override evidence, identical/not-found errors, then a compare-and-set request/command check and the updated API/error response. Incidental UUIDs are omitted. Source rows: anon-2.jsonl:3387, anon-2.jsonl:3388, anon-2.jsonl:3389, anon-2.jsonl:3390, anon-2.jsonl:3391, anon-2.jsonl:3392.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ### Real request
> 
> Existing state
> 
> ```json
> {
>     "customerId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>     "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>     "transactionId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>     "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>     "ccy": "SGD",
>     "transactionType": "INVESTMENT",
>     "status": "CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION",
>     "goalId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>     "planId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>     "requestedAmount": 100,
>     "orders": []
> }
> ```
> 
> ‌
> 
> Request
> 
> ```json
> {
>     "transaction": {
>         "customerId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>         "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>         "transactionId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>         "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>         "ccy": "SGD",
>         "transactionType": "INVESTMENT",
>         "status": "SETTLEMENT_CONFIRMED",
>         "goalId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>         "planId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>         "requestedAmount": 100,
>         "settledAmount": 101.2,
>         "orders": [],
>         "convertedOrders": [],
>         "statusUpdatedDate": "2022-05-14T00:00:00Z"
>     },
>     "settledAt": "2022-05-14T22:10:00.000000+08:00[Asia/Singapore]",
>     "requestedBy": "<email>",
>     "reason": "Because I can",
>     "simulateOnly": false
> }
> ```
> 
> ‌
> 
> Response
> 
> ```json
> {
>     "simulateOnly": false,
>     "diff": [
>         {
>             "op": "add",
>             "path": "/settledAmount",
>             "value": 101.2
>         },
>         {
>             "op": "add",
>             "path": "/settledAt",
>             "value": "2022-05-14T22:10:00+08:00[Asia/Singapore]"
>         },
>         {
>             "op": "replace",
>             "path": "/status",
>             "value": "SETTLEMENT_CONFIRMED"
>         }
>     ]
> }
> ```
> 
> ‌
> 
> Results:
> 
> New state
> 
> ```json
> {
>     "customerId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>     "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>     "transactionId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>     "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>     "ccy": "SGD",
>     "transactionType": "INVESTMENT",
>     "status": "SETTLEMENT_CONFIRMED",
>     "goalId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>     "planId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>     "requestedAmount": 100,
>     "settledAmount": 101.2,
>     "settledAt": "2022-05-14T22:10:00+08:00[Asia/Singapore]",
>     "orders": []
> }
> ```
> 
> ‌
> 
> New event
> 
> ```json
> {
>     "eventName": "package$CustomerTransactionOverriddenEvt",
>     "persistentId": "CustomerTransactionManagerEntity|

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>     "partitionNumber": 0,
>     "sequenceNumber": 9,
>     "timeStamp": "2022-05-17T02:38:00.696Z",
>     "offSet": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>     "event": {
>         "transaction": {
>             "customerId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>             "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>             "transactionId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>             "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>             "ccy": "SGD",
>             "transactionType": "INVESTMENT",
>             "status": "SETTLEMENT_CONFIRMED",
>             "goalId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>             "planId": "

**Evidence:** anon-2.jsonl:3388 · comment 301724607 · PR 3529 · 2022-05-17

> ",
>             "requestedAmount": 100,
>             "settledAmount": 101.2,
>             "settledAt": "2022-05-14T22:10:00+08:00[Asia/Singapore]",
>             "orders": []
>         },
>         "requestedBy": "<email>",
>         "reason": "Because I can"
>     },
>     "serializationManifest": "com.endowus.silver.transaction.impl.entities.customer.ces.events.package$CustomerTransactionOverriddenEvt"
> }
> ```
> 
> ‌

## R-3389 — Override rejects identical state and missing customer/transaction with distinct errors

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3529: IAO-156: Add internal endpoint to allow override transaction data

**Source-preserving request, proposal, or question:**

> ### Reject if no change
> 
> Response
> 
> ```json
> {
>     "error_code": "",
>     "name": "BadRequest",
>     "detail": "Provided transaction is identical to existing state"
> }
> ```
> 
> ‌
> 
> ### Reject if customer or transaction not found
> 
> ```json
> {
>     "error_code": "TRANSACTION_NOT_FOUND",
>     "name": "com.endowus.silver.transaction.api.exceptions.TransactionSvcException",
>     "detail": "Customer [[incidental identifier omitted]] does not have transaction with id [[incidental identifier omitted]]"
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR3529 sequence: simulation-only and real override evidence, identical/not-found errors, then a compare-and-set request/command check and the updated API/error response. Incidental UUIDs are omitted. Source rows: anon-2.jsonl:3387, anon-2.jsonl:3388, anon-2.jsonl:3389, anon-2.jsonl:3390, anon-2.jsonl:3391, anon-2.jsonl:3392.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3389 · comment 301724705 · PR 3529 · 2022-05-17

> ### Reject if no change
> 
> Response
> 
> ```json
> {
>     "error_code": "",
>     "name": "BadRequest",
>     "detail": "Provided transaction is identical to existing state"
> }
> ```
> 
> ‌
> 
> ### Reject if customer or transaction not found
> 
> ```json
> {
>     "error_code": "TRANSACTION_NOT_FOUND",
>     "name": "com.endowus.silver.transaction.api.exceptions.TransactionSvcException",
>     "detail": "Customer [

**Evidence:** anon-2.jsonl:3389 · comment 301724705 · PR 3529 · 2022-05-17

> ] does not have transaction with id [

**Evidence:** anon-2.jsonl:3389 · comment 301724705 · PR 3529 · 2022-05-17

> ]"
> }
> ```
> 
> ‌

## R-3392 — Updated expectedExistingTransaction/targetTransaction request and stale-state BadRequest

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3529: IAO-156: Add internal endpoint to allow override transaction data

**Source-preserving request, proposal, or question:**

> Updated the API to CAS style to protect the endpoint from concurrent modification
> 
> Request
> 
> ```json
> {
>     "expectedExistingTransaction": {
>         "transaction": {
>             "customerId": "[incidental identifier omitted]",
>             "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>             "transactionId": "[incidental identifier omitted]",
>             "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>             "ccy": "SGD",
>             "transactionType": "INVESTMENT",
>             "status": "CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION",
>             "goalId": "[incidental identifier omitted]",
>             "planId": "[incidental identifier omitted]",
>             "requestedAmount": 100,
>             "orders": [],
>             "convertedOrders": [],
>             "statusUpdatedDate": "2022-05-14T00:00:00Z"
>         }
>     },
>     "targetTransaction": {
>         "transaction": {
>             "customerId": "[incidental identifier omitted]",
>             "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>             "transactionId": "[incidental identifier omitted]",
>             "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>             "ccy": "SGD",
>             "transactionType": "INVESTMENT",
>             "status": "SETTLEMENT_CONFIRMED",
>             "goalId": "[incidental identifier omitted]",
>             "planId": "[incidental identifier omitted]",
>             "requestedAmount": 100,
>             "settledAmount": 101.2,
>             "orders": [],
>             "convertedOrders": [],
>             "statusUpdatedDate": "2022-05-14T00:00:00Z"
>         },
>         "settledAt": "2022-05-14T22:10:00.000000+08:00[Asia/Singapore]"
>     },
>     "requestedBy": "<email>",
>     "reason": "Because I can",
>     "simulateOnly": true
> }
> ```
> 
> ‌
> 
> Response
> 
> ```json
> {
>     "simulateOnly": true,
>     "diff": [
>         {
>             "op": "add",
>             "path": "/settledAmount",
>             "value": 101.2
>         },
>         {
>             "op": "add",
>             "path": "/settledAt",
>             "value": "2022-05-14T22:10:00+08:00[Asia/Singapore]"
>         },
>         {
>             "op": "replace",
>             "path": "/status",
>             "value": "SETTLEMENT_CONFIRMED"
>         }
>     ]
> }
> ```
> 
> ‌
> 
> If existing state has changed, service will log the diff. Since it should be rare, log should be ok - not adding another field to complicate the exception
> 
> ```json
> {
>     "error_code": "",
>     "name": "BadRequest",
>     "detail": "Existing transaction does not match provided expected state. Check logs to find the unexpected diff."
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR3529 sequence: simulation-only and real override evidence, identical/not-found errors, then a compare-and-set request/command check and the updated API/error response. Incidental UUIDs are omitted. Source rows: anon-2.jsonl:3387, anon-2.jsonl:3388, anon-2.jsonl:3389, anon-2.jsonl:3390, anon-2.jsonl:3391, anon-2.jsonl:3392.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> Updated the API to CAS style to protect the endpoint from concurrent modification
> 
> Request
> 
> ```json
> {
>     "expectedExistingTransaction": {
>         "transaction": {
>             "customerId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>             "transactionId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>             "ccy": "SGD",
>             "transactionType": "INVESTMENT",
>             "status": "CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION",
>             "goalId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "planId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "requestedAmount": 100,
>             "orders": [],
>             "convertedOrders": [],
>             "statusUpdatedDate": "2022-05-14T00:00:00Z"
>         }
>     },
>     "targetTransaction": {
>         "transaction": {
>             "customerId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>             "transactionId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>             "ccy": "SGD",
>             "transactionType": "INVESTMENT",
>             "status": "SETTLEMENT_CONFIRMED",
>             "goalId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "planId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "requestedAmount": 100,
>             "settledAmount": 101.2,
>             "orders": [],
>             "convertedOrders": [],
>             "statusUpdatedDate": "2022-05-14T00:00:00Z"
>         },
>         "settledAt": "2022-05-14T22:10:00.000000+08:00[Asia/Singapore]"
>     },
>     "requestedBy": "<email>",
>     "reason": "Because I can",
>     "simulateOnly": true
> }
> ```
> 
> ‌
> 
> Response
> 
> ```json
> {
>     "simulateOnly": true,
>     "diff": [
>         {
>             "op": "add",
>             "path": "/settledAmount",
>             "value": 101.2
>         },
>         {
>             "op": "add",
>             "path": "/settledAt",
>             "value": "2022-05-14T22:10:00+08:00[Asia/Singapore]"
>         },
>         {
>             "op": "replace",
>             "path": "/status",
>             "value": "SETTLEMENT_CONFIRMED"
>         }
>     ]
> }
> ```
> 
> ‌
> 
> If existing state has changed, service will log the diff. Since it should be rare, log should be ok - not adding another field to complicate the exception
> 
> ```json
> {
>     "error_code": "",
>     "name": "BadRequest",
>     "detail": "Existing transaction does not match provided expected state. Check logs to find the unexpected diff."
> }
> ```
> 
> ‌

## R-3400 — I guess you mean to remove this empty test?

**Source stance:** open-question

**Context:**

> portfolio-impl/src/test/scala/com/endowus/silver/portfolio/impl/PortfolioServiceImplTest.scala; PR 3398: Feat/IAO-93 block goal modification

**Source-preserving request, proposal, or question:**

> I guess you mean to remove this empty test?

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3400 · comment 295778212 · PR 3398 · 2022-04-20

Source path: `portfolio-impl/src/test/scala/com/endowus/silver/portfolio/impl/PortfolioServiceImplTest.scala`

## R-3414 — Trigger `POST /api/v2/report/monthly-statements` for 2022-03 in Staging [<url> ~16K active customers and ~11.5K sftp upload task, all completed in ~1.25hrs

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3332: SILVER-12449: Report service improments

**Source-preserving request, proposal, or question:**

> Trigger `POST /api/v2/report/monthly-statements` for 2022-03 in Staging
> 
> [<url>
> 
> ~16K active customers and ~11.5K sftp upload task, all completed in ~1.25hrs
> 
> ‌
> 
> Report generation task stats:
> 
> * p95 takes 2.5s
> * All transient failures were retried automatically, all hard failures are to due data issue \(missing sgd amount, mismatch broker account, invalid instrument\)
> 
> ‌
> 
> SFTP upload task stats:
> 
> * p95 takes 0.5s
> * No transient error 
> 
> ![](<url>
> ‌

**Evidence:** anon-2.jsonl:3414 · comment 292742481 · PR 3332 · 2022-04-06

## R-3415 — Delete the directory in SFTP server, and trigger `POST /api/v1/report/upload-document-sftp` for 2022-03 in Staging [<url> ‌ Result is consistent with previ

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3332: SILVER-12449: Report service improments

**Source-preserving request, proposal, or question:**

> Delete the directory in SFTP server, and trigger `POST /api/v1/report/upload-document-sftp` for 2022-03 in Staging
> 
> [<url>
> 
> ‌
> 
> Result is consistent with previous steps.  
> 
> ![](<url>
> ‌

**Evidence:** anon-2.jsonl:3415 · comment 292742688 · PR 3332 · 2022-04-06

## R-3416 — Example of hard failure cannot be cured with retry ``` c.l.l.s.a.t.TransportException: com.lightbend.lagom.scaladsl.persistence.PersistentEntity$InvalidCom

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3332: SILVER-12449: Report service improments

**Source-preserving request, proposal, or question:**

> Example of hard failure cannot be cured with retry
> 
> ```
> c.l.l.s.a.t.TransportException: com.lightbend.lagom.scaladsl.persistence.PersistentEntity$InvalidCommandException: Instrument [SG9999014005] does not exist!
> ```
> 
> ![](<url>
> ‌

**Evidence:** anon-2.jsonl:3416 · comment 292742927 · PR 3332 · 2022-04-06

## R-3417 — Example of transient failure that was retried automatically ``` java.io.IOException: Connection reset by peer ``` ![](<url> ‌

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3332: SILVER-12449: Report service improments

**Source-preserving request, proposal, or question:**

> Example of transient failure that was retried automatically
> 
> ```
> java.io.IOException: Connection reset by peer
> ```
> 
> ![](<url>
> ‌

**Evidence:** anon-2.jsonl:3417 · comment 292743182 · PR 3332 · 2022-04-06

## R-3418 — Report service was healthy in terms heap / gc / container’s memory utilization [<url> ![](<url> ‌

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3332: SILVER-12449: Report service improments

**Source-preserving request, proposal, or question:**

> Report service was healthy in terms heap / gc / container’s memory utilization
> 
> [<url>
> 
> ![](<url>
> ‌

**Evidence:** anon-2.jsonl:3418 · comment 292753993 · PR 3332 · 2022-04-06

## R-3458 — ```shell > echo "feat/SILVER-12505-multi-ccy-bugbe-simulation-" | sed 's/[^a-zA-Z0-9]/-/g' | cut -c -63 | sed 's/-$//' feat-SILVER-12505-multi-ccy-bugbe-si

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3146: Remove last hyphen in git branch label

**Source-preserving request, proposal, or question:**

> ```shell
> > echo "feat/SILVER-12505-multi-ccy-bugbe-simulation-" | sed 's/[^a-zA-Z0-9]/-/g' | cut -c -63 | sed 's/-$//'
> feat-SILVER-12505-multi-ccy-bugbe-simulation
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3458 · comment 284278631 · PR 3146 · 2022-03-01

## R-3459 — ```shell > echo "feat/---" | sed 's/[^a-zA-Z0-9]/-/g' | cut -c -63 | sed 's/-*$//' feat > echo "feat/SILVER-12505-multi-ccy-bugbe-simulation-@-?----" | sed

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3146: Remove last hyphen in git branch label

**Source-preserving request, proposal, or question:**

> ```shell
> > echo "feat/---" | sed 's/[^a-zA-Z0-9]/-/g' | cut -c -63 | sed 's/-*$//'     
> feat
> 
> > echo "feat/SILVER-12505-multi-ccy-bugbe-simulation-@-?----" | sed 's/[^a-zA-Z0-9]/-/g' | cut -c -63 | sed 's/-*$//'
> feat-SILVER-12505-multi-ccy-bugbe-simulation
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3459 · comment 284283394 · PR 3146 · 2022-03-01

## R-3463 — Dummy task to test serdes if we publish multiple tasks to the topic

**Source stance:** explanation

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/ReportKafkaService.scala; PR 3101: WIP Queue monthly statements in kafka

**Source-preserving request, proposal, or question:**

> Dummy task to test serdes if we publish multiple tasks to the topic

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3463 · comment 281656818 · PR 3101 · 2022-02-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/ReportKafkaService.scala`

## R-3484 — Tested this change with marketdata \+ instrument service in dev - both work fine. This PR doesn’t improve any speed, just move back to using non-root user,

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 2808: Run container with system user instead of root

**Source-preserving request, proposal, or question:**

> Tested this change with marketdata \+ instrument service in dev - both work fine.
> 
> This PR doesn’t improve any speed, just move back to using non-root user, because of security.
> 
> Fixed minor typo in the branch label

**Evidence:** anon-2.jsonl:3484 · comment 270245101 · PR 2808 · 2021-12-31

## R-3485 — Tested with gateway too. It comes up alright and dev env is functional

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 2808: Run container with system user instead of root

**Source-preserving request, proposal, or question:**

> Tested with gateway too. It comes up alright and dev env is functional

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3485 · comment 270858887 · PR 2808 · 2022-01-05

## R-3486 — Tested `document` service in dev too. Able to create new customer \+ upload some documents \+ view them in adminUI.

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 2808: Run container with system user instead of root

**Source-preserving request, proposal, or question:**

> Tested `document` service in dev too. Able to create new customer \+ upload some documents \+ view them in adminUI.

**Evidence:** anon-2.jsonl:3486 · comment 273364167 · PR 2808 · 2022-01-18

## R-3504 — Goal modify summary has soft validation; confirmation has hard validation under the FE contract

**Source stance:** requested-change

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/GoalModifySummaryBehaviour.scala; PR 3019: SILVER-11923: Factors goal modify summary/confirmation

**Source-preserving request, proposal, or question:**

> As we discussed, this is during summary - these fields are not required. I just add soft validation here just in case - but our contract w FE is that they won’t send it until confirmation.
> 
> The summary response would contain correct data, and FE supposes to use that in confirmation step. Hence it’s hard validation there, not here.

**Evidence:** anon-2.jsonl:3504 · comment 279066034 · PR 3019 · 2022-02-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/GoalModifySummaryBehaviour.scala`

## R-3514 — Deployed to `staging` together with actual Factors changes. Created new goal / modified goal / invested new funding source, and observe no serdes error \(r

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 2979: SILVER-11940: Add new ProductLineAndIntent for Factors

**Source-preserving request, proposal, or question:**

> Deployed to `staging` together with actual Factors changes. Created new goal / modified goal / invested new funding source, and observe no serdes error \(related to goal\)
> 
> Kibana URL \(lots of filter because we have lots of other noises\)
> 
> ```
> <url>
> ```
> 
> ![](<url>
> ‌

**Evidence:** anon-2.jsonl:3514 · comment 277347036 · PR 2979 · 2022-02-04

## R-3515 — Historical question about TestContainers versus EmbeddedPostgres and in-memory tests

**Source stance:** open-question

**Context:**

> General PR discussion; PR 2962: TestContainer Trial

**Source-preserving request, proposal, or question:**

> Are we planning to make use of TestContainers for full fledge e2e integration tests, in which DB state is shared between tests? Otherwise I’m not sure if it’s worth the trouble just to test Postgres related pieces.
> 
> If we trust Slick, we should already be agnostic to the underlying database, and hence can potentially use another DB driver that supports in-memory for unit tests, instead of EmbeddedPostgres. If we don’t trust, then we should just write tests to explicitly test Slick, without repository logic.
> 
> ‌

**Conditions and limits:**

- The TestContainers/EmbeddedPostgres discussion is historical and the concern is followed by acceptance of the clarification. It is not a blanket rejection of database integration tests. Source rows: anon-2.jsonl:3515, anon-2.jsonl:3516.

**Evidence:** anon-2.jsonl:3515 · comment 276984427 · PR 2962 · 2022-02-03

## R-3517 — Added `Deleted` to the cases in `deleteRelatedTransaction` I see `DeleteCmd` is already handled correctly by the entity if in `Deleted` state

**Source stance:** reported-verification

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/common/DividendDeleter.scala; PR 2835: SILVER-11314: Fetch DividendState from entity before deleting to handle lag between DividendJdbcEventProcessor and DividendEventProcessor

**Source-preserving request, proposal, or question:**

> Added `Deleted` to the cases in `deleteRelatedTransaction`
> 
> I see `DeleteCmd` is already handled correctly by the entity if in `Deleted` state

**Evidence:** anon-2.jsonl:3517 · comment 272457921 · PR 2835 · 2022-01-13

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/common/DividendDeleter.scala`

## R-3529 — I’m not what’s wrong, but after I switch to use random, the test becomes flaky. I will raise separate PR to follow up on this later, if that’s ok :pray:

**Source stance:** reported-verification

**Context:**

> dividend-impl/src/test/scala/com/endowus/silver/dividend/impl/common/ReinvestedDividendDataSyncHelperTest.scala; PR 2833: SILVER-11229: Fix settlement date for dividend reinvestment

**Source-preserving request, proposal, or question:**

> I’m not what’s wrong, but after I switch to use random, the test becomes flaky.
> 
> I will raise separate PR to follow up on this later, if that’s ok :pray: 

**Evidence:** anon-2.jsonl:3529 · comment 272792244 · PR 2833 · 2022-01-14

Source path: `dividend-impl/src/test/scala/com/endowus/silver/dividend/impl/common/ReinvestedDividendDataSyncHelperTest.scala`

## R-3534 — Yeah it’s weird. If I revert, the test consistently passing. If I use random, it’s very flaky - fail very frequently locally

**Source stance:** reported-verification

**Context:**

> dividend-impl/src/test/scala/com/endowus/silver/dividend/impl/common/ReinvestedDividendDataSyncHelperTest.scala; PR 2833: SILVER-11229: Fix settlement date for dividend reinvestment

**Source-preserving request, proposal, or question:**

> Yeah it’s weird. If I revert, the test consistently passing. If I use random, it’s very flaky - fail very frequently locally

**Evidence:** anon-2.jsonl:3534 · comment 272794430 · PR 2833 · 2022-01-14

Source path: `dividend-impl/src/test/scala/com/endowus/silver/dividend/impl/common/ReinvestedDividendDataSyncHelperTest.scala`

## R-3583 — I think we should make this method returns the instrumentIds only - and let its caller invoke instrumentService. It will make it simpler to write test too.

**Source stance:** suggestion

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/StatementDataGenerator.scala; PR 2739: include instruments from transactions as well to build cache

**Source-preserving request, proposal, or question:**

> I think we should make this method returns the instrumentIds only - and let its caller invoke instrumentService. It will make it simpler to write test too. No need to mock

**Evidence:** anon-2.jsonl:3583 · comment 267447941 · PR 2739 · 2021-12-15

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/StatementDataGenerator.scala`

## R-3587 — Goal modify futures are constructed sequentially and tested as three dependent steps

**Source stance:** reported-verification

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/GoalModifyConfirmationBehaviour.scala; PR 2697: SILVER-10548: Implement GoalModifyConfirmation for Income

**Source-preserving request, proposal, or question:**

> The futures are created sequentially. So we will do these 3 step by step. I have tests for those cases too

**Evidence:** anon-2.jsonl:3587 · comment 266219213 · PR 2697 · 2021-12-09

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/GoalModifyConfirmationBehaviour.scala`

## R-3594 — As chatted, I’ll check how we can write svcImplTest with real entity \(and hopefully without too much saga about mock entity > test driver > real entity :f

**Source stance:** requested-change

**Context:**

> advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala; PR 2643: SILVER-10408: Minor rename/refactor ProductLine implementation to better express the design pattern. Implement ExistingGoalDetail for Income

**Source-preserving request, proposal, or question:**

> As chatted,
> 
>   
> I’ll check how we can write svcImplTest with real entity \(and hopefully without too much saga about mock entity > test driver > real entity :fingers_crossed: \)  
>   
> For this API, everything happens in svc, and entity is only involved to return current state. Ok-ish to use mock.

**Conditions and limits:**

- These historical testing comments distinguish service orchestration mocks, entity-driver tests, and possible end-to-end tests; they do not state a universal no-mocks or embedded-database mandate. Source rows: anon-2.jsonl:3594, anon-2.jsonl:3597, anon-2.jsonl:3604, anon-2.jsonl:3605.

**Evidence:** anon-2.jsonl:3594 · comment 264683558 · PR 2643 · 2021-12-02

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala`

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

## R-3596 — This is a dump from Technology satellite portfolio with a few manual edits. Will sync again after we have the Income portfolio created in Staging. ‌ Also w

**Source stance:** explanation

**Context:**

> advisory-impl/src/test/resources/mock/productPortfolio.conf; PR 2612: SILVER-10375: Support addAdvisoryTag for Income. Add /advisory/edge/income/portfolios

**Source-preserving request, proposal, or question:**

> This is a dump from Technology satellite portfolio with a few manual edits. Will sync again after we have the Income portfolio created in Staging.
> 
> ‌
> 
> Also will look into split it into smaller chunks, since we might want to test them separately for goal create/modify summary flow

**Evidence:** anon-2.jsonl:3596 · comment 264013916 · PR 2612 · 2021-11-30

Source path: `advisory-impl/src/test/resources/mock/productPortfolio.conf`

## R-3597 — I generally prefer e2e tests over mock tests… but haven’t figured out how to write them effectively yet. The below seems to be the pattern we follow in oth

**Source stance:** suggestion

**Context:**

> advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala; PR 2612: SILVER-10375: Support addAdvisoryTag for Income. Add /advisory/edge/income/portfolios

**Source-preserving request, proposal, or question:**

> I generally prefer e2e tests over mock tests… but haven’t figured out how to write them effectively yet. The below seems to be the pattern we follow in other services

**Conditions and limits:**

- These historical testing comments distinguish service orchestration mocks, entity-driver tests, and possible end-to-end tests; they do not state a universal no-mocks or embedded-database mandate. Source rows: anon-2.jsonl:3594, anon-2.jsonl:3597, anon-2.jsonl:3604, anon-2.jsonl:3605.

**Evidence:** anon-2.jsonl:3597 · comment 264014034 · PR 2612 · 2021-11-30

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala`

## R-3603 — Yes it’s a dump \(from Satellite - Technology\) for now, since I don’t care about its content. Will review once we impl goal create/modify - hopefully can 

**Source stance:** explanation

**Context:**

> advisory-impl/src/test/resources/mock/productPortfolio.conf; PR 2612: SILVER-10375: Support addAdvisoryTag for Income. Add /advisory/edge/income/portfolios

**Source-preserving request, proposal, or question:**

> Yes it’s a dump \(from Satellite - Technology\) for now, since I don’t care about its content.
> 
> Will review once we impl goal create/modify - hopefully can use more correct data for Income portfolio then
> 
> ‌

**Evidence:** anon-2.jsonl:3603 · comment 264024132 · PR 2612 · 2021-11-30

Source path: `advisory-impl/src/test/resources/mock/productPortfolio.conf`

## R-3604 — ServiceImplTest mocks client boundaries; EntityTest checks command, state, events and response

**Source stance:** requested-change

**Context:**

> advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala; PR 2612: SILVER-10375: Support addAdvisoryTag for Income. Add /advisory/edge/income/portfolios

**Source-preserving request, proposal, or question:**

> [incidental identifier omitted] So we have 2 types of test:
> 
> * \*ServiceImplTest: use mock/stub for everything, and test the processing logic in \*ServiceImpl, e.g. request-to-command transformation, API composition
> * \*EntityTest: use persistence entity driver and test using command, verifying state \+ event\(s\) \+ response
> 
> ‌
> 
> I see ChargeServiceImplTest also follows this pattern.
> 
> The added AdvisoryServiceImplTest here also also follows that.
> 
> ‌
> 
> In scope of this PR, there is no change at entity level, hence no new tests added.

**Conditions and limits:**

- These historical testing comments distinguish service orchestration mocks, entity-driver tests, and possible end-to-end tests; they do not state a universal no-mocks or embedded-database mandate. Source rows: anon-2.jsonl:3594, anon-2.jsonl:3597, anon-2.jsonl:3604, anon-2.jsonl:3605.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3604 · comment 264025007 · PR 2612 · 2021-11-30

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala`

>  So we have 2 types of test:
> 
> * \*ServiceImplTest: use mock/stub for everything, and test the processing logic in \*ServiceImpl, e.g. request-to-command transformation, API composition
> * \*EntityTest: use persistence entity driver and test using command, verifying state \+ event\(s\) \+ response
> 
> ‌
> 
> I see ChargeServiceImplTest also follows this pattern.
> 
> The added AdvisoryServiceImplTest here also also follows that.
> 
> ‌
> 
> In scope of this PR, there is no change at entity level, hence no new tests added.

## R-3605 — Historical e2e exploration from ServiceImpl avoids committing to flaky EmbeddedCassandra

**Source stance:** suggestion

**Context:**

> advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala; PR 2612: SILVER-10375: Support addAdvisoryTag for Income. Add /advisory/edge/income/portfolios

**Source-preserving request, proposal, or question:**

> e2e tests, if any, should have entry point starting from \*ServiceImpl, and somehow use actual entity. It seems Lagom recommends using EmbeddedCassandra to glue these, but from my experience, EmbeddedCassandra is a hot mess - flaky and slow.
> 
> I will think about this in the background.

**Conditions and limits:**

- These historical testing comments distinguish service orchestration mocks, entity-driver tests, and possible end-to-end tests; they do not state a universal no-mocks or embedded-database mandate. Source rows: anon-2.jsonl:3594, anon-2.jsonl:3597, anon-2.jsonl:3604, anon-2.jsonl:3605.

**Evidence:** anon-2.jsonl:3605 · comment 264025311 · PR 2612 · 2021-11-30

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala`

